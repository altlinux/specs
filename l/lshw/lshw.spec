Name: lshw
Version: 2.16
Release: alt1
%define real_version B.0%version

Summary: Hardware Lister
License: GPLv2 only
Group: System/Kernel and hardware

URL: http://lshw.org
# .... redirects to http://ezix.org/project/wiki/HardwareLiSter
Source: http://ezix.org/software/files/lshw-%real_version.tar.gz
Source1: lshw.consolehelper
Source2: lshw.pam
Source100: lshw-icons.tar.bz2
Source101: lshw.desktop

Patch1: lshw-2.11-guiname.patch
Patch2: lshw-2.13-gcc43.patch

Requires: pciids usbids

# Automatically added by buildreq on Sun Jan 15 2012
BuildRequires: gcc-c++ libgtk+2-devel libsqlite3-devel

%description
lshw (Hardware Lister) is a small tool to provide detailed informaton on the
hardware configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems, on some PowerPC
machines (PowerMac G4 is known to work) and AMD64.

Information can be output in plain text, XML or HTML.

%package gui
Summary: Graphical hardware lister
Group: System/Kernel and hardware
Requires: pciids usbids
# Probably we should drop this requirements...
Requires: lshw = %version-%release

%description gui
lshw (Hardware Lister) is a small tool to provide detailed informaton on the
hardware configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems, on some PowerPC
machines (PowerMac G4 is known to work) and AMD64.

This package provides graphical (GTK+) front-end to lshw.

%prep
%setup -n lshw-%real_version -a 100
%patch1 -p1
%patch2 -p1

%build
subst 's/-g -Wall -Os/%optflags/' src/core/Makefile src/gui/Makefile src/Makefile
# parallel build seems OK now. let's try...
export SQLITE=1
%make_build all gui

%install
export SQLITE=1
%make_install install install-gui DESTDIR=%buildroot

install -Dp -m644 lshw.png %buildroot%_pixmapsdir/lshw.png
install -Dp -m644 lshw-16x16.png %buildroot%_miconsdir/lshw.png
install -Dp -m644 lshw-32x32.png %buildroot%_niconsdir/lshw.png
install -Dp -m644 lshw-48x48.png %buildroot%_liconsdir/lshw.png
install -Dp -m644 %_sourcedir/lshw.desktop %buildroot%_desktopdir/lshw.desktop

# To run GUI via consolehelper
install -pD -m640 %_sourcedir/lshw.pam %buildroot%_sysconfdir/pam.d/lshw-gui
install -pD -m640 %_sourcedir/lshw.consolehelper %buildroot%_sysconfdir/security/console.apps/lshw-gui
install -d %buildroot%_bindir
ln -s %_bindir/consolehelper %buildroot%_bindir/lshw-gui

%find_lang lshw

%files -f lshw.lang
%_sbindir/lshw
%exclude %_datadir/lshw/*.txt
%exclude %_datadir/lshw/*.ids
%_man1dir/*

%files gui
%_bindir/lshw-gui
%_sbindir/lshw-gui
%_sysconfdir/security/console.apps/*
%_sysconfdir/pam.d/*
%dir %_datadir/lshw
%_datadir/lshw/ui/
%_datadir/lshw/artwork/
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_desktopdir/*

%changelog
* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 2.16-alt1
- 2.16

* Thu Oct 07 2010 Victor Forsiuk <force@altlinux.org> 2.15-alt1
- 2.15
- Build with experimental SQLite support.
- Run lshw-gui via consolehelper.

* Tue Feb 24 2009 Victor Forsyuk <force@altlinux.org> 2.14-alt1
- 2.14

* Wed Nov 05 2008 Victor Forsyuk <force@altlinux.org> 2.13-alt2
- Fix FTBFS with gcc4.3.

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 2.13-alt1
- 2.13

* Wed Oct 10 2007 Victor Forsyuk <force@altlinux.org> 2.12-alt1
- 2.12

* Thu Aug 09 2007 Victor Forsyuk <force@altlinux.org> 2.11.01-alt1
- 2.11.01
- Binaries moved to /usr/bin.
- manuf.txt and oui.txt aren't used at all, so we have no reason to package them.
- We now depend on pciids and usbids packages for pci.ids and usb.ids
  respectively.

* Wed Mar 21 2007 Victor Forsyuk <force@altlinux.org> 2.10-alt1
- 2.10

* Tue Nov 07 2006 Victor Forsyuk <force@altlinux.org> 2.09-alt1
- 2.09
- Rename GUI frontend: lshw-gtk looks more logical than gtk-lshw.
- Move all artwork to gui package.
- Added freedesktop-style menu.

* Wed May 10 2006 Victor Forsyuk <force@altlinux.ru> 2.08.01-alt1
- 2.08.01

* Mon Nov 21 2005 Victor Forsyuk <force@altlinux.ru> 2.06-alt1
- 2.06

* Wed Jul 20 2005 Victor Forsyuk <force@altlinux.ru> 2.05-alt1
- New version.

* Sat Jun 25 2005 Victor Forsyuk <force@altlinux.ru> 2.04-alt1
- Initial build.
