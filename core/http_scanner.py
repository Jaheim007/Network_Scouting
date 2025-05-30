import requests
from bs4 import BeautifulSoup

def scan_http(ip, port=80):
    url = f"http://{ip}:{port}/"
    print(f"🌐 Scanning HTTP on {url}")
    result = {
        "ip": ip,
        "port": port,
        "http_access": False,
        "files": [],
        "error": None
    }

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            result["http_access"] = True
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')

            files = []
            for link in links:
                href = link.get('href')
                if href and not href.startswith('?') and href != '/':
                    files.append(href)

            result["files"] = files
        else:
            result["error"] = f"HTTP Status: {response.status_code}"

    except Exception as e:
        result["error"] = str(e)

    return result
