Name: xrdb
Version: 1.2.1
Release: alt1

Summary: X server resource database utility
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.org>

%ifarch %e2k
Requires: mcpp
%else
Requires: cpp
%endif

Source: %name-%version.tar.gz

BuildRequires: libXmu-devel xorg-util-macros

%description
Xrdb is used to get or set the contents of the RESOURCE_MANAGER
property on the root window of screen 0, or the SCREEN_RESOURCES
property on the root window of any or all screens, or everything
combined.

You would normally run this program from your X startup file.

%prep
%setup

%build
%autoreconf
%configure \
%ifarch %e2k
	--with-cpp=%_bindir/mcpp
%else
	--with-cpp=%_bindir/cpp
%endif

%make_build

%install
%makeinstall_std

%files
%doc README*
%_bindir/*
%_man1dir/*

%changelog
* Wed Nov 17 2021 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Autobuild version bump to 1.2.1

* Wed Mar 20 2019 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Autobuild version bump to 1.2.0

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Tue Jun 26 2018 Michael Shigorin <mike@altlinux.org> 1.0.9-alt2
- E2K: depend on mcpp to avoid pulling whole lcc in
- minor spec cleanup

* Tue Apr 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Thu Feb 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sun Aug 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Jan 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Wed Apr 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- CVS snapshot 2006-04-03

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

