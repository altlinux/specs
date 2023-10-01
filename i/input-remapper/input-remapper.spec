Name: input-remapper
Version: 2.0.1
Release: alt1

Summary: An easy to use tool to change the behaviour of your input devices

License: GPL-3.0
Group: Development/Python3
Url: https://github.com/sezanzeb/input-remapper

# Source-url: https://github.com/sezanzeb/input-remapper/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro

BuildArch: noarch

AutoProv: no

#Requires: libgtksourceview4-gir
Requires: typelib(GtkSource) = 4

%description
An easy to use tool to change the behaviour of your input devices.
Supports X11, Wayland, combinations, programmable macros, joysticks, wheels,
triggers, keys, mouse-movements and more. Maps any input to any other input.

%prep
%setup
subst 's|/usr/lib/udev/rules.d|%_udevrulesdir|' setup.py
subst 's|/usr/lib/systemd/system|%_unitdir|' setup.py

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.md
%_bindir/input-remapper-control
%_bindir/input-remapper-gtk
%_bindir/input-remapper-reader-service
%_bindir/input-remapper-service
%python3_sitelibdir/inputremapper/
%python3_sitelibdir/input_remapper-*.egg-info/
%_sysconfdir/dbus-1/system.d/inputremapper.Control.conf
%_sysconfdir/xdg/autostart/input-remapper-autoload.desktop
%_unitdir/input-remapper.service
%_udevrulesdir/99-input-remapper.rules
%_datadir/applications/input-remapper-gtk.desktop
%_datadir/input-remapper/*
%_datadir/metainfo/io.github.sezanzeb.input_remapper.metainfo.xml
%_datadir/polkit-1/actions/input-remapper.policy

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Sat May 27 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Sisyphus

* Sat May 27 2023  <saahriktu@andromeda> 2.0.0-althckr10.1
- Initial package
