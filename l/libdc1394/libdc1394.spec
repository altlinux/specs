%define abiversion 22
Name: libdc1394
Version: 2.1.3
Release: alt1.2

Summary: Library for 1394 Digital Camera Specification

License: LGPL v2.1
Group: System/Libraries
Url: http://sf.net/projects/libdc1394/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2

Patch1: libdc1394-13b85d2d23548682b617ddc1196f5560a27998bd.patch
Patch2: libdc1394-2.1.3-alt-v4l.patch

%define libraw1394_ver 2.0.4
Requires: libraw1394 >= %libraw1394_ver
BuildPreReq: libraw1394-devel >= %libraw1394_ver
BuildPreReq: libv4l-devel

# Automatically added by buildreq on Mon Jul 06 2009
BuildRequires: doxygen gcc-c++ imake libSM-devel libX11-devel libXext-devel libXv-devel libraw1394-devel libusb-devel

%description
libdc1394 is a library that is intended to provide a high level
programming interface for application developers who wish to control
IEEE 1394 based cameras that conform to the 1394-based Digital Camera
Specification (found at http://www.1394ta.org/).

%package -n %name-%abiversion
Summary: Library for 1394 Digital Camera Specification
Group: System/Libraries

%description -n %name-%abiversion
libdc1394 is a library that is intended to provide a high level
programming interface for application developers who wish to control
IEEE 1394 based cameras that conform to the 1394-based Digital Camera
Specification (found at http://www.1394ta.org/).

%package devel
Summary: Development components for libdc1394
Group: Development/C
Requires: %name-%abiversion = %version-%release
Requires: libraw1394-devel >= %libraw1394_ver

%description devel
This package contains the header-files for libdc1394 development.

%package tools
Summary: Development and include files for %name
Group: System/Kernel and hardware
Requires: %name-%abiversion = %version-%release

%description tools
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This package provides tools to dump, send, format IEEE 1394
isochronous channel packets and test %name basic functionality.

%prep
%setup

%patch1 -p2
%patch2 -p2

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n %name-%abiversion
%doc AUTHORS ChangeLog NEWS README
%_libdir/lib*.so.*

%files devel
%_includedir/dc1394/
%_libdir/*.so
%_pkgconfigdir/*

%files tools
%_bindir/dc1394_vloopback
%_bindir/dc1394_reset_bus
%_man1dir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1.2
- Fixed build

* Sun Feb 12 2012 Sergey Y. Afonin <asy@altlinux.ru> 2.1.3-alt1.1
- NMU: fix usb_init function name conflict (ALT #26893)

* Sun Oct 30 2011 Michael Shigorin <mike@altlinux.org> 2.1.3-alt1
- NMU: 2.1.3 (bugfixes)

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.qa2
- Rebuilt for debuginfo

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Sat Dec 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- replace CLK_TCK with sysconf(_SC_CLK_TCK)
- add require libraw1394-devel to devel package

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.1
- new version 1.2.1

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- replace xorg-x11-devel-static with xorg-x11-devel in build requires
- make libs no executable

* Fri Dec 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1.1
- rebuild with libraw1394 1.2.0, add requires for it

* Fri Aug 26 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version, rebuild with libraw1394-1.1.0

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt0.1
- first build for ALT Linux Sisyphus (spec from PLD team)
