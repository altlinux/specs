Name: getdp
Version: 3.3.0
Release: alt1
Summary: A General Environment for the Treatment of Discrete Problems
License: GPLv2
Group: Sciences/Mathematics
Url: https://getdp.info/

Source: %name-%version.tar
Patch1: getdp-3.3.0-missing-cstring.patch

# libblas/liblapack note: these libraries can be found in the following packages:
# - libatlas -- only on i586 and x86_64
# - libopenblas -- can't link: undefined reference to symbol 'dgesv_' in lapack
# - liblapack -- lapack only
# Use blas from libopenblas and lapack from liblapack (see cmake options).
# Use libsparskit instead of libpetsc.

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc-fortran
BuildRequires: libopenblas-devel liblapack-devel
BuildRequires: libarpack-ng-devel libgsl-devel
BuildRequires: libsparskit-devel

%description
GetDP is a free finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions.

%prep
%setup
%patch1 -p2

%build
%cmake_insource -DCMAKE_BUILD_TYPE=Release\
                -DENABLE_PETSC=0 -DENABLE_SPARSKIT=1\
                -DBLAS_LAPACK_LIBRARIES="-llapack -lopenblas"

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/getdp
%dir %_docdir/getdp
%_docdir/getdp/*
%_man1dir/getdp.*

%changelog
* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt1
- v.3.3.0, first build for Altlinux


