Name: csrch
Version: 1996
Release: alt4
Summary: MINPACK-2 implementation of the More and Thuente linesearch
License: BSD/non-commertial using only
Group: Sciences/Mathematics
Url: ftp://ftp.mcs.anl.gov/pub/MINPACK-2/csrch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.mcs.anl.gov/pub/MINPACK-2/csrch/csrch.tar.gz
Source1: ftp://ftp.mcs.anl.gov/pub/MINPACK-2/csrch/README

Requires: lib%name = %version-%release
BuildPreReq: gcc-fortran

%description
CSRCH is the MINPACK-2 implementation of the More and Thuente
linesearch. A variant is included in the NLPy bundle, which may be
sufficient for most purposes.

%package -n lib%name
Summary: Shared library of CSRCH
Group: System/Libraries

%description -n lib%name
CSRCH is the MINPACK-2 implementation of the More and Thuente
linesearch. A variant is included in the NLPy bundle, which may be
sufficient for most purposes.

This package contains shared library of CSRCH.

%package -n lib%name-devel
Summary: Development files of CSRCH
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
CSRCH is the MINPACK-2 implementation of the More and Thuente
linesearch. A variant is included in the NLPy bundle, which may be
sufficient for most purposes.

This package contains development files of CSRCH.

%package -n lib%name-devel-static
Summary: Static library of CSRCH
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
CSRCH is the MINPACK-2 implementation of the More and Thuente
linesearch. A variant is included in the NLPy bundle, which may be
sufficient for most purposes.

This package contains static library of CSRCH.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
%make_build install
%make_build %name

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir

install -m755 %name %buildroot%_bindir
cp -P source/lib%name.* %buildroot%_libdir/

%files
%doc README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc source/*.f
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1996-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1996-alt3
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1996-alt2
- Rebuilt for soname set-versions

* Mon Sep 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1996-alt1
- Initial build for Sisyphus

