%define sover 0
%def_disable static

Name: xblas
Version: 1.0.248
Release: alt2

Summary: Extended and Mixed Precision version of BLAS
License: MIT
Group: Sciences/Mathematics

Url: http://www.netlib.org/xblas/

# Source-url: http://www.netlib.org/xblas/xblas-%version.tar.gz
Source: %name-%version.tar

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: lib%name = %version-%release
BuildPreReq: gcc-fortran

%description
This library of routines is part of a reference implementation for
the Dense and Banded BLAS routines, along with their
Extended and Mixed Precision versions, as documented in
Chapters 2 and 4 of the new BLAS Standard, which is available from:

%package -n lib%name
Summary: Shared library of Extended and Mixed Precision BLAS
Group: System/Libraries

%description -n lib%name
This library of routines is part of a reference implementation for
the Dense and Banded BLAS routines, along with their
Extended and Mixed Precision versions, as documented in
Chapters 2 and 4 of the new BLAS Standard, which is available from:

This package contains shared library of XBLAS.

%package -n lib%name-devel
Summary: Development files of Extended and Mixed Precision BLAS
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
This library of routines is part of a reference implementation for
the Dense and Banded BLAS routines, along with their
Extended and Mixed Precision versions, as documented in
Chapters 2 and 4 of the new BLAS Standard, which is available from:

This package contains development files of XBLAS.

%package -n lib%name-devel-static
Summary: Static library of Extended and Mixed Precision BLAS
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This library of routines is part of a reference implementation for
the Dense and Banded BLAS routines, along with their
Extended and Mixed Precision versions, as documented in
Chapters 2 and 4 of the new BLAS Standard, which is available from:

This package contains static library of XBLAS.

%package -n lib%name-devel-doc
Summary: Documentation for Extended and Mixed Precision BLAS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
This library of routines is part of a reference implementation for
the Dense and Banded BLAS routines, along with their
Extended and Mixed Precision versions, as documented in
Chapters 2 and 4 of the new BLAS Standard, which is available from:

This package contains development documentation for XBLAS.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static} --enable-fortran --disable-plain-blas
%make_build lib
# non SMP build
%make test-lib


%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_docdir/lib%name-devel

install -pm644 *.a %buildroot%_libdir
install -pm644 src/*.h %buildroot%_includedir
install -pm644 doc/report.ps %buildroot%_docdir/lib%name-devel

# shared library

pushd %buildroot%_libdir
g77 -shared -lm -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-o lib%name.so.%sover -Wl,-soname,lib%name.so.%sover -Wl,-z,defs
ln -s lib%name.so.%sover lib%name.so
popd

%if_disabled static
rm -v %buildroot%_libdir/*.a
%endif

%check
%make tests

%files
%doc README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.248-alt2
- disable devel-static subpackage

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.248-alt1.3
- fix source url
- move test to check section, fix concurrent build issue

* Thu Mar 28 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.248-alt1.2
- fix build

* Tue May 30 2017 Michael Shigorin <mike@altlinux.org> 1.0.248-alt1.1
- E2K: link lib%name.so against libm explicitly
- minor spec cleanup in memoriam

* Fri Nov 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.248-alt1
- Version 1.0.248

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.245-alt4
- Rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.245-alt3
- Added shared library

* Thu Jul 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.245-alt2
- Moved documentation into separate package

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.245-alt1
- Initial build for Sisyphus

