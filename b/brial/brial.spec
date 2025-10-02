%define soname 3

%def_disable python

Name: brial
Version: 1.2.15
Release: alt1
Summary: Framework for Boolean Rings
# The entire source code is GPLv2+ except the Cudd directory that is BSD
License: GPL-2.0+ and BSD-3-Clause
Group: Sciences/Mathematics
Url: https://github.com/BRiAl/BRiAl/
VCS: https://github.com/BRiAl/BRiAl

# Source-url: %url/releases/download/%version/%name-%version.tar.bz2
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch3500: brial-boost-loongarch64.patch

# cudd/cudd.h:#define CUDD_VERSION "2.5.0"
Provides: bundled(cudd) = 2.5.0

BuildRequires: gcc-c++
BuildRequires: boost-program_options-devel
BuildRequires: libgd-devel
BuildRequires: libm4ri-devel
%if_enabled python
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%endif

%description
The core of BRiAl is a C++ library, which provides high-level data
types for Boolean polynomials and monomials, exponent vectors, as well
as for the underlying polynomial rings and subsets of the powerset of
the Boolean variables. As a unique approach, binary decision diagrams
are used as internal storage type for polynomial structures. On top of
this C++-library we provide a Python interface. This allows parsing of
complex polynomial systems, as well as sophisticated and extendable
strategies for Grobner base computation. BRiAL features a powerful
reference implementation for Grobner basis computation.

%package -n lib%name%soname
Summary: %summary
Group: System/Libraries

%description -n lib%name%soname
The core of BRiAl is a C++ library, which provides high-level data
types for Boolean polynomials and monomials, exponent vectors, as well
as for the underlying polynomial rings and subsets of the powerset of
the Boolean variables. As a unique approach, binary decision diagrams
are used as internal storage type for polynomial structures. On top of
this C++-library we provide a Python interface. This allows parsing of
complex polynomial systems, as well as sophisticated and extendable
strategies for Grobner base computation. BRiAL features a powerful
reference implementation for Grobner basis computation.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
Development headers and libraries for %name.

%if_enabled python
%package -n python3-module-%name
Summary: Python 3 interface to %name
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
Python 3 interface to %name.
%endif

%prep
%setup
%patch0 -p1
%patch3500 -p1

%build
export CPPFLAGS="-DPBORI_NDEBUG"
%autoreconf
%configure --enable-shared --disable-static
%make_build

%if_enabled python
# Make the python interfaces
pushd sage-brial
%pyproject_build
popd
%endif

%install
%makeinstall_std
rm %buildroot%_libdir/*.la

%if_enabled python
# Install the python interfaces
pushd sage-brial
%pyproject_install
popd
%endif

%check
export LD_LIBRARY_PATH=$PWD/.libs:$PWD/groebner/src/.libs
make check

%files -n lib%name%soname
%doc README
%doc LICENSE
%_libdir/lib%{name}*.so.%{soname}*

%files -n lib%name-devel
%_includedir/polybori.h
%_includedir/polybori/
%_libdir/lib%{name}*.so
%_pkgconfigdir/%name.pc

%if_enabled python
%files -n python3-module-%name
%doc sage-brial/README.md
%python3_sitelibdir_noarch/%{name}*
%endif

%changelog
* Thu Oct 02 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.15-alt1
- New version 1.2.15.

* Thu Jun 19 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.14-alt1
- New version 1.2.14.
- Added VCS tag.

* Thu Nov 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.2.12-alt2
- NMU: fixed FTBFS on LoongArch.

* Mon Jan 16 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.12-alt1
- New version.

* Fri Jul 29 2022 Leontiy Volodin <lvol@altlinux.org> 1.2.11-alt1
- New version.

* Wed Nov 10 2021 Leontiy Volodin <lvol@altlinux.org> 1.2.10-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
