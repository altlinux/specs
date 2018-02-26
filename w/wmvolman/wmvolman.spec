# vim: set ft=spec: -*- rpm-spec -*-

Name: wmvolman
Version: 1.0
Release: alt1.1

Summary: Window Maker Volume Manager
Group: Graphical desktop/Window Maker
License: GPLv2
Url: http://people.altlinux.ru/~raorn/wmvolman.html

Requires: udisks >= 1.0.0

Packager: Sir Raorn <raorn@altlinux.ru>

Source: http://people.altlinux.ru/~raorn/%name-%version.tar.bz2
Patch: wmvolman-1.0-alt-DSO.patch

# Automatically added by buildreq on Fri May 05 2006
BuildRequires: libdbus-glib-devel libdockapp-devel udisks-devel

%description
wmVolMan is a small volume manager for Window Maker. For now
it only displays and allows mounting and unmounting removable
media and hotpluggable devices that are added to or removed
from the system. It uses D-BUS and HAL to listen for new
devices.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%_bindir/%name
%dir %_datadir/%name/
%dir %_datadir/%name/default/
%_datadir/%name/default/*.xpm

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build

* Mon Oct 04 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0-alt1
- [1.0]
 + Rewritten from HAL to UDisks
 + New icons for BlueRay and HD DVD media

* Thu Jan 03 2008 Sir Raorn <raorn@altlinux.ru> 0.9-alt1
- [0.9]
 + Gracefully handle DBus and Hal restarts

* Sun Sep 16 2007 Sir Raorn <raorn@altlinux.ru> 0.8-alt1
- [0.8]
 + "Device busy" indicator
- License set to GPLv2

* Tue Aug 29 2006 Sir Raorn <raorn@altlinux.ru> 0.7-alt1
- [0.7]
 + Added README, described HAL properties and theming
 + Added CD-audio and "unknown" CD icons
 + Added support for memory cards (CF/MS/SD/MMC/SM)
 + Fixed and improved icon fallback

* Sat Jul 15 2006 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt2
- GIT snapshot v0.6.1-g8dbe9c2
 + Fixed dvd_plus_r/rw drive type detection
 + Added CF/MS/SD/MMC/SM cards icons

* Wed Apr 26 2006 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- Fixed fdi location

* Wed Apr 26 2006 Sir Raorn <raorn@altlinux.ru> 0.6-alt1
- Built for Sisyphus

