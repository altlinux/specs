Name: listener
Version: 1.7.2
Release: alt1

Summary: listener is a sounds detection program
Group: Sound
License: GPL
Url: http://www.vanheusden.com/%name/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %url/%name-%version.tgz
Patch: %name-1.6.5-alt-makefile.patch

BuildPreReq: kernel-headers-common

# Automatically added by buildreq on Fri Mar 12 2004
BuildRequires: libncurses-devel libsndfile-devel libtinfo-devel

%description
This program listens for sound. If it detects any, it starts recording
automatically and also automatically stops when things become silent
again.

%prep
%setup -q
%patch -p1

%build
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%config(noreplace) %_sysconfdir/*
%doc manual.html

%changelog
* Wed Oct 08 2008 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Thu Apr 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.5-alt1
- new version.

* Fri Dec 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Fri Mar 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- new version.

* Fri Dec 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1-alt1
- First build for Sisyphus.


