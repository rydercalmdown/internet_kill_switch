import time
import utils
from toggle_switches import SWITCHES

def main():
    """Run the application"""
    print('Starting application...')
    utils.setup()
    print('IP Address is {}'.format(utils.get_pi_network_ip_address()))
    print('Running application...')
    try:
        while True:
            for switch in SWITCHES:
                if switch.should_refresh_config():
                    print('Refreshing config')
                    utils.update_dnsmasq_config()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Shutting down...')


if __name__ == "__main__":
    main()
