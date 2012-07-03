Name: xkbevd
Version: 1.1.3
Release: alt1

Summary: XKB event daemon
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXau-devel libXdmcp-devel libxkbfile-devel
BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
This  command  is very raw and is therefore only partially implemented;
we present it here as a rough prototype for developers, not as  a  gen-
eral  purpose  tool  for  end  users.  Something like this might make a
suitable replacement for xev;  I'm not signing up, mind you,  but  it's
an interesting idea.

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
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.1.3-alt1
- Autobuild version bump to 1.1.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

