"""
AI Chatbot - Flask Application Entry Point
A ChatGPT-style AI chatbot with streaming responses, conversation management,
and a premium glassmorphism UI.
"""

import os
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ─── App Factory ──────────────────────────────────────────────────────────────

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Initialize database
    from database.models import init_db
    init_db()

    # Create uploads directory
    uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)

    # ─── Register Blueprints ──────────────────────────────────────────────

    from routes.chat import chat_bp
    from routes.settings import settings_bp

    app.register_blueprint(chat_bp)
    app.register_blueprint(settings_bp)

    # ─── Main Routes ─────────────────────────────────────────────────────

    @app.route('/')
    def index():
        """Serve the main application page."""
        return render_template('index.html')

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        """Serve uploaded files."""
        return send_from_directory(uploads_dir, filename)

    # ─── Error Handlers ──────────────────────────────────────────────────

    @app.errorhandler(404)
    def not_found(e):
        """Handle 404 errors."""
        return {'error': 'Resource not found', 'status': 404}, 404

    @app.errorhandler(500)
    def server_error(e):
        """Handle 500 errors."""
        return {'error': 'Internal server error', 'status': 500}, 500

    @app.errorhandler(413)
    def too_large(e):
        """Handle file too large errors."""
        return {'error': 'File too large. Maximum size is 16MB.', 'status': 413}, 413

    return app


# ─── Run the Application ─────────────────────────────────────────────────────

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'

    print(f"""
==================================================
           AI Chatbot is running!

   Local:   http://localhost:{port}
   Debug:   {debug}

   Press Ctrl+C to stop the server
==================================================
    """)

    app.run(host='0.0.0.0', port=port, debug=debug)
