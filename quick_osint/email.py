import webbrowser

def check_breach(email):
    """Check email breaches using free services."""
    url = f"https://www.dehashed.com/search?query={email}"
    webbrowser.open(url)
    return {"message": "Opened browser for email breach check."}
