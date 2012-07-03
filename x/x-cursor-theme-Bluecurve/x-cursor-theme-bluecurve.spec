%define themename Bluecurve

Name: x-cursor-theme-%themename
Version: 0.120
Release: alt1

Summary: Cursors for Xorg

License: GPL
Group: System/X11
BuildArch: noarch

Source: %name-%version.tar.gz

Conflicts: xorg-x11-server <= 1:1.0.2-alt5

Packager: Valery Inozemtsev <shrek@altlinux.ru>

%description
This package contains cursors for Xorg.

%prep
%setup -q -c

%install
%__install -d %buildroot%_iconsdir/
%__cp -a %themename %buildroot%_iconsdir/

%files
%_iconsdir/%themename

%changelog
* Sat Mar 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.120-alt1
- update to 0.120

* Wed Aug 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.73-alt1
- initial release

