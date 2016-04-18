Name: xinput
Version: 1.6.2
Release: alt1
Summary: utility to configure and test XInput devices
License: MIT/X11
Group: System/X11
Url: https://cgit.freedesktop.org/xorg/app/xinput

Source: %name-%version.tar.gz

BuildRequires(pre): xorg-util-macros

# Automatically added by buildreq on Mon Apr 18 2016
# optimized out: libX11-devel libXext-devel libXfixes-devel libXrender-devel perl pkg-config python-base python-modules xorg-fixesproto-devel xorg-inputproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXi-devel libXinerama-devel libXrandr-devel

%description
xinput - utility to configure and test XInput devices

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
* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.6.2-alt1
- Autobuild version bump to 1.6.2

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.5.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Fri Jun 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Mon Mar 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.99.3-alt1
- 1.4.99.3

* Thu May 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- initial release
