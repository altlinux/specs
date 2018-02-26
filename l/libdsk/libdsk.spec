# vim: set ft=spec: -*- spec -*-
# $Id: libdsk,v 1.2 2003/12/14 22:19:38 raorn Exp $

%def_disable static

Name: libdsk
Version: 1.2.1
Release: alt2.qa1

Summary: General floppy and diskimage access library
Group: System/Libraries
License: LGPL
Url: http://www.seasip.demon.co.uk/Unix/LibDsk/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.seasip.demon.co.uk/Unix/LibDsk/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Sep 29 2003
BuildRequires: bzlib-devel zlib-devel
%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
LibDsk is a library intended to give transparent access to floppy
drives and to the "disc image files" used by emulators to represent
floppy drives.

%package devel
Summary: Header files for developing apps which will use %name
Group: Development/C
Requires: %name = %version-%release

%description devel
LibDsk is a library intended to give transparent access to floppy
drives and to the "disc image files" used by emulators to represent
floppy drives.

The %name-devel package contains the include files needed to develop
programs that use the %name library.

%if_enabled static
%package devel-static
Summary: Static library for developing apps which will use %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
LibDsk is a library intended to give transparent access to floppy
drives and to the "disc image files" used by emulators to represent
floppy drives.

The %name-devel-static package contains the static library needed to
develop statically linked programs that use the %name library.
%endif

%package utils
Summary: LibDsk utilites
Group: File tools
Requires: %name = %version-%release

%description utils
LibDsk is a library intended to give transparent access to floppy
drives and to the "disc image files" used by emulators to represent
floppy drives.

The %name-utils package contains various utilites for mnipulating
floppies or disk image files for emulated machines.

%prep
%setup -q

%build
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
	%{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%doc README TODO
%_libdir/*.so.*
%_man5dir/*

%files devel
%doc doc/libdsk.* doc/cfi.html
%_includedir/%name.h
%_libdir/%name.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- cleanup spec

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14 (with rpmrb script)

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- restored from orphaned
- fix Source Url, add packager, remove COPYING, INSTALL

* Mon Dec 15 2003 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt2
- devel-static and *.la fixes

* Mon Sep 29 2003 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt1
- Built for Sisyphus

