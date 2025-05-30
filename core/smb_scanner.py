from impacket.smbconnection import SMBConnection
import socket

def scan_smb_shares(ip):
    print(f"📁 Scanning SMB shares on {ip}")
    try:
        conn = SMBConnection(ip, ip, timeout=3)
        conn.login('', '')  # Anonymous login attempt

        shares = conn.listShares()
        share_results = []

        for share in shares:
            share_name = share['shi1_netname'][:-1]
            try:
                files = conn.listPath(share_name, '*')
                file_list = [f.get_longname() for f in files if f.is_file()]
                share_results.append({
                    "share": share_name,
                    "files": file_list
                })
            except Exception as e:
                share_results.append({
                    "share": share_name,
                    "files": [],
                    "error": str(e)
                })

        return {
            "ip": ip,
            "shares": share_results
        }

    except Exception as e:
        return {
            "ip": ip,
            "error": f"Connection failed: {str(e)}"
        }
