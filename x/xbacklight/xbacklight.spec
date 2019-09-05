Name: xbacklight
Version: 1.2.3
Release: alt1
Summary: adjust backlight brightness using RandR extension
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar.gz

# Automatically added by buildreq on Wed Sep 19 2018
# optimized out: glibc-kernheaders-generic libxcb-devel perl pkg-config python-base sh3
BuildRequires: libxcbutil-devel

BuildRequires: libXrandr-devel libXrender-devel xorg-util-macros

%description
Xbacklight is used to adjust the backlight brightness where  supported.
It  finds  all  outputs on the X server supporting backlight brightness
control and changes them all in the same way.

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
* Thu Sep 05 2019 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Autobuild version bump to 1.2.3

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Autobuild version bump to 1.2.2

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Sep 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- initial release
