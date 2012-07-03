Name: mini-screenshoter
Version: 0.1
Release: alt3

Summary: The LXDE Screenshot Tool 
License: LGPL2+
Group: Graphical desktop/GNOME
Url: http://lubuntu.gip-gip.com
Packager: LXDE Development Team <lxde at packages.altlinux.org>
BuildArch: noarch

Source0: %name-%version.tar.gz
Source1: mini-screenshoter.desktop

Requires: scrot

%description
The LXDE Screenshot Tool

%prep
%setup -q

%install
mkdir %buildroot
cp -R * %buildroot
install -Dp -m0644 %SOURCE1 %buildroot%_datadir/applications/

%files
%_bindir/*
%_datadir/applications/mini-screenshoter.desktop

%changelog
* Fri Jan 14 2011 Radik Usupov <radik@altlinux.org> 0.1-alt3
- Fix screenshoter scripts (thanks raorn@)

* Tue Jan 11 2011 Radik Usupov <radik@altlinux.org> 0.1-alt2
- Changed script

* Mon Dec 06 2010 Radik Usupov <radik@altlinux.org> 0.1-alt1
- Initial build

