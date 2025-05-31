import socket

def check_port(ip, port):
    timeout = 0.5  # globalni timeout u sekundama
    socket.setdefaulttimeout(timeout)
    print(f"[INFO] Globalni timeout:  {timeout} sekundi")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((ip, port))
        print(f"[OK] Port {port} na adresi {ip} je otvoren.")
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        print(f"[FAIL] Port {port} na adresi {ip} je zatvoren ili nedostupan. ({e})")
    finally:
        sock.close()

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port_number = 80
    print(f"[INFO] Provjeravam port {port_number} na IP adresi {ip_address}")
    check_port(ip_address, port_number)
