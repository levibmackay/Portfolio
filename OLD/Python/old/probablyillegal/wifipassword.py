import nmap
import socket

def main():
    subnet = "10.255.0.0/24"
    scanner = nmap.PortScanner()

    print(f"Scanning {subnet} for live hosts (ping sweep)...")
    scanner.scan(hosts=subnet, arguments='-sn')

    live_hosts = scanner.all_hosts()
    if not live_hosts:
        print("No live hosts found.")
        return

    print(f"Found {len(live_hosts)} live hosts:\n")
    for host in live_hosts:
        try:
            hostname = socket.gethostbyaddr(host)[0]
        except socket.herror:
            hostname = "(no hostname)"
        print(f"{host} - {hostname}")

if __name__ == "__main__":
    main()
