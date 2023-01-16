%define soname 3

%def_disable python

Name: brial
Version: 1.2.12
Release: alt1
Summary: Framework for Boolean Rings
# The entire source code is GPLv2+ except the Cudd directory that is BSD
License: GPL-2.0+ and BSD-3-Clause
Group: Sciences/Mathematics
Url: https://github.com/BRiAl/BRiAl/

Source: %url/releases/download/%version/%name-%version.tar.bz2
# The clock function has been removed from python 3.8.  See
# https://github.com/BRiAl/BRiAl/commit/74d861705c77c3af7e6a2e49dd57f8d26a664072
Patch: %name-clock.patch
# cudd/cudd.h:#define CUDD_VERSION "2.5.0"
Provides: bundled(cudd) = 2.5.0

BuildRequires: gcc-c++
BuildRequires: boost-program_options-devel
BuildRequires: libgd3-devel
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
%patch -p1

%build
export CPPFLAGS="-DPBORI_NDEBUG"
%autoreconf
%configure --enable-shared --disable-static
# Get rid of undesirable hardcoded rpaths.
# sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
#     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
#     -i libtool

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

%if_enabled python
%files -n python3-module-%name
%doc sage-brial/README.md
%python3_sitelibdir_noarch/%{name}*
%endif

%changelog
* Mon Jan 16 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.12-alt1
- New version.

* Fri Jul 29 2022 Leontiy Volodin <lvol@altlinux.org> 1.2.11-alt1
- New version.

* Wed Nov 10 2021 Leontiy Volodin <lvol@altlinux.org> 1.2.10-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
