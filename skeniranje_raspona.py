
import socket

def check_port(ip, port):
    timeout = 0.5
    socket.setdefaulttimeout(timeout)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((ip, port))
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "Nepoznat servis"
        print(f"[OPEN] Port {port} ({service}) na {ip} je otvoren.")
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
    finally:
        sock.close()

def scan_range(ip, start_port, end_port):
    print(f"\nSkeniram {ip} od porta {start_port} do {end_port}...")
    for port in range(start_port, end_port + 1):
        check_port(ip, port)

if __name__ == "__main__":
    try:
        start_port = int(input("Unesi početni port (npr. 20): "))
        end_port = int(input("Unesi završni port (npr. 1024): "))
        if not (0 < start_port <= 65535 and 0 < end_port <= 65535 and start_port <= end_port):
            raise ValueError
    except ValueError:
        print("Neispravan unos portova. Moraju biti cijeli brojevi između 1 i 65535 i start ≤ end.")
        exit(1)

    scan_range("localhost", start_port, end_port)
