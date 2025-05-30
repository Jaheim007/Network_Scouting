import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ftp_scanner import scan_ftp
import json

from core.http_scanner import scan_http
import json

# Replace with an IP/port you control or know
result = scan_http("192.168.1.108", 80)
print(json.dumps(result, indent=2))

