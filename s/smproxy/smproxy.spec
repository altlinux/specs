Name: smproxy
Version: 1.0.5
Release: alt1

Summary: Session Manager Proxy
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libICE-devel libSM-devel libX11-devel libXau-devel libXdmcp-devel
BuildRequires: libXext-devel libXmu-devel libXt-devel pkg-config xorg-proto-devel
BuildRequires: xorg-util-macros

%description
smproxy allows X applications that do not support X11R6 session management
to participate in an X11R6 session.

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
* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Mon Apr 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

