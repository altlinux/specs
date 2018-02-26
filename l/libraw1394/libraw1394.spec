%def_disable static
%define abiversion 11

Name: libraw1394
Version: 2.0.9
Release: alt1

Summary: FireWire interface library

License: GPL/LGPL
Group: System/Libraries
Url: http://ieee1394.wiki.kernel.org

Source: %name-%version.tar.bz2
Patch: libraw1394-0.10.0-alt-makefile.patch
Patch1: libraw1394-0.10.0-alt-doc.patch

%if_enabled static
BuildPreReq: glibc-devel-static
%endif

# manually removed: gcc-g77 libg2c-devel
# Automatically added by buildreq on Mon Jul 06 2009
BuildRequires: docbook-utils w3c-markup-validator-libs

%description
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

The reason for making a library the interface to the kernel is to avoid
a program dependancy on the kernel version, which would hinder development and
optimization of raw1394.  If development changed the protocol and made it
incompatible with previous versions only the libraw1394 has to be upgraded to
match the kernel version (instead of all applications).

%package -n %name-%abiversion
Summary: FireWire interface library
Group: System/Libraries

%description -n %name-%abiversion
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

The reason for making a library the interface to the kernel is to avoid
a program dependancy on the kernel version, which would hinder development and
optimization of raw1394.  If development changed the protocol and made it
incompatible with previous versions only the libraw1394 has to be upgraded to
match the kernel version (instead of all applications).

%package tools
Summary: Development and include files for libraw1394
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

%package devel
Summary: Development and include files for libraw1394
Group: Development/C
Requires: %name-%abiversion = %version-%release

%description devel
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This package contains the header files for libraw1394 development

%package devel-static
Summary: Development components for libraw1394
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This package contains the static libraries.

%prep
%setup

%build
%configure \
    %{subst_enable static}

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build
make -C doc htmldoc || echo "Fix me if possible"

%install
%makeinstall_std

mv doc/%name doc/html

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files -n %name-%abiversion
%_libdir/*.so.*
%doc README NEWS AUTHORS

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*
%doc doc/html

%files tools
%_bindir/*
%_man1dir/*
%_man5dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 2.0.9-alt1
- Autobuild version bump to 2.0.9

* Tue Mar 06 2012 Fr. Br. George <george@altlinux.ru> 2.0.8-alt1
- Autobuild version bump to 2.0.8

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt2.1
- Removed bad RPATH

* Sun Oct 30 2011 Michael Shigorin <mike@altlinux.org> 2.0.5-alt2
- NMU: updated Url: too

* Sun Oct 30 2011 Michael Shigorin <mike@altlinux.org> 2.0.5-alt1
- NMU: 2.0.5

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.1
- new version 1.2.1 (with rpmrb script)

* Fri Dec 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt0.1
- new version

* Fri Aug 26 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt0.1
- new version

* Sat Jan 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.10.0-alt1
- new version.
- tools subpackage.

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt3
- do not package .la files.

* Wed Nov 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt2
- %%url changed.
- rebuild

* Sat May 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.0-alt1
- Adopted for Sisyphus.

* Mon Jun 04 2001 Harald Welte <laforge@gnumonks.org>
- redhat 7 compile...

* Mon Jun 04 2001 Harald Welte <laforge@conectiva.com>
+ libraw1394=0.9.0-1cl
- updated to 0.9.0

* Thu Apr 05 2001 Harald Welte <laforge@conectiva.com>
+ libraw1394-0.8.2-1cl
- initial conectiva RPM
- split devel package in devel / devel-static
- updated to 0.8.2

* Fri Jan 05 2001 Harald Welte <laforge@gnumonks.org>
- ported SPECfile to RedHat RPM
- libraw1394 0.8.1

* Mon Sep 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.6-2mdk
- clean spec

* Mon Jul 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-1mdk
- initial spec
