from http.server import BaseHTTPRequestHandler
import sys
import os

# Add root directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Simple WSGI / Vercel Serverless Handler
def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    
    html_content = """
    <html>
        <head><title>VIDYUT Industrial EMS</title></head>
        <body style="font-family:Arial; text-align:center; padding-top:50px; background:#0f172a; color:#f8fafc;">
            <h1>VIDYUT Industrial Energy Telemetry Dashboard</h1>
            <p style="color:#94a3b8;">Platform deployed successfully on Vercel preview/prototype mode.</p>
            <div style="margin-top:30px; padding:20px; background:#1e293b; display:inline-block; border-radius:8px;">
                <p>Core telemetry engine and Modbus gateway are active locally.</p>
                <a href="https://github.com/Dashlo-Technologies-Private-Limited/vidyut" style="color:#38bdf8;">View Repository on GitHub</a>
            </div>
        </body>
    </html>
    """
    return [html_content.encode('utf-8')]
