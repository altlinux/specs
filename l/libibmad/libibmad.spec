Name: libibmad
Version: 1.3.6
Release: alt2

Summary: OpenIB InfiniBand Management and Diagnostic Tools
License: GPL/BSD
Group: System/Legacy libraries

Url: http://openib.org/
Source: http://openib.org/downloads/%name-%version.tar
Patch: libibmad-alt-makefile.patch
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildRequires(pre): rpm-build-compat
BuildPreReq: libibumad-devel-static >= 1.3.6
Requires: libibumad >= 1.3.6

# Automatically added by buildreq on Thu Aug 23 2007
BuildRequires: gcc-c++ glibc-devel-static libibumad-devel

%description
libibmad provides low layer IB functions for use by the IB diagnostic
and management programs. These include MAD, SA, SMP, and other basic
IB functions.

%package devel
Summary: Development files for the libibmad library
Group: Development/C
Requires: %name = %version-%release libibumad-devel

%description devel
Development files for the libibmad library.

%package devel-static
Summary: Static development files for the libibmad library
Group: Development/C
Requires: %name-devel = %version-%release libibumad-devel-static

%description devel-static
Static development files for the libibmad library.

%prep
%setup -n %name-%version
%patch -p1

%build
%configure
sed -i -e '1a\echo=echo' libtool
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/infiniband/*

%files devel-static
%_libdir/*.a

%changelog
* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt2
- Rebuilt for debuginfo

* Wed Dec 15 2010 Timur Aitov <timonbl4@altlinux.org> 1.3.6-alt1
- New version

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 1.3.5-alt1.qa1
- FTBFS (fix macro name)

* Wed Sep 01 2010 Andriy Stepanov <stanv@altlinux.ru> 1.3.5-alt1
- New version.

* Fri Oct 16 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.3_20090314-alt1
- update to OFED-1.4.2

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3_20081118-alt2
- Moved this version into group System/Legacy libraries

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3_20081118-alt1
- Version 1.2.3_20081118

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.1.6-alt1
- OFED 1.3.1

* Thu Aug 23 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.6-alt1
- Initial build

