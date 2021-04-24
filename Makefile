RASPBERRY_PI_IP=10.0.0.10
RASPBERRY_PI_USERNAME=pi


.PHONY: install
install:
	@cd deployment && bash install.sh

.PHONY: run
run:
	@cd src && sudo ../env/bin/python app.py

.PHONY: copy
copy:
	@echo "Copying to raspberry pi"
	rsync -r $(shell pwd) --exclude env --exclude data $(RASPBERRY_PI_USERNAME)@$(RASPBERRY_PI_IP):/home/$(RASPBERRY_PI_USERNAME)

.PHONY: shell
shell:
	@echo "Connecting to raspberry pi"
	@ssh $(RASPBERRY_PI_USERNAME)@$(RASPBERRY_PI_IP)

.PHONY: configure-on-boot
configure-on-boot:
	@echo "Configuring /etc/rc.local"
	@cd deployment && bash configure_on_boot.sh
