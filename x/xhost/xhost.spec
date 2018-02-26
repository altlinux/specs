Name: xhost
Version: 1.0.5
Release: alt1
Summary: server access control program for X
License: MIT/X11
Group: System/X11
Packager: Valery Inozemtsev <shrek@altlinux.ru>
Url: http://xorg.freedesktop.org

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXau-devel libXmu-devel xorg-util-macros xorg-xtrans-devel

%description
The xhost program is used to add and delete host names or user names to
the list allowed to make connections to the X server.  In the  case  of
hosts,  this  provides  a rudimentary form of privacy control and secu-
rity.  It is only sufficient for a workstation (single  user)  environ-
ment,  although  it  does  limit  the worst abuses.  Environments which
require more sophisticated measures  should  implement  the  user-based
mechanism  or use the hooks in the protocol for passing other authenti-
cation data to the server.

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
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Jul 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Apr 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- fixed #8894

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

