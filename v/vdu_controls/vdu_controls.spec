Name:    vdu_controls
Version: 2.6.9
Release: alt1

Summary: Visual Display Unit virtual control panel
License: GPL-3.0-or-later
Group:   System/Configuration/Other
URL:     https://digitaltrails.github.io/vdu_controls/
VCS:     https://github.com/digitaltrails/vdu_controls

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3
Requires: ddcutil
Requires: i2c-tools
Requires: brightnessctl
Requires: python3-module-PyQt6
Requires: python3-module-PyQt5
Requires: python3-module-pyudev
Requires: python3-module-serial
Requires: python3-module-opencv
Requires: ImageMagick-tools
Requires: v4l-utils
Requires: xdg-utils

BuildArch: noarch

%description
vdu_controls is a virtual control panel for externally connected
VDUs (visual display units). Controls are included for backlight
brightness, and contrast. vdu_controls uses the ddcutil command
line utility to interact with external displays via VESA Display
Data Channel (DDC) Virtual Control Panel (VCP) standards.

%prep
%setup

%build
# No build required.

%install
install -dm755 %buildroot%_bindir \
               %buildroot%_mandir/man1/ \
               %buildroot%_datadir/applications \
               %buildroot%_datadir/%name \
               %buildroot%_datadir/%name/translations \
               %buildroot%_datadir/%name/icons \
               %buildroot%_datadir/%name/sample-scripts \
               %buildroot%_datadir/icons/hicolor/256x256/apps

# Copy the Python package into the private app directory.
cp -r src/%name %buildroot%_datadir/%name

# Install assets.
install -m644 %name.desktop %buildroot%_datadir/applications/%name.desktop
install -m644 src/%name/resources/icons/app/%name.svg \
        %buildroot%_datadir/icons/hicolor/256x256/apps/%name.svg
install -m644 icons/* %buildroot%_datadir/%name/icons/
install -m644 translations/*.ts %buildroot%_datadir/%name/translations/
install -m755 sample-scripts/* %buildroot%_datadir/%name/sample-scripts/
install -m644 docs/_build/man/%name.1 %buildroot%_mandir/man1/

# Byte-compile the installed Python sources (brp-alt does not touch /usr/share/vdu_controls).
python3 -m compileall -q -f %buildroot%_datadir/%name

# Install the wrapper script that launches the private package.
install -m755 packaging/%name.wrapper %buildroot/%_bindir/%name

%files
%doc LICENSE.md README.md
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/256x256/apps/%name.svg
%_mandir/man1/%name.1*
%dir %_datadir/%name/
%_datadir/%name/%name/
%_datadir/%name/icons/
%_datadir/%name/translations/
%dir %_datadir/%name/sample-scripts/
%_datadir/%name/sample-scripts/lux-from-webcam.bash
%_datadir/%name/sample-scripts/laptop-ddcutil-emulator.bash
%_datadir/%name/sample-scripts/lux-from-webcam.py
%_datadir/%name/sample-scripts/vlux_meter.py
%_datadir/%name/sample-scripts/__pycache__/

%changelog
* Wed Aug 12 2026 Sergey Palcheh <minergenon@altlinux.org> 2.6.9-alt1
- new version 2.6.9

* Wed Aug 05 2026 Sergey Palcheh <minergenon@altlinux.org> 2.6.8-alt1
- new version 2.6.8

* Sat Jul 11 2026 Sergey Palcheh <minergenon@altlinux.org> 2.6.5-alt1
- new version 2.6.5
- switch to PyQt6 and the new src/vdu_controls package layout
- add explicit Requires for python3-module-PyQt6 and python3-module-PyQt5
  (vlux_meter.py still uses PyQt5)

* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 2.6.0-alt1
- new version 2.6.0

* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Sat Feb 22 2025 Sergey Palcheh <minergenon@altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus
