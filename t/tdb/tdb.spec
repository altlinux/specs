Name: tdb
Version: 1.2.9
Release: alt1.1

Summary: A trivial database system
License: GPL
Group: Databases
Url: http://tdb.samba.org/

Source: http://samba.org/ftp/tdb/%name-%version.tar.gz
Patch1: 0001-Install-python-bindings-in-the-arch-specific-locatio.patch

BuildRequires: docbook-dtds docbook-style-xsl xsltproc python-devel

%description
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

This is the primary library.

%package utils
Summary: a trivial database system utils
Group: Databases
Requires: lib%name = %version-%release

%description utils
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

This package contains some utils for managing tdb databases

%package -n lib%name
Summary: a trivial database system
Group: System/Libraries

%description -n lib%name
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

This is the primary library.

%package -n lib%name-devel
Summary: a trivial database system development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This is a simple database API. It was inspired by the realisation that
in Samba we have several ad-hoc bits of code that essentially
implement small databases for sharing structures between parts of
Samba. As I was about to add another I realised that a generic
database module was called for to replace all the ad-hoc bits.

I based the interface on gdbm. I couldn't use gdbm as we need to be
able to have multiple writers to the databases at one time.

(I == tridge@samba.org)

These are the development files.

%package -n python-module-%name
Group: Development/Python
Summary: Python bindings for the Tdb library
Requires: lib%name = %version-%release

%description -n python-module-%name
Python bindings for libtdb



%prep
%setup
%patch1 -p1

%build
%undefine _configure_gettext
./autogen.sh
%configure --disable-rpath
%make_build

%install
%make_install DESTDIR=%buildroot install

rm -f %buildroot%_libdir/libtdb.a


%files utils
%_bindir/*
%_man8dir/*

%files -n lib%name
%_libdir/libtdb.so.*
%doc docs/README

%files -n lib%name-devel
%_libdir/libtdb.so
%_includedir/tdb.h
%_pkgconfigdir/tdb.pc

#files -n lib%name-devel-static
#%_libdir/*.a

%files -n python-module-%name
%python_sitelibdir/tdb.so

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9-alt1.1
- Rebuild with Python-2.7

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1.2.9-alt1
- 1.2.9
- Add python bindings in new python-module-tdb subpackage

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Sat Nov 05 2005 Nick S. Grechukh <gns@altlinux.org> 1.0.6-alt3
- initial build for Sisyphus

* Mon Dec 10 2001 Ben Woodard <ben@zork.net>
- Bumped up the version number
- changed email addrs.

* Thu May 23 2001 Jonathon D Nelson <jnelson@securepipe.com>
- Created redhat packages.

