Name: appres
Version: 1.0.7
Release: alt1

Summary: list X application resource database
License: X11
Group: System/X11
# git
Source: %name-%version.tar.gz

Url: http://cgit.freedesktop.org/xorg/app/appres

# Automatically added by buildreq on Sun Dec 14 2025
# optimized out: libX11-devel libgpg-error ninja-build openssl-config pkg-config python3 python3-base sh5 xorg-proto-devel xz
BuildRequires: libXt-devel meson

%description
The appres program prints the resources seen by an application (or
subhierarchy of an application) with the specified class and instance
names.  It can be used to determine which resources a particular
program will load.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/*
%_man1dir/*

%changelog
* Sun Dec 14 2025 Fr. Br. George <george@altlinux.org> 1.0.7-alt1
- Autobuild version bump to 1.0.7

* Wed Sep 19 2018 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt2
- fix build

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- New version

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- XOrg7 initial build

