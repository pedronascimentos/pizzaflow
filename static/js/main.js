function showCustomNotification(text) {
    const notification = document.createElement('div');
    notification.className = 'notification-card';
    notification.innerHTML = `<strong style="color: black">Novo Pedido!</strong><br>${text}`;
    document.body.appendChild(notification);

    // Força a animação de entrada

    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 500); 
    }, 5000);
}



function updateNavbarBadge() {
    const badge = document.getElementById('ifood-badge');
    if (badge) {
        let currentCount = parseInt(badge.textContent, 10);
        badge.textContent = currentCount + 1;
        badge.classList.remove('is-hidden');
    }
}

async function checkForNewIfoodOrders() {
    try {
        const response = await fetch('/api/ifood/liberar-proximo');
        
        if (response.status === 200) {
            const newOrder = await response.json();
            console.log("Novo pedido recebido (ciclo infinito):", newOrder);
            showCustomNotification(`Cliente: ${newOrder.cliente_nome}`);
            updateNavbarBadge();
        } 
    } catch (error) {
        console.error("Erro ao verificar por novos pedidos:", error);
    }
}


document.addEventListener('DOMContentLoaded', () => {


    const columns = document.querySelectorAll('.kanban-cards');
    if (columns.length > 0) {
        columns.forEach(column => {
            new Sortable(column, {
                group: 'kanban',
                animation: 150,
                ghostClass: 'is-ghost',
                onEnd: (evt) => {
                    const card = evt.item;
                    const toColumn = evt.to;
                    const pedidoId = card.dataset.id;
                    const novoStatus = toColumn.dataset.status;

                    fetch('/pedidos/mover', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: `pedido_id=${pedidoId}&novo_status=${novoStatus}`
                    });
                }
            });
        });
    }


    if (document.querySelector('.kanban-board')) {
        console.log("Iniciando timer infinito para verificar pedidos do iFood...");
        const pedidoTimer = setInterval(checkForNewIfoodOrders, 15000);
    }

    const assignModal = document.getElementById('assign-employee-modal');
    const assignBtns = document.querySelectorAll('.assign-employee-btn');
    const modalPedidoIdInput = document.getElementById('modal-pedido-id');


    const openModal = () => assignModal.classList.add('is-active');
    const closeModal = () => assignModal.classList.remove('is-active');


    assignBtns.forEach(btn => {
        btn.addEventListener('click', (event) => {
            // Pega o ID do pedido do card pai
            const card = event.currentTarget.closest('.card');
            const pedidoId = card.dataset.id;
            modalPedidoIdInput.value = pedidoId;
            openModal();
        });
    });

    assignModal.querySelector('.modal-background').addEventListener('click', closeModal);
    assignModal.querySelector('.delete').addEventListener('click', closeModal);
    assignModal.querySelector('#cancel-assign').addEventListener('click', closeModal);
});