Name:    game-device-udev
Version: 0.24
Release: alt1

Summary: udev rules for game-devices
License: MIT
Group:   System/Configuration/Hardware
Url:     https://codeberg.org/fabiscafe/game-devices-udev
VCS:     https://codeberg.org/fabiscafe/game-devices-udev.git

Source: %name-%version.tar
Source1: uinput.conf

Requires: udev

BuildArch: noarch

%description
udev rules to make supported controllers available with user rights

%prep
%setup

%build

%install
#Installs rules
install -dm755 %buildroot%_udevrulesdir/
cp *.rules %buildroot%_udevrulesdir/
#uinput
install -Dm644 %SOURCE1 %buildroot%_modules_loaddir/uinput.conf

%files
%doc LICENSE README.md
%_udevrulesdir/*.rules
%_modules_loaddir/uinput.conf

%changelog
* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 0.24-alt1
- new version (0.24) with rpmgs script via gear-uupdate

* Tue Feb 25 2025 Sergey Palcheh <minergenon@altlinux.org> 0.23-alt1
- initial build for ALT Sisyphus

