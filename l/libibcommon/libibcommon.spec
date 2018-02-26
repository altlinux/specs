Summary: OpenFabrics Alliance InfiniBand management common library
Name: libibcommon
Version: 1.2.0
Release: alt2

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

License: GPL/BSD

Group: System/Libraries

Source: http://www.openfabrics.org/downloads/%{name}-%{version}.tar
Url: http://openfabrics.org/

# Automatically added by buildreq on Tue Aug 21 2007
BuildRequires: gcc-c++ glibc-devel-static

%description
libibcommon provides common utility functions for the IB diagnostic and
management tools.

%package devel
Summary: Development files for the libibcommon library
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for the libibcommon library.

%package devel-static
Summary: Static development files for the libibcommon library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static development files for the libibcommon library.

%prep
%setup

%build
%configure
sed -i -e '1a\echo=echo' libtool
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%dir %_includedir/infiniband
%_includedir/infiniband/*.h

%files devel-static
%_libdir/*.a

%changelog
* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Rebuilt for debuginfo

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Fri Jun 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Made this package as owner of %_includedir/infiniband

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Thu Apr 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2
- Add static package

* Fri Sep 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.8-alt0.M41.1
- build for 4.1

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.8-alt1
- OFED 1.3.1

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.4-alt1
- Initial release
