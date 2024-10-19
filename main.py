from port_scanner import scan_ports
from vulnerability_scanner import check_vulnerability
from exploitation_tool import exploit

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Vulnerability Scanner")
    print("3. Exploitation Tool")
    choice = input("Select an option (1-3): ")

    if choice == '1':
        target = input("Enter the target IP address: ")
        scan_ports(target)
    elif choice == '2':
        url = input("Enter the target URL: ")
        check_vulnerability(url)
    elif choice == '3':
        target = input("Enter the target IP address: ")
        exploit(target)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
