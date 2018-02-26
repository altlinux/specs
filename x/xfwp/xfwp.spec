Name: xfwp
Version: 1.0.2
Release: alt3

Summary: X firewall proxy
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
Patch: xfwp-1.0.2-gcc4.6.patch

BuildRequires: libICE-devel libX11-devel libXau-devel libXdmcp-devel pkg-config
BuildRequires: xorg-proto-devel xorg-util-macros xorg-xtrans-devel

%description
The  X firewall proxy (xfwp) is an application layer gateway proxy that
may be run on a network firewall host to forward X traffic  across  the
firewall.  Used in conjunction with the X server Security extension and
authorization checking, xfwp constitutes a safe, simple,  and  reliable
mechanism  both  to  hide  the  addresses  of  X servers located on the
Intranet and to enforce a server connection policy.  Xfwp  cannot  pro-
tect  against mischief originating on the Intranet; however, when prop-
erly configured it can guarantee that only trusted clients  originating
on authorized external Internet hosts will be allowed inbound access to
local X servers.

%prep
%setup
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
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- Fix gcc4.6 build

* Tue Apr 10 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Fix build

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2.1
- Automatic buildreqfix
- Autobuild watchfile added

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed #8894

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

