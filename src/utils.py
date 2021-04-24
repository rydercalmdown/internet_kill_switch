import os
import subprocess
from toggle_switches import SWITCHES


def get_pi_network_ip_address():
    """Return the current IP of the pi on the network"""
    cmd = "ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'"
    return str(subprocess.check_output(cmd, shell=True).decode('utf-8')).strip()


def build_listen_address_config_line():
    """Returns the listen-address config line"""
    return "listen-address=::1,127.0.0.1,{}".format(get_pi_network_ip_address())


def build_address_config_line(domain):
    """Builds the address config line"""
    return "address=/{}/127.0.0.1".format(domain)


def build_config_file():
    """Builds the DNSmasq config file"""
    config_lines = [
        'dhcp-mac=set:client_is_a_pi,B8:27:EB:*:*:*',
        'dhcp-reply-delay=tag:client_is_a_pi,2',
        'interface=lo',
        'interface=wlan0',
        'server=8.8.8.8',
        'server=8.8.4.4',
    ]
    config_lines.append(build_listen_address_config_line())
    for switch in SWITCHES:
        if switch.is_active():
            config_lines = config_lines + switch.get_config_lines()
    return config_lines


def write_config_file(lines):
    """Writes the config file for dnsmasq"""
    config_file_path = '/etc/dnsmasq.conf'
    with open(config_file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')


def restart_dnsmasq():
    """Restart dnsmasq"""
    cmd = 'sudo systemctl stop dnsmasq && sudo systemctl start dnsmasq'
    subprocess.check_output(cmd, shell=True)


def update_dnsmasq_config():
    """Update DNSmasq config"""
    write_config_file(build_config_file())
    restart_dnsmasq()


def setup():
    """Sets up dnsmasq daemon"""
    update_dnsmasq_config()
