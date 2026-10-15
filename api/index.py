import sys
import os

# Add root directory to path so it can import vidyut7
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your core logic or define the Vercel WSGI/ASGI handler app here
try:
    import vidyut7
    # If vidyut7 exposes an app or we can wrap its request handler
    app = getattr(vidyut7, 'app', None)
except Exception as e:
    def app(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b"Vercel Python Error: " + str(e).encode()]