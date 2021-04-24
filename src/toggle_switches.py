from gpiozero import Button


class SwitchConfig():
    """Configuration class for each switch"""

    def __init__(self, pin, domains):
        self.pin = pin # Uses Broadcom (BCM) pin numbering
        self.domains = domains
        self.button = Button(self.pin)
        self.button.when_pressed = self.set_active
        self.button.when_released = self.set_inactive
        self.state = self.button.is_pressed
        self.previous_state = self.state

    def set_active(self):
        print('Blocking {}'.format(self.domains))
        self.state = True

    def set_inactive(self):
        print('Unblocking {}'.format(self.domains))
        self.state = False

    def is_active(self):
        """Returns the state of the switch"""
        return self.state

    def get_config_lines(self):
        """Builds the address config line"""
        lines = []
        for domain in self.domains:
            lines.append("address=/{}/127.0.0.1".format(domain))
        return lines

    def should_refresh_config(self):
        if self.previous_state != self.state:
            # Should refresh config
            self.previous_state = self.state
            return True
        return False


SWITCHES = [
    SwitchConfig(18, ['facebook.com', 'messenger.com']),
    SwitchConfig(24, ['instagram.com']),
]
