import socket

def scan_ports(target):
    print(f"Scanning ports on {target}...")
    for port in range(1, 1025):  # Scanning ports 1-1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()

if __name__ == "__main__":
    target_input = input("Enter the target IP address: ")
    scan_ports(target_input)
