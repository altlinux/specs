Name: iceauth
Version: 1.0.4
Release: alt1
Summary: ICE authority file utility
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libICE-devel xorg-util-macros

%description
The  iceauth  program  is  used  to  edit and display the authorization
information used in connecting with ICE.  This program is usually  used
to  extract authorization records from one machine and merge them in on
another (as is the case when using remote logins or granting access  to
other users).  Commands (described below) may be entered interactively,
on the iceauth command line, or in scripts.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
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

