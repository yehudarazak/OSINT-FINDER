import requests

def search_username(username, platform):
    """Search for a username on specified platforms."""
    urls = {
        "twitter": f"https://twitter.com/{username}",
        "instagram": f"https://www.instagram.com/{username}/",
        "github": f"https://github.com/{username}",
    }
    if platform not in urls:
        return {"error": f"Platform {platform} not supported"}

    url = urls[platform]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return {"message": f"Username '{username}' found on {platform}!"}
        else:
            return {"message": f"Username '{username}' not found on {platform}."}
    except Exception as e:
        return {"error": f"Failed to search username: {e}"}
