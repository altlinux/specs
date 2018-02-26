Name: q4wine
Version: 0.118
Release: alt1
Summary: Q4Wine is an Qt4 GUI for WINE
Group: Emulators
License: GPL
Url: http://sourceforge.net/projects/q4wine/
Packager: Boris Savelev <boris@altlinux.org>
Source: http://download.sourceforge.net/sourceforge/q4wine/%name-%version.tar.bz2

# Automatically added by buildreq on Fri Dec 19 2008
BuildRequires: gcc-c++ libqt4-devel
BuildRequires: libstdc++-devel libtool cmake
BuildRequires: icoutils

Requires: libqt4-sql-sqlite, icoutils, /usr/bin/wine

ExclusiveArch: %ix86

%description
Q4Wine is an Qt4-based GUI for WINE. It will help you to manage wine prefixes and installed applications.

General features:
- Works with different wine versions at same time;
- Creating, deleting and managing prefixes (WINEPREFIX);
- Easy controlling for wine process;
- Easy installer wizard for wine applications; (Not yet. Wait for v. 0.120)
- Autostart icons support;
- Support of ISO images;
- Icons can be extracted from PE files (.exe, .dll);
- and more... ;)

%prep
%setup

%build
%cmake \
    -DWITH_WINETRIKS=ON
%make -C BUILD

%install
%makeinstall_std -C BUILD INSTALL_ROOT=%buildroot

%files
%_bindir/%{name}*
%_libdir/%name
%_datadir/%name
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%_man1dir/%{name}*

%changelog
* Fri Apr 16 2010 Boris Savelev <boris@altlinux.org> 0.118-alt1
- new version

* Sat Jan 23 2010 Boris Savelev <boris@altlinux.org> 0.115-alt1.g0e148f5
- build from upstream git
- guess wine lib path (closes #22384)

* Mon Nov 16 2009 Boris Savelev <boris@altlinux.org> 0.114-alt1
- new version

* Fri Oct 09 2009 Boris Savelev <boris@altlinux.org> 0.113-alt1
- new version

* Sat Sep 05 2009 Boris Savelev <boris@altlinux.org> 0.112-alt1.g8044728
- build from upstream git

* Wed Feb 25 2009 Boris Savelev <boris@altlinux.org> 0.111-alt1
- new version

* Wed Feb 25 2009 Boris Savelev <boris@altlinux.org> 0.110g-alt3
- add libqt4-sql-sqlite to requires (fix #181846)

* Sat Jan 31 2009 Boris Savelev <boris@altlinux.org> 0.110g-alt2
- fix wine requires (problem with wine-vanilla)

* Wed Jan 28 2009 Boris Savelev <boris@altlinux.org> 0.110g-alt1
- new version (0.110g)

* Thu Jan 01 2009 Boris Savelev <boris@altlinux.org> 0.108-alt2
- add icoutils requires

* Fri Dec 19 2008 Boris Savelev <boris@altlinux.org> 0.108-alt1
- initial build for Sisyphus

