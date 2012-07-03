%def_disable static
%define oname libraw1394
Name: libraw1394-8
Version: 1.2.1
Release: alt1.qa1

Summary: FireWire interface library

License: GPL/LGPL
Group: System/Libraries
Url: http://www.linux1394.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.linux1394.org/dl/%oname-%version.tar.bz2
Patch: libraw1394-0.10.0-alt-makefile.patch
Patch1: libraw1394-0.10.0-alt-doc.patch

%if_enabled static
BuildPreReq: glibc-devel-static
%endif

Provides: libraw1394 = %version
Obsoletes: libraw1394

# manually removed: gcc-g77 libg2c-devel 
# Automatically added by buildreq on Fri Aug 26 2005
BuildRequires: OpenSP docbook-dtds docbook-style-dsssl docbook-utils gcc-c++ libstdc++-devel openjade sgml-common xml-common

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

%package devel
Summary: Development and include files for libraw1394
Group: Development/C
Requires: %name = %version-%release
Conflicts: %oname-devel

%description devel
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can
directly send to and receive from other nodes without requiring a kernel driver
for the protocol in question.

This package contains the header files for libraw1394 development

%prep
%setup -q -n %oname-%version
%__subst "s|@libdir@|\$(libdir)|" Makefile.am
#%patch -p1
#%patch1 -p1

%build
%__rm -f missing
%__libtoolize --copy --force
%__aclocal
touch ChangeLog
%__automake -a -c -f
%__autoconf

%configure \
    %{subst_enable static}

%make_build

%install
%makeinstall

%files
%_libdir/*.so.*
%doc README NEWS AUTHORS

%files devel
%_includedir/%oname/
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- rename to libraw1394-8 (compat package)

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
