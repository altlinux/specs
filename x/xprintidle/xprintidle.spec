# -*- mode: rpm-spec -*-

Summary: Prints User Idle Time to Stdout
Name: xprintidle
Version: 0.2
Release: alt3
Source: %name-%version.tar
Patch: xprintidle-0.2-dso.patch
Url: http://www.dtek.chalmers.se/~henoch/text/xprintidle.html
Group: System/X11

Packager: Evgenii Terechkov <evg@altlinux.ru>
License: GPL2

BuildPreReq: gcc
# Automatically added by buildreq on Thu Apr 08 2010 (-bi)
# optimized out: elfutils glibc-pthread xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: imake libX11-devel libXScrnSaver-devel libXext-devel xorg-cf-files

%description
xprintidle is a small program that prints the user's idle time to stdout,
using the X screensaver extension. It is meant for use in scripts.

%prep
%setup
%patch -p1

%build
%configure --x-libraries=%_libdir
make

%install
%makeinstall

%files
%_bindir/%name
%doc COPYING README AUTHORS ChangeLog NEWS

%changelog
* Mon May 21 2012 Terechkov Evgenii <evg@altlinux.org> 0.2-alt3
- Fix DSO linkage

* Thu Apr  8 2010 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt2
- Buildreqs updated to fix build

* Sat Feb  7 2009 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt1
- 0.2

* Sat Sep 23 2006 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt1
- Build for Sisyphus

* Mon Aug 21 2006 Terechkov Evgenii <evg@altlinux.ru> 0.1-alt0.C30.1
- Initial build for C30

