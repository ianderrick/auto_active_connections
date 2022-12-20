import socket

# create an AF_INET, STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# get a list of active connections
active_connections = s.connections()

# create a file named "active_connections_HOSTNAME"
with open("active_connections_{}".format(host), "w") as f:
    for conn in active_connections:
# get service name
        service = socket.getservbyport(conn.lport)
# get resolved hostname
        addr = socket.gethostbyaddr(conn.rhost)
# write connection info to file
        f.write("{}:{} ({}) => {}\n".format(conn.lhost, conn.lport, service, addr))
