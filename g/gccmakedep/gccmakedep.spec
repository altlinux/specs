Name: gccmakedep
Version: 1.0.2
Release: alt1

Summary: create dependencies in makefiles using 'gcc -M'
License: MIT/X11
Group: Development/C

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: pkg-config xorg-proto-devel xorg-util-macros

%description
The gccmakedep program calls 'gcc -M' to output makefile rules describ-
ing  the  dependencies  of each sourcefile, so that make(1) knows which
object files must be recompiled when a dependency has changed.

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
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

