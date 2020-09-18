Name: getdp
Version: 3.3.0
Release: alt2
Summary: A General Environment for the Treatment of Discrete Problems
License: GPLv2
Group: Sciences/Mathematics
Url: https://getdp.info/

Source: %name-%version.tar
Patch1: getdp-3.3.0-missing-cstring.patch

# libatlas (source of blas and lapack) at the moment is built
# only for i586 and x86_64.
# There are problems with building with openblas (another source),
# here and in libgmsh. Here it is possible to use blas from
# libopenblas and lapack from liblapack
# with makefile option -DBLAS_LAPACK_LIBRARIES="-llapack -lopenblas"
# but we want to link with libgmsh too.
# So let's use libatlas:
ExclusiveArch: i586 x86_64

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc-fortran
BuildRequires: libatlas-devel libarpack-ng-devel libgsl-devel
BuildRequires: libsparskit-devel
BuildRequires: libgmsh-devel

%description
GetDP is a free finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions.

%prep
%setup
%patch1 -p2

%build
%cmake_insource -DENABLE_PETSC=0 -DENABLE_SPARSKIT=1\
                -DENABLE_GMSH=1

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/getdp
%dir %_docdir/getdp
%_docdir/getdp/*
%_man1dir/getdp.*

%changelog
* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt2
- build with gmsh support
- use libatlas instead of libopenblas + liblapack
- ExclusiveArch: i586 x86_64 (as in libatlas and gmsh)

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt1
- v.3.3.0, first build for Altlinux


