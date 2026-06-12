Name:    vdu_controls
Version: 2.6.0
Release: alt1

Summary: Visual Display Unit virtual control panel
License: GPL-3.0
Group:   System/Configuration/Other
URL:     https://github.com/digitaltrails/vdu_controls

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Requires: ddcutil
Requires: i2c-tools

BuildArch: noarch

%description
vdu_controls is a virtual control panel for externally connected
VDUs (visual display units).  Controls are included for backlight
brightness, and contrast.  vdu_controls uses the ddcutil command
line utility to interact with external displays via VESA Display
Data Channel (DDC) Virtual Control Panel (VCP) standards.

%prep
%setup

%build
#Just a placeholder, no build required.

%install
install -dm755 %buildroot%_bindir \
               %buildroot%_mandir/man1/ \
               %buildroot%_datadir/applications \
               %buildroot%_datadir/%name/translations \
               %buildroot%_datadir/%name/icons \
               %buildroot%_datadir/%name/sample-scripts \
               %buildroot%_datadir/icons/hicolor/256x256/apps
install -m755 %name.py  %buildroot/%_bindir/%name
install -m644 %name.desktop %buildroot%_datadir/applications/%name.desktop
install -m644 %name.png %buildroot%_datadir/icons/hicolor/256x256/apps/%name.png
install -m644 icons/* %buildroot%_datadir/%name/icons/
install -m644 translations/*.ts %buildroot%_datadir/%name/translations/
install -m644 translations/about_*.txt %buildroot%_datadir/%name/translations/
install -m755 sample-scripts/* %buildroot%_datadir/%name/sample-scripts/
install -m644 docs/_build/man/%name.1 %buildroot%_mandir/man1/

%files
%doc LICENSE.md README.md
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/256x256/apps/%name.png
%_mandir/man1/%name.1*
%dir %_datadir/%name/
%_datadir/%name/icons/
%_datadir/%name/translations/
%dir %_datadir/%name/sample-scripts/
%_datadir/%name/sample-scripts/lux-from-webcam.bash
%_datadir/%name/sample-scripts/laptop-ddcutil-emulator.bash
%_datadir/%name/sample-scripts/lux-from-webcam.py
%_datadir/%name/sample-scripts/vlux_meter.py

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 2.6.0-alt1
- new version 2.6.0

* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Sat Feb 22 2025 Sergey Palcheh <minergenon@altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus

