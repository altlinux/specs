Name:    libarpack-ng
Version: 3.9.0
Release: alt1
Summary: Fortran 77 subroutines for solving large scale eigenvalue problems

License: BSD
Group:   Sciences/Mathematics
URL:     http://forge.scilab.org/index.php/p/arpack-ng/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: arpack-ng-%version.tar

BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: libopenblas-devel
BuildRequires: liblapack-devel
BuildRequires: eigen3

Provides:  arpack = %version-%release

%global optflags_lto %optflags_lto -ffat-lto-objects

%description
ARPACK is a collection of Fortran 77 subroutines designed to solve large
scale eigenvalue problems.

The package is designed to compute a few eigenvalues and corresponding
eigenvectors of a general n by n matrix A. It is most appropriate for
large sparse or structured matrices A where structured means that a
matrix-vector product w <- Av requires order n rather than the usual
order n**2 floating point operations. This software is based upon an
algorithmic variant of the Arnoldi process called the Implicitly
Restarted Arnoldi Method (IRAM).

%package devel
Summary: Files needed for developing arpack based applications
Group:   System/Libraries

%description devel
ARPACK is a collection of Fortran 77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.

%package doc
Summary: Examples for the use of arpack
Group: Documentation
BuildArch: noarch

%description doc
This package contains examples for the use of arpack-ng.

%package devel-static
Summary: Static library for developing arpack based applications
Group: System/Libraries

%description devel-static
ARPACK is a collection of Fortran 77 subroutines designed to solve
large scale eigenvalue problems. This package contains the static
library and so links used for building arpack based applications.

%prep
%setup -q -n arpack-ng-%version

%build
%autoreconf
%configure --enable-shared \
           --enable-static \
           --with-blas="-L%{_libdir}/atlas -lf77blas -latlas" \
           --with-lapack="-L%{_libdir}/atlas -llapack -latlas"
%make_build

%install
%makeinstall_std

# Get rid of .la files
rm -rf %buildroot%_libdir/*.la

%files
%doc CHANGES COPYING
%_libdir/libarpack.so.*

%files devel
%doc DOCUMENTS EXAMPLES
%_libdir/libarpack.so
%_pkgconfigdir/*.pc

%files doc
%doc EXAMPLES/ DOCUMENTS/

%files devel-static
%_libdir/libarpack.a

%changelog
* Sat Feb 11 2023 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Mon Sep 20 2021 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt2
- FTBFS: fix build with LTO.

* Mon Dec 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Mon Sep 21 2020 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt2
- Rebuild with openblas + lapack (ALT #38975).

* Sun Jan 13 2019 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.3-alt1
- New version.
- Build with libatlas only for i586 and x86_64.

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.2-alt1
- New version.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.1-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version.

* Wed May 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- new version 3.4.0

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Mon Apr 29 2013 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build in Sisyphus from Fedora (ALT #28909)

