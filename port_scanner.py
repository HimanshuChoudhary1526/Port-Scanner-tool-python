#Submitted by Himanshu Choudhary 
import argparse
import nmap

def argument_parser():
    """Allow the user to specify the target host and port"""
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and list of ports. Scan attempts to identify the service running on a port.")

    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list, such as '25,80,8080'")
    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary
    return var_args

def nmap_scan(host_id, port_num):
    """Use nmap utility to check host ports for status."""
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    return f"[*] {host_id} tcp/{port_num} {state}"


if __name__ == '_main_':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["ports"]
        
        if not host or not ports:
            raise ValueError("Error, please provide both host and port arguments.")
        
        ports = ports.split(",")  # Make a list from port numbers
        for port in ports:
            print(nmap_scan(host, port))
    except ValueError as e:
        print(e)





