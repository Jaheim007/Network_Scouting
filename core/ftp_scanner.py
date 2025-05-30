from ftplib import FTP
import socket

def scan_ftp(ip, port=21):
    print(f"📂 Scanning FTP on {ip}:{port}")
    result = {
        "ip": ip,
        "port": port,
        "ftp_access": False,
        "files": [],
        "error": None
    }

    try:
        ftp = FTP()
        ftp.connect(ip, port, timeout=5)
        ftp.login()  # anonymous login by default

        result["ftp_access"] = True
        files = ftp.nlst()
        result["files"] = files
        ftp.quit()
    except Exception as e:
        result["error"] = str(e)

    return result
