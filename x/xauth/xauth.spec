Name: xauth
Version: 1.0.7
Release: alt1
Epoch: 1
Summary: X authority file utility
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXau-devel libXext-devel libXmu-devel xorg-xtrans-devel xorg-util-macros

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server.  This program is usually
used to extract authorization records from one machine and merge them in
on another (as is the case when using remote logins or granting access to
other users).  Commands (described below) may be entered interactively,
on the xauth command line, or in scripts.  Note that this program does
not contact the X server except when the generate command is used.
Normally xauth is not used to create the authority file entry in the
first place; the program that starts the X server (often xdm or startx)
does that.

%def_enable ipv6

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable ipv6}
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.7-alt1
- 1.0.7

* Sat Dec 03 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.6-alt3
- Updated to 1.0.6-4-gfbc307f.
- Updated build dependencies.
- Dropped /usr/X11R6/bin/xauth symlink.

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.6-alt2
- enabled ipv6

* Tue May 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.6-alt1
- 1.0.6

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.5-alt1
- 1.0.5

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt2
- fixed build dependencies

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt1
- 1.0.3

* Tue Dec 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt2
- fixed obsoletes version

* Thu Dec 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt1
- 1.0.2
- renamed package xorg-x11-%name to %name

* Sat Jan 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt4
- rebuild with new rpm macros

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- fixed #8894

* Sat Jan 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- added symlink to %_x11bindir/xauth for compatibility openssh

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

