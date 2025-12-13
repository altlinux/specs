Name: xwud
Version: 1.0.7
Release: alt1

Summary: image displayer for X
License: X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.gz

BuildRequires: libX11-devel pkg-config xorg-proto-devel xorg-util-macros

%description
Xwud  is  an  X  Window  System image undumping utility.  Xwud allows X
users to display in a window an image saved in  a  specially  formatted
dump file, such as produced by xwd(1).

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
* Sat Dec 13 2025 Fr. Br. George <george@altlinux.org> 1.0.7-alt1
- Autobuild version bump to 1.0.7

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Wed Jan 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

