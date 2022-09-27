import socket


def ipconfig():
    try:
        host_name = socket.gethostname()
        ipv4 = socket.gethostbyname(host_name)
        ipv6 = list(map(int, ipv4.split('.')))
        print("Ethernet adapter Ethernet")
        print("Name. . . . . . . . . . .", host_name)
        print("IPv4 Address. . . . . . . . . . .", ipv4)
        print("IPv6 Address. . . . . . . . . . .", '2002:{:02x}{:02x}:{:02x}{:02x}::'.format(*ipv6))
    except:
        print("Unable to get Hostname and IP")


ipconfig()
