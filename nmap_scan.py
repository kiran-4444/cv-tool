"""
This module provides utility functions to scan the network
"""

import socket
import nmap


def get_ip_from_mac(mac_address) -> str | None:
    """
    Get the IP address of a host with the given MAC address.
    :param mac_address: MAC address of the host
    :return: IP address of the host
    """
    nm = nmap.PortScanner()

    nm.scan(hosts="192.168.0.255/24", arguments="-sP -sn", sudo=True)
    hosts_list = [(x, nm[x]["addresses"].get("mac")) for x in nm.all_hosts()]

    ip_addr = None
    for host, mac_addr in hosts_list:
        if mac_addr == mac_address:
            print(f"Host found: {host}")
            ip_addr = host
            break

    return ip_addr


def get_host_ip_address() -> str | None:
    """
    Get the IP address of the current host.
    :return: IP address of the current host
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external server to get the current IP address
        # The IP address here (8.8.8.8) is a Google DNS server, which is just used to
        # determine the outbound IP address; no data is sent.
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception as _:
        ip_address = None
    finally:
        s.close()

    return ip_address
