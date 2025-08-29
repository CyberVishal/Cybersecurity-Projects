# 🔐 Simple Port Scanner
# Author: Your Name
# Description: Scans for open ports on a target system.

import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def main():
    target = input("Enter target IP address: ")
    print(f"\n🔍 Scanning target: {target}\n")
    
    for port in range(20, 1025):  # scanning ports 20–1024
        scan_port(target, port)

if __name__ == "__main__":
    main()
