from app import app, load_app

load_app(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, reloader=True) 