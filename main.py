from app import app, load_app

load_app(app)

if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True, reloader=False) 