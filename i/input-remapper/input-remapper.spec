Name: input-remapper
Version: 2.1.1
Release: alt1

Summary: An easy to use tool to change the behaviour of your input devices

License: GPL-3.0
Group: Development/Python3
Url: https://github.com/sezanzeb/input-remapper

# Source-url: https://github.com/sezanzeb/input-remapper/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires(pre): python3-module-setuptools python3-module-wheel

BuildArch: noarch

AutoProv: no

#Requires: libgtksourceview4-gir
Requires: typelib(GtkSource) = 4

# see ALT bug 49653
Requires: python3(pydantic)

%description
An easy to use tool to change the behaviour of your input devices.
Supports X11, Wayland, combinations, programmable macros, joysticks, wheels,
triggers, keys, mouse-movements and more. Maps any input to any other input.

%prep
%setup
subst 's|/usr/lib/udev/rules.d|%_udevrulesdir|' setup.py
subst 's|/usr/lib/systemd/system|%_unitdir|' setup.py

%build
%pyproject_build

%install
%pyproject_install
%python3_prune
# hack 
mv %buildroot%python3_sitelibdir/etc %buildroot
mv %buildroot%python3_sitelibdir/usr/{bin,share} %buildroot/usr
mv %buildroot%python3_sitelibdir/usr/lib/{systemd,udev} %buildroot/usr/lib
chmod a+x %buildroot%_bindir/*

%files
%doc README.md
%_bindir/input-remapper-control
%_bindir/input-remapper-gtk
%_bindir/input-remapper-reader-service
%_bindir/input-remapper-service
%python3_sitelibdir/inputremapper/
%python3_sitelibdir/input_remapper-*.dist-info/
%_sysconfdir/xdg/autostart/input-remapper-autoload.desktop
%_unitdir/input-remapper.service
%_udevrulesdir/99-input-remapper.rules
%_datadir/dbus-1/system.d/inputremapper.Control.conf
%_datadir/applications/input-remapper-gtk.desktop
%_datadir/metainfo/io.github.sezanzeb.input_remapper.metainfo.xml
%_datadir/polkit-1/actions/input-remapper.policy
%_datadir/input-remapper/
%_iconsdir/hicolor/scalable/apps/input-remapper.svg

%changelog
* Sun Mar 02 2025 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1
- switch to pyproject build

* Tue Mar 12 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- add Requires: python3(pydantic) (ALT bug 49653)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Sat May 27 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Sisyphus

* Sat May 27 2023  <saahriktu@andromeda> 2.0.0-althckr10.1
- Initial package
