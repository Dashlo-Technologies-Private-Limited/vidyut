import sys
import os

# Add root directory to path so it can locate vidyut7_3.py (or your core script)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Attempt to import your main application module
    import vidyut7_3 as core_app
except ImportError:
    try:
        import vidyut7 as core_app
    except ImportError:
        core_app = None

def app(environ, start_response):
    """Vercel Python serverless entry point handler."""
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    
    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>VIDYUT · Vercel Preview Mode</title>
        <style>
            body {{ font-family: Inter, system-ui, sans-serif; background: #0b0f17; color: #f1f5f9; padding: 40px; text-align: center; }}
            .card {{ background: #151e2e; border: 1px solid #26334d; border-radius: 12px; max-width: 600px; margin: 40px auto; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
            h1 {{ color: #0ea5e9; font-size: 24px; }}
            p {{ color: #94a3b8; line-height: 1.5; }}
            a {{ color: #38bdf8; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>VIDYUT Industrial Energy Telemetry Dashboard</h1>
            <p>Platform successfully linked to Vercel edge/serverless wrapper.</p>
            <p>Your full multi-threaded EMS backend, Modbus TCP pollers, and SQLite telemetry engine are running locally on your plant workstation. For complete local control, access via <code>http://localhost:8080</code>.</p>
            <p style="margin-top: 20px;"><a href="https://github.com/Dashlo-Technologies-Private-Limited/vidyut" target="_blank">View GitHub Repository</a></p>
        </div>
    </body>
    </html>
    """
    return [html_output.encode('utf-8')]
