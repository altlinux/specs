Summary: QEMU GUI written in Qt5
Name: aqemu
Version: 0.9.2
Release: alt0.1
License: GPL2
Group: Emulators
Packager: Boris Savelev <boris@altlinux.org>
Url: https://github.com/tobimensch/aqemu
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Wed Mar 04 2009
BuildRequires(pre): cmake
BuildRequires: gcc-c++ libvncserver-devel ImageMagick
BuildRequires: qt5-base-devel

%description
AQEMU is a QEMU GUI written in Qt5.
The program have user-friendly interface and allows to set up the majority of QEMU options.

%prep
%setup

%build
%cmake
PATH=%{_datadir}/qt5/bin:$PATH; export PATH
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
mkdir -p %buildroot%_desktopdir
install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
install -m644 ./menu_data/%name.desktop %buildroot%_desktopdir/
convert -size 16x16 ./menu_data/aqemu_64x64.png %buildroot%_miconsdir/%name.png
convert -size 32x32 ./menu_data/aqemu_64x64.png %buildroot%_niconsdir/%name.png
convert -size 48x48 ./menu_data/aqemu_64x64.png %buildroot%_liconsdir/%name.png
rm -rf %buildroot%_datadir/doc/%name

%files
%doc README* AUTHORS* CHANGELOG* TODO*
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%_man1dir/%{name}*
%_pixmapsdir/*.png

%changelog
* Sat Oct 22 2016 L.A. Kostis <lakostis@altlinux.ru> 0.9.2-alt0.1
- 0.9.2 release.

* Sat May 28 2016 L.A. Kostis <lakostis@altlinux.ru> 0.9.1-alt0.1
- New version, now with qt5 support.

* Mon Mar 19 2012 Boris Savelev <boris@altlinux.org> 0.8.2-alt1
- new version (0.8.2) with rpmgs script

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1.qa1
- NMU: dropped obsolete menu entry

* Mon Jul 12 2010 Boris Savelev <boris@altlinux.org> 0.8-alt1
- new version (0.8) (Closes: #23758)
- build from upstream git

* Wed Sep 30 2009 Boris Savelev <boris@altlinux.org> 0.7.3-alt1
- new version (0.7.3)

* Sat Jun 27 2009 Boris Savelev <boris@altlinux.org> 0.7.2-alt1
- new version (0.7.2)

* Fri Apr 10 2009 Boris Savelev <boris@altlinux.org> 0.7.1-alt1
- new version (0.7.1)

* Wed Mar 04 2009 Boris Savelev <boris@altlinux.org> 0.7-alt1
- new version (0.7)

* Fri Jan 30 2009 Boris Savelev <boris@altlinux.org> 0.6.1-alt1
- new version (0.6.1)

* Wed Dec 17 2008 Boris Savelev <boris@altlinux.org> 0.6-alt1
- new version

* Thu Nov 13 2008 Boris Savelev <boris@altlinux.org> 0.5.2-alt2
- clean desktop and menu files (fix #17666)

* Fri Oct 17 2008 Boris Savelev <boris@altlinux.org> 0.5.2-alt1
- New Manage QEMU Binary Window
- Minor Interface Rebuilding.
- More Bug Fix

* Thu Sep 18 2008 Boris Savelev <boris@altlinux.org> 0.5.1-alt1
- New Network Option "Hostname".
- New OS Logos Icons (From Qemulator).
- Minor Interface Rebuilding.
- Major Bug Fix.
- Change package group.

* Wed Sep 03 2008 Boris Savelev <boris@altlinux.org> 0.5-alt1
- initial build
