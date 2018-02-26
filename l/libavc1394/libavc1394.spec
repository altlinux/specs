Name: libavc1394
Version: 0.5.4
Release: alt1

Summary: A library to control AV firewire devices

License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/libavc1394/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%name/%name-%version.tar.gz

%define libraw1394_ver 1.1.0
Requires: libraw1394 >= %libraw1394_ver
BuildPreReq: libraw1394-devel >= %libraw1394_ver

#BuildPreReq: libtool_1.4

# manually removed: gcc-g77 libg2c-devel 
# Automatically added by buildreq on Fri Aug 26 2005
BuildRequires: gcc-c++ libraw1394-devel libstdc++-devel pkgconfig

%description
libavc1394 is a programming interface for the 1394 Trade
Association AV/C (Audio/Video Control) Digital Interface
Command Set.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
libavc1394 is a programming interface for the 1394 Trade
Association AV/C (Audio/Video Control) Digital Interface
Command Set.

This package contains development files needed to compile applications
using %name.

%package devel-static
Summary: Static version of %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libavc1394 is a programming interface for the 1394 Trade
Association AV/C (Audio/Video Control) Digital Interface
Command Set.

This package contains libraries needed to compile applications
statically linked  with %name.

%package utils
Summary: FireWire interface
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description utils
libavc1394 is a programming interface for the 1394 Trade
Association AV/C (Audio/Video Control) Digital Interface
Command Set.

This package contains utilities from %name package.

%prep
%setup
subst "s|@libdir@|\$(libdir)|" Makefile.am

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
cp test/.libs/romtest %buildroot%_bindir

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files
%_libdir/*.so.*
%doc README NEWS INSTALL AUTHORS ChangeLog

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-static
%_libdir/*.a

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Sun Oct 30 2011 Michael Shigorin <mike@altlinux.org> 0.5.4-alt1
- NMU: 0.5.4
- minor spec cleanup

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Jul 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5.3-alt1
- rebuild with new libraw1394 2.0.4

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.3-alt0.1
- new version 0.5.3 (with rpmrb script)

* Mon Dec 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt2
- use autoreconf

* Fri Aug 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- new version
- fix bug #6696 (license)

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt2
- use libtool-1.4
- do not package .la files.

* Wed Nov 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt1
- First build for Sisyphus.
