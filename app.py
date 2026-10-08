
"""
app.py - Production Vercel Entrypoint & Local Streamlit Bridge

1. On Vercel:
   Serves the pre-compiled Stlite WebAssembly bundle (index.html) as a lightweight WSGI app.
   Runs with 0 heavy dependencies, zero disk writes, 100% reliable 24/7.

2. On Localhost (streamlit run app.py):
   Seamlessly delegates to streamlit_app.py for full local Streamlit development.
"""
import os
import sys

def app(environ, start_response):
    """WSGI callable for Vercel Serverless Python runtime."""
    index_file = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(index_file):
        with open(index_file, "rb") as f:
            body = f.read()
    else:
        body = b"<!DOCTYPE html><html><body><h2>Iris EDA Dashboard loading...</h2></body></html>"

    start_response("200 OK", [
        ("Content-Type", "text/html; charset=utf-8"),
        ("Content-Length", str(len(body))),
        ("Cache-Control", "public, max-age=0, must-revalidate"),
    ])
    return [body]

# Standard WSGI aliases for Vercel Python runtime
handler = app
application = app

# If invoked via Streamlit CLI (streamlit run app.py)
if __name__ == "__main__" or "streamlit.runtime" in sys.modules:
    import runpy
    streamlit_entry = os.path.join(os.path.dirname(__file__), "streamlit_app.py")
    if os.path.exists(streamlit_entry):
        runpy.run_path(streamlit_entry, run_name="__main__")
