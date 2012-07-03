Name: appres
Version: 1.0.3
Release: alt2

Summary: list X application resource database
License: MIT/X11
Group: System/X11
# git
Source: %name-%version.tar.bz2

Url: http://cgit.freedesktop.org/xorg/app/appres

# Automatically added by buildreq on Tue May 18 2010
BuildRequires: libXt-devel xorg-util-macros

%description
The appres program prints the resources seen by an application (or
subhierarchy of an application) with the specified class and instance
names.  It can be used to determine which resources a particular
program will load.

%prep
%setup -q

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt2
- fix build

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- New version

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- XOrg7 initial build

