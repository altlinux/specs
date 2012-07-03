Name: xwininfo
Version: 1.1.2
Release: alt1

Summary: window information utility for X
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
# Automatically added by buildreq on Tue Dec 09 2008
BuildRequires: libX11-devel libXext-devel

BuildRequires: pkg-config xorg-util-macros

%description
Xwininfo is a utility for displaying information about windows. Various
information is displayed depending on which options are selected.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Sat Oct 02 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Wed Sep 22 2010 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Version up
- Implement upstream syncing scheme

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- XOrg7 initial build

