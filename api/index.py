import sys
import os

# Ensure the root folder is in the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def app(environ, start_response):
    """Vercel Serverless Function entry point handler."""
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    
    html_output = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>VIDYUT · Industrial Energy Telemetry Dashboard</title>
        <style>
            body { font-family: 'Inter', system-ui, sans-serif; background: #0b0f17; color: #f1f5f9; padding: 40px; text-align: center; }
            .card { background: #151e2e; border: 1px solid #26334d; border-radius: 16px; max-width: 650px; margin: 40px auto; padding: 40px; box-shadow: 0 8px 30px rgba(0,0,0,0.6); }
            h1 { color: #0ea5e9; font-size: 26px; font-weight: 800; margin-bottom: 10px; }
            .sub { color: #38bdf8; font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; font-weight: 700; margin-bottom: 20px; }
            p { color: #94a3b8; line-height: 1.6; font-size: 14px; }
            .badge { display: inline-block; background: #0ea5e926; color: #38bdf8; border: 1px solid #0ea5e940; padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 700; margin-top: 15px; }
            .footer { margin-top: 30px; font-size: 12px; color: #64748b; }
            a { color: #38bdf8; text-decoration: none; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>VIDYUT</h1>
            <div class="sub">Visualised Industrial Dashboard for Yield &amp; Utility Tracking</div>
            <p><strong>Zawarmala Mine &amp; Chanderiya Smelter Operations</strong></p>
            <p>Your full multi-threaded EMS backend, Modbus TCP gateway simulator, SQLite database, and high-performance operator HMI are fully active locally on your workstation.</p>
            <div class="badge">Vercel Edge Prototype Mode Active</div>
            <p class="footer">For complete live telemetry and plant automation control, access your local server at <br><code>http://localhost:8080</code></p>
        </div>
    </body>
    </html>
    """
    return [html_output.encode('utf-8')]
