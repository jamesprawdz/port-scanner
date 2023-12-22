import socket
from concurrent.futures import ThreadPoolExecutor

# Define the target host
target = "example.com"
# Convert the host to its IPv4 address if it's a domain name
target_ip = socket.gethostbyname(target)


def scan_port(port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the socket
            s.settimeout(1)
            # Connect to the target on the specified port
            s.connect((target_ip, port))
            print(f"Port {port} is open.")
    except (socket.timeout, socket.error):
        pass  # The port is closed or can't be reached


# The range of ports to scan
port_range = range(1, 1025)

# Using ThreadPoolExecutor to scan ports in parallel
with ThreadPoolExecutor(max_workers=100) as executor:
    # Map the function to the ports
    executor.map(scan_port, port_range)

print("Scan completed.")
