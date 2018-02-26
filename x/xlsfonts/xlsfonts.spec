Name: xlsfonts
Version: 1.0.4
Release: alt1

Summary: server font list displayer for X
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXau-devel libXdmcp-devel pkg-config xorg-proto-devel
BuildRequires: xorg-util-macros

%description
xlsfonts lists the fonts that match the given  pattern.   The  wildcard
character  "*" may be used to match any sequence of characters (includ-
ing none), and "?" to match any single character.   If  no  pattern  is
given, "*" is assumed.

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
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Fri Feb 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

