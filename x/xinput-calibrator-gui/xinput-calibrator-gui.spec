Name: xinput-calibrator-gui
Version: 1.0
Release: alt1

Summary: GUI for touchscreen calibrating
Summary(ru_RU.UTF-8): Графический интерфейс калибровки сенсорного экрана

License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://abf.io/import/xinput-calibrator-gui
# Source-url: https://abf.io/import/xinput-calibrator-gui.git (ROSA import, tag rosa2021.1-1.0-14; license GPLv3 as declared in the ROSA spec)
Source: %name-%version.tar
Patch: %name-alt.patch

AutoProv: nopython3
BuildArch: noarch

BuildRequires: rpm-build-python3

Requires: /usr/bin/xinput_calibrator
Requires: /usr/bin/pkexec

%add_python3_path %_datadir/%name

%description
Graphical front end for the xinput_calibrator utility: runs the calibration,
writes the result to /etc/X11/xorg.conf.d/99-calibration.conf, allows to
adjust touch sensitivity (FingerLow/FingerHigh) and to disable misclick
detection. Useful for interactive boards, panels and kiosks.

%description -l ru_RU.UTF-8
Графический интерфейс для утилиты xinput_calibrator: запускает калибровку,
записывает результат в /etc/X11/xorg.conf.d/99-calibration.conf, позволяет
настроить чувствительность (FingerLow/FingerHigh) и отключить обнаружение
ложных нажатий (misclick). Подходит для интерактивных досок, панелей и киосков.

%prep
%setup
%patch -p1

%install
install -D -m 0644 xinput-calibrator-gui.py %buildroot%_datadir/%name/%name.py
install -D -m 0644 xinputcalibrator_classes.py %buildroot%_datadir/%name/xinputcalibrator_classes.py
chmod 0755 %buildroot%_datadir/%name/%name.py
mkdir -p %buildroot%_bindir
ln -s ../share/%name/%name.py %buildroot%_bindir/%name
install -D -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -D -m 0644 %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for Sisyphus
