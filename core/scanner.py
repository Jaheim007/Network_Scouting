import nmap
import yaml

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

target_ports = []
for ports in config["ports"].values():
    target_ports.extend(ports)
ports_str = ",".join(str(p) for p in target_ports)

def scan_network(target_network):
    print(f"🔍 Scanning {target_network} on ports {ports_str}")
    nm = nmap.PortScanner()
    nm.scan(hosts=target_network, arguments=f"-p {ports_str} --open -T4")
    
    results = []
    for host in nm.all_hosts():
        host_data = {
            "ip": host,
            "hostname": nm[host].hostname(),
            "open_ports": [],
        }
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                service = nm[host][proto][port]["name"]
                host_data["open_ports"].append({"port": port, "service": service})
        results.append(host_data)
    return results
