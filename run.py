from app import create_app
import criar_db


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
