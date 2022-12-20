import socket

# Create an AF_INET, STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Get a list of active connections
active_connections = s.connections()

# Create a file named "active_connections_HOSTNAME"
with open("active_connections_{}".format(host), "w") as f:
    for conn in active_connections:
# Get service name
        service = socket.getservbyport(conn.lport)
# Get resolved hostname
        addr = socket.gethostbyaddr(conn.rhost)
# Write connection info to file
        f.write("{}:{} ({}) => {}\n".format(conn.lhost, conn.lport, service, addr))
