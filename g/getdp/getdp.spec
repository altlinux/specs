Name: getdp
Version: 3.3.0
Release: alt3
Summary: A General Environment for the Treatment of Discrete Problems
License: GPLv2
Group: Sciences/Mathematics
Url: https://getdp.info/

Source: %name-%version.tar
Patch1: getdp-3.3.0-missing-cstring.patch

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc-fortran
BuildRequires: libopenblas-devel liblapack-devel
BuildRequires: libarpack-ng-devel libgsl-devel
BuildRequires: libsparskit-devel
BuildRequires: libgmsh-devel

%description
GetDP is a free finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions.

%prep
%setup
%patch1 -p2

%build
# - For linking with gmsh it should be build with private API enabled.
# - In Altlinux autodetection does not work correctly for
#   libopenblas + liblapack, BLAS_LAPACK_LIBRARIES should be set.
%cmake_insource -DENABLE_PETSC=0 -DENABLE_SPARSKIT=1\
                -DENABLE_GMSH=1\
                -DBLAS_LAPACK_LIBRARIES="-lopenblas -llapack"

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/getdp
%dir %_docdir/getdp
%_docdir/getdp/*
%_man1dir/getdp.*

%changelog
* Sun Sep 20 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt3
- revert to libopenblas + liblapack, remove ExclusiveArch

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt2
- build with gmsh support
- use libatlas instead of libopenblas + liblapack
- ExclusiveArch: i586 x86_64 (as in libatlas and gmsh)

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt1
- v.3.3.0, first build for Altlinux


