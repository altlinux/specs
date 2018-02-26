Name: xrefresh
Version: 1.0.4
Release: alt1

Summary: refresh all or part of an X screen
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXau-devel libXdmcp-devel pkg-config xorg-proto-devel
BuildRequires: xorg-util-macros

%description
Xrefresh  is  a simple X program that causes all or part of your screen
to be repainted.  This is useful when system messages  have  messed  up
your  screen.  Xrefresh maps a window on top of the desired area of the
screen and then immediately unmaps it, causing  refresh  events  to  be
sent  to  all applications.  By default, a window with no background is
used, causing all applications to repaint ``smoothly.''   However,  the
various options can be used to indicate that a solid background (of any
color) or the root window background should be used instead.

%prep
%setup

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Mon Apr 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Mar 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- CVS shaphot 2006-03-09

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

