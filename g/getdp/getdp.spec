Name: getdp
Version: 3.5.0
Release: alt2

Summary: A General Environment for the Treatment of Discrete Problems
License: GPLv2
Group: Sciences/Mathematics

Url: https://getdp.info
Source: %name-%version.tar

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
%ifarch %e2k
# libgfortran is not linked against libquadmath as of lcc 1.26.16;
# looks like that's not uncommon on x86 either
sed -i 's,-lgfortran,& -lquadmath,' CMakeLists.txt
%endif

%build
# - For linking with gmsh it should be build with private API enabled.
# - In Altlinux autodetection does not work correctly for
#   libopenblas + liblapack, BLAS_LAPACK_LIBRARIES should be set.
%cmake_insource -DENABLE_PETSC=0 -DENABLE_SPARSKIT=1 \
                -DENABLE_GMSH=1 \
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
* Mon Apr 17 2023 Michael Shigorin <mike@altlinux.org> 3.5.0-alt2
- E2K: fix build with lcc 1.26.16
- minor spec cleanup

* Sun Jul 17 2022 Vladislav Zavjalov <slazav@altlinux.org> 3.5.0-alt1
- v.3.5.0

* Thu Dec 10 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt4
- add patch: fix Rank mismatch error in contrib/Sparskit/inout.f (for gcc-10)

* Sun Sep 20 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt3
- revert to libopenblas + liblapack, remove ExclusiveArch

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt2
- build with gmsh support
- use libatlas instead of libopenblas + liblapack
- ExclusiveArch: i586 x86_64 (as in libatlas and gmsh)

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.3.0-alt1
- v.3.3.0, first build for Altlinux


