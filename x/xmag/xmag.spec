Name: xmag
Version: 1.0.4
Release: alt2

Summary: magnify parts of the screen
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libXaw-devel libX11-devel pkg-config xorg-proto-devel xorg-util-macros

%description
The xmag program allows you to magnify portions of an X screen. If no
explicit region is specified, a square with the pointer in the upper
left corner is displayed indicating the area to be enlarged. The area
can be dragged out to the desired size by pressing Button 2. Once
a region has been selected, a window is popped up showing a blown up
version of the region in which each pixel in the source image is
represented by a small square of the same color. Pressing Button1 in the
enlargement window shows the position and RGB value of the pixel under
the pointer until the button is released. Typing ``Q'' or ``^C'' in the
enlargement window exits the program. information is displayed depending
on which options are selected.

%prep
%setup -q
sed -i 's/(XMAG_LIBS) -lm$/(XMAG_LIBS) -lm -lXmu/' Makefile.am

%build
%autoreconf
%configure

%make_build

%install
%makeinstall appdefaultdir=%buildroot%_x11appconfdir

%files
%_bindir/*
%_man1dir/*
%_sysconfdir/X11/app-defaults/*

%changelog
* Mon May 28 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt2
- DSO list completion

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue Aug 25 2009 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up
- sync with upstream up to aw7 downgrade patch

* Sun Feb 26 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- XOrg7 initial build

