%define sover 0
Name: xblas
Version: 1.0.248
Release: alt1
Summary: Extended and Mixed Precision version of BLAS
License: MIT
Group: Sciences/Mathematics
Url: http://www.netlib.org/xblas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.netlib.org/xblas/xblas.tar.gz

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
%configure --enable-fortran --disable-plain-blas
%make_build makefiles
%make_build sources test-sources
%make_build all

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_docdir/lib%name-devel

install -m644 *.a %buildroot%_libdir
install -m644 src/*.h %buildroot%_includedir
install -p -m644 doc/report.ps %buildroot%_docdir/lib%name-devel

# shared library

pushd %buildroot%_libdir
g77 -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive \
	-o lib%name.so.%sover -Wl,-soname,lib%name.so.%sover -Wl,-z,defs
ln -s lib%name.so.%sover lib%name.so
popd

%files
%doc README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
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

