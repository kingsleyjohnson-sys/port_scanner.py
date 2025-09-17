# port_scanner.py
import socket
import argparse

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1.0)
                result = sock.connect_ex((host, port))
                state = "OPEN" if result == 0 else "CLOSED"
                print(f"Port {port}: {state}")
        except KeyboardInterrupt:
            print("\nScan stopped by user.")
            return
        except socket.gaierror:
            print("Hostname could not be resolved.")
            return
        except socket.error:
            print("Couldn't connect to server.")
            return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("target", nargs="?", default="scanme.nmap.org", help="Target hostname or IP")
    parser.add_argument("--ports", nargs="*", type=int, default=[21,22,80,443],
                        help="List of ports to scan (default: 21 22 80 443)")
    args = parser.parse_args()

    scan_ports(args.target, args.ports)
