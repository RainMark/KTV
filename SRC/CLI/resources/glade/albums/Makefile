INSTALL_PATH=~/.local/share/icons/hicolor/128x128/apps

all: install

install: uninstall
	@install -Dm 644 *.png $(INSTALL_PATH)

uninstall:
	@rm -rf $(INSTALL_PATH)/stv_*.png
