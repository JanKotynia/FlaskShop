from shop import app
from shop.chat import chat_bp
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(debug=1)