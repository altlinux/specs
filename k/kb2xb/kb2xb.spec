Name:    kb2xb
Version: 1.1.2
Release: alt1

Summary: Keyboard + Mouse - Xbox One virtual gamepad
License: MIT
Group:   System/Configuration/Hardware
URL:     https://github.com/janyel-lima/kb2xb

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Requires: python3
Requires: python3-module-evdev
Requires: python3-module-uinput
Requires: python3-module-pyside6

BuildArch: noarch

%description
Keyboard + Mouse - Xbox One virtual gamepad
(evdev/uinput, Wayland & X11, profile-based)

Maps any keyboard (and optionally a mouse) to a virtual Xbox One controller
that any game or emulator sees as a real gamepad - no configuration inside
the game required.

%prep
%setup

%build

%install
install -Dm644 kb2xb.py     %buildroot%_datadir/%name/kb2xb.py
install -Dm644 kb2xb_gui.py %buildroot%_datadir/%name/kb2xb_gui.py

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
exec python3 %_datadir/%name/kb2xb.py "$@"
EOF

cat > %buildroot%_bindir/%name-gui <<'EOF'
#!/bin/sh
exec python3 %_datadir/%name/kb2xb_gui.py "$@"
EOF

chmod +x %buildroot%_bindir/%name %buildroot%_bindir/%name-gui

install -Dm644 kb2xb.desktop          %buildroot%_desktopdir/%name.desktop
install -Dm644 icon.svg               %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dm644 completions/kb2xb.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm644 completions/_kb2xb     %buildroot%_datadir/zsh/site-functions/_%name
install -Dm644 completions/kb2xb.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc LICENSE README.md
%_bindir/%name
%_bindir/%name-gui
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_kb2xb
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Fri Aug 21 2026 Sergey Palcheh <minergenon@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
