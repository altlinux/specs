Name: xorg-server-control
Version: 1.4
Release: alt1

Summary: The XOrg server facility control
License: GPL
Group: System/X11
BuildArch: noarch

Obsoletes: xorg-x11-server-control, xfree86-server-control

Source: xorg-server.control

%description
This package contains control rules for X11 server facility.
See control(8) for details.

%install
install -pD -m755 %SOURCE0 %buildroot%_controldir/xorg-server

%files
%config %_controldir/*

%changelog
* Thu Apr 10 2025 Arseny Maslennikov <arseny@altlinux.org> 1.4-alt1
- Introduced unprivileged (a.k.a. rootless) mode for X servers.
  In this mode, just like in restricted mode, X servers have no way
  to gain root privileges, but can be executed by any user.
  Rootless mode makes sense in a KMS/DRM environment.

* Sun Jan 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Recognize X server placed in one of the following locations:
  /usr/bin/Xorg /usr/X11R6/bin/Xorg /usr/X11R6/bin/XFree86.

* Fri Nov 25 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- build for Xorg-7.0 (BINARY=/usr/bin/Xorg)

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added help.

* Sat Aug 28 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- Renamed to xorg-server-control.

* Mon Oct 06 2003 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
