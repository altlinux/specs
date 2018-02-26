Name: listres
Version: 1.0.3
Release: alt1

Summary: list resources in X widgets
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libX11-devel libXaw-devel pkg-config xorg-proto-devel xorg-util-macros

%description
The listres program generates a list of a widget's resource database. The class in which each resource is first defined, the instance and class name, and the type of each resource is listed. If no specific widgets or the -all switch are given, a two-column list of widget names and their class hierarchies is printed.

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
* Wed Mar 21 2012 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1.1
- Recalculate buildreq

* Fri Sep 24 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Fri Nov 21 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Sync with upstream up to aw7 downgrade patch

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- XOrg7 initial build

