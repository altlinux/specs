Name: xcmsdb
Version: 1.0.4
Release: alt1

Summary: Device Color Characterization utility for X Color Management System
License: MIT/X11
Group: System/X11

Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXau-devel libXdmcp-devel pkg-config xorg-proto-devel
BuildRequires: xorg-util-macros

%description
xcmsdb is used to load, query, or remove Device Color  Characterization
data stored in properties on the root window of the screen as specified
in section 7, Device Color  Characterization,  of  the  ICCCM.   Device
Color  Characterization  data  (also  called  the Device Profile) is an
integral part of Xlib's X Color Management System (Xcms), necessary for
proper conversion of color specification between device-independent and
device-dependent  forms.   Xcms  uses  3x3  matrices  stored   in   the
XDCCC_LINEAR_RGB_MATRICES  property  to  convert  color  specifications
between CIEXYZ and RGB Intensity (XcmsRGBi, also referred to as  linear
RGB).    Xcms  then  uses  display  gamma  information  stored  in  the
XDCCC_LINEAR_RGB_CORRECTION property to  convert  color  specifications
between  RGBi and RGB device (XcmsRGB, also referred to as device RGB).

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
* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1.1
- Automatic buildreqfix
- Autobuild watchfile added

* Wed Dec 28 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

