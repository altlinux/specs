Name: xdrfile
Version: 1.1.1
Release: alt2
Summary: Reading and writing trr and xtc files
License: LGPL v3
Group: Development/Tools
Url: http://wiki.gromacs.org/index.php/XTC_Library
Source: ftp://ftp.gromacs.org/pub/contrib/xdrfile-1.1.1.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: lib%name = %version-%release

BuildPreReq: gcc-fortran chrpath

%description
This tool allows to read GROMACS trr and xtc files and also to
convert from one format to another.

%package -n lib%name
Summary: XTC shared library
Group: System/Libraries

%description -n lib%name
This library allows to read GROMACS trr and xtc files and also to
convert from one format to another.

%package -n lib%name-devel
Summary: Development files of XTC library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This library allows to read GROMACS trr and xtc files and also to
convert from one format to another.

This package contains development files of XTC library.

%package -n lib%name-devel-static
Summary: XTC static library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This library allows to read GROMACS trr and xtc files and also to
convert from one format to another.

This package contains static version of XTC library.

%prep
%setup

%build
%configure --enable-fortran --enable-shared
%make_build
%make test

%install
%makeinstall_std

chrpath -d %buildroot%_bindir/trr2xtc

%files
%doc AUTHORS COPYING NEWS README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Removed RPATH

* Fri Nov 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Rebuilt for debuginfo

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Rebuilt without rpm-build-compat

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

