Name: wmtimer
Version: 2.92
Release: alt3

Summary: Run command at specified time
License: GPL
Group: Graphical desktop/Window Maker

Source0: wmtimer-%version.tar.gz
Source1: wmtimer.1
Patch: wmtimer-2.92-InitialTimerBeep.patch

# Automatically added by buildreq on Fri Oct 20 2006
BuildRequires: libgtk+2-devel libXext-devel libXpm-devel

%description
Run commands at specified time.  WMTimer can be configured either at run
time via the command line or by using the GTK interface by clicking on the
main part of the window (anywhere except the buttons).

%prep
%setup
sed -i 's,^CFLAGS.*,& -std=gnu89,' wmtimer/Makefile

%build
cd wmtimer
%make_build CC="gcc %optflags"

%install
install -pDm755 wmtimer/wmtimer %buildroot%_bindir/wmtimer
install -pDm644 %_sourcedir/wmtimer.1 %buildroot%_man1dir/wmtimer.1

%files
%doc Changelog CREDITS README
%_bindir/*
%_man1dir/*

%changelog
* Sat Oct 03 2015 Michael Shigorin <mike@altlinux.org> 2.92-alt3
- gcc5 FTBFS workaround (-std=gnu89)
- minor spec cleanup
- dropped Url:

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.92-alt2.qa1
- NMU: rebuilt for debuginfo.

* Fri Oct 20 2006 Victor Forsyuk <force@altlinux.org> 2.92-alt2
- Added man-page from Debian.
- Fix initial timer beep in wmtimer.c when using -c mode (Debian patch).

* Wed Apr 06 2005 Victor Forsyuk <force@altlinux.ru> 2.92-alt1
- New version (ported to GTK2, so update buildreqs).
- Correct package URL.
- Apply %%optflags and build with parallel make.

* Mon Sep 29 2003 Ott Alex <ott@altlinux.ru> 2.9-alt1
- New release

* Mon Apr 28 2003 Ott Alex <ott@altlinux.ru> 2.4-alt1
- Initial build

