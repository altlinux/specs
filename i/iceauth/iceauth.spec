Name: iceauth
Version: 1.0.9
Release: alt1
Summary: ICE authority file utility
License: X11
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar.gz

BuildRequires: libICE-devel xorg-util-macros

%description
The  iceauth  program  is  used  to  edit and display the authorization
information used in connecting with ICE.  This program is usually  used
to  extract authorization records from one machine and merge them in on
another (as is the case when using remote logins or granting access  to
other users).  Commands (described below) may be entered interactively,
on the iceauth command line, or in scripts.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc *.md
%_bindir/*
%_man1dir/*

%changelog
* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 1.0.9-alt1
- Autobuild version bump to 1.0.9

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.0.8-alt1
- Autobuild version bump to 1.0.8

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 1.0.7-alt1
- Autobuild version bump to 1.0.7

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sun Oct 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue Jul 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu May 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- fixed iceauth dumps core if signal caught before initialization done

* Wed May 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- added iceauth-1.0.1-coverity924.patch,
	iceauth-1.0.1-coverity1039.patch,
	iceauth-1.0.1-coverity1089.patch

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

