Name: qrupdate
Version: 1.1.2
Release: alt3
Summary: Library for fast updating of QR and Cholesky decompositions
License: GPLv3+
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/qrupdate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-fortran f2c liblapack-devel

%description
qrupdate is a Fortran library for fast updates of QR and Cholesky
decompositions.

%package -n lib%name
Summary: Library for fast updating of QR and Cholesky decompositions
Group: System/Libraries

%description -n lib%name
qrupdate is a Fortran library for fast updates of QR and Cholesky
decompositions.

%package -n lib%name-devel
Summary: Development files of qrupdate
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
qrupdate is a Fortran library for fast updates of QR and Cholesky
decompositions.

This package contains development files of qrupdate.

%prep
%setup
sed -i 's|^\(LIBDIR\).*|\1=%_lib|' Makeconf*

%build
%make_build solib

%install
%makeinstall_std

%files -n lib%name
%doc ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%changelog
* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt3
- Rebuilt with updated openblas

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus

