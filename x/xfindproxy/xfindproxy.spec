Name: xfindproxy
Version: 1.0.2
Release: alt2

Summary: locate proxy services
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
Patch:	xfindproxy-alt-lvalue.patch


BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel libXdmcp-devel
BuildRequires: libXt-devel pkg-config xorg-proto-devel xorg-util-macros

%description
xfindproxy is a program used to locate available  proxy  services.   It
utilizes the Proxy Management Protocol to communicate with a proxy man-
ager.  The proxy manager keeps track of all available  proxy  services,
starts  new  proxies  when  necessary,  and makes sure that proxies are
shared whenever possible.

%prep
%setup
%patch

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
* Tue Feb 14 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Fix new GCC lvalue always true error

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

