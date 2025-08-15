%define soname 0

Name: sirocco2
Version: 2.1.1
Release: alt1
Summary: Library for computing homotopy continuation of roots
License: GPL-3.0+
Group: Sciences/Mathematics
Url: https://github.com/miguelmarco/SIROCCO2
VCS: https://github.com/miguelmarco/SIROCCO2

Source: https://github.com/miguelmarco/SIROCCO2/releases/download/%version/libsirocco-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libmpfr-devel

%description
This is a library for computing homotopy continuation of a given root
of one dimensional sections of bivariate complex polynomials.

%package -n lib%name-common
Summary: Common files for %name
Group: System/Libraries
BuildArch: noarch

%description -n lib%name-common
This package provides common files for %name.

%package -n lib%name-%soname
Summary: Library for computing homotopy continuation of roots
Group: System/Libraries

%description -n lib%name-%soname
This is a library for computing homotopy continuation of a given root
of one dimensional sections of bivariate complex polynomials.

%package -n lib%name-devel
Summary: Development files for sirocco, a math library
Group: Development/C++

%description -n lib%name-devel
This is a library for computing homotopy continuation of a given root of one
dimensional sections of bivariate complex polynomials.

The output is a piecewise linear approximation of the path followed
by the root, with the property that there is a tubular neighborhood,
with square transversal section, that contains the actual path, and
there is a three times thicker tubular neighborhood guaranted to
contain no other root of the polynomial. This second property ensures
that the piecewise linear approximation computed from all roots of a
polynomial form a topologically correct deformation of the actual
braid, since the inner tubular neighborhoods cannot intersect.

This subpackage contains the include files and library links for
developing with the sirocco library.

%prep
%setup -n libsirocco-%version
%patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n lib%name-common
%doc LICENSE README.md

%files -n lib%name-%soname
%_libdir/libsirocco.so.%{soname}*

%files -n lib%name-devel
%_includedir/*
%_libdir/libsirocco.so
%_pkgconfigdir/*.pc

%changelog
* Fri Aug 15 2025 Leontiy Volodin <lvol@altlinux.org> 2.1.1-alt1
- New version 2.1.1.
- Added VCS tag.
- Packaged common files separately.

* Fri Nov 26 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
