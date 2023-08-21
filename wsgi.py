# wsgi.py

from main import wsapp  # Replace 'your_flask_app' with your actual Flask application

if __name__ == "__main__":
    from waitress import serve
    serve(wsapp, host="0.0.0.0", port=80)  # Adjust host and port as needed
