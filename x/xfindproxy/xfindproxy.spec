Name: xfindproxy
Version: 1.0.3
Release: alt1

Summary: locate proxy services
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Mon Mar 11 2013
# optimized out: libICE-devel libX11-devel pkg-config xorg-xproto-devel
BuildRequires: libXt-devel xorg-pmproto-devel

BuildRequires: xorg-util-macros

%description
xfindproxy is a program used to locate available  proxy  services.   It
utilizes the Proxy Management Protocol to communicate with a proxy man-
ager.  The proxy manager keeps track of all available  proxy  services,
starts  new  proxies  when  necessary,  and makes sure that proxies are
shared whenever possible.

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
* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3
- Drop inactual patch

* Mon Mar 11 2013 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- Rebuild with new buildreq

* Tue Feb 14 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Fix new GCC lvalue always true error

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

