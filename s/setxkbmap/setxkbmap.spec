Name: setxkbmap
Version: 1.3.3
Release: alt1
Summary: set the keyboard using the X Keyboard Extension
License: MIT/X11
Group: System/X11
Url: https://cgit.freedesktop.org/xorg/app/setxkbmap/

Source: %name-%version.tar.gz

# Automatically added by buildreq on Tue Jun 21 2022
# optimized out: glibc-kernheaders-generic libX11-devel libXrender-devel libgpg-error perl pkg-config python3-base sh4 xorg-proto-devel
BuildRequires: libXrandr-devel libxkbfile-devel python3

BuildRequires: xorg-util-macros

%description
The setxkbmap command maps the keyboard to use the layout determined by
the options specified on the command line.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README*
%_bindir/*
%_man1dir/*

%changelog
* Tue Jun 21 2022 Fr. Br. George <george@altlinux.org> 1.3.3-alt1
- Autobuild version bump to 1.3.3

* Thu Sep 05 2019 Fr. Br. George <george@altlinux.ru> 1.3.2-alt1
- Autobuild version bump to 1.3.2

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Jul 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Jul 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Nov 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Mar 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

