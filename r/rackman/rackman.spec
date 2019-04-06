# TODO: wait for python3 gtk
Name: rackman
Version: 1.12.0
Release: alt1

Summary: A tool measure distances on the screen

License: GPL
Group: Graphics
Url: https://github.com/FRiMN/Rackman

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/FRiMN/Rackman/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArchitectures: noarch

BuildRequires(pre): rpm-build-intro

%py_use pygtk

%description
A tool measure distances on the screen.

%prep
%setup
subst "s|/usr/share/rackman|%_sysconfdir/%name|g" setup.py rackman.py

%build
%python_build

%install
%python_install
%find_lang %name

rm -rf %buildroot/usr/lib/

%files -f %name.lang
%_bindir/%name
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/rackman.conf
%_mandir/ru/man1/%name.*
%_docdir/%name/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop

%changelog
* Sat Apr 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- initial build for ALT Sisyphus
