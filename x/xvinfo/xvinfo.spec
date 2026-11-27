Name: xvinfo
Version: 1.1.6
Release: alt1
Summary: Print out X-Video extension adaptor information
License: X11
Group: System/X11
Url: https://cgit.freedesktop.org/xorg/app/xkbcomp/

Source: %name-%version.tar.gz

BuildRequires: libXv-devel xorg-util-macros

%description
xvinfo  prints  out  the  capabilities of any video adaptors associated
with the display that are accesible through the X-Video extension

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
* Fri Nov 27 2026 Fr. Br. George <george@altlinux.org> 1.1.6-alt1
- Autobuild version bump to 1.1.6

* Thu Apr 18 2024 Fr. Br. George <george@altlinux.org> 1.1.5-alt1
- Autobuild version bump to 1.1.5

* Wed Mar 20 2019 Fr. Br. George <george@altlinux.ru> 1.1.4-alt1
- Autobuild version bump to 1.1.4

* Mon Apr 18 2016 Fr. Br. George <george@altlinux.ru> 1.1.3-alt1
- Autobuild version bump to 1.1.3

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Nov 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

