%define _unpackaged_files_terminate_build 1
%define soname 4
%define apiversion 0

Name: getdp
Version: 4.0.0
Release: alt1

Summary: A General Environment for the Treatment of Discrete Problems
License: GPL-2.0-or-later
Group: Sciences/Mathematics

Url: http://getdp.info
#http://getdp.info//src/
Source: %name-%version.tar

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc-fortran
BuildRequires: libopenblas-devel liblapack-devel
BuildRequires: libarpack-ng-devel libgsl-devel
BuildRequires: libsparskit-devel
BuildRequires: libgmsh-devel
BuildRequires: eigen3-compat-devel

%description
GetDP is a free finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions.

%package devel
Summary: Development files for %name
Group: Development/C++
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n lib%name%soname
Group: System/Libraries
Summary: %name library
%description -n lib%name%soname
%name library.

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
                -DBLAS_LAPACK_LIBRARIES="-lopenblas -llapack" \
                -DCMAKE_CXX_FLAGS="-I/usr/include/eigen3-compat" \
                -DENABLE_BUILD_SHARED=ON

%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/getdp
%dir %_docdir/getdp
%_docdir/getdp/*
%_man1dir/getdp.*

%files -n lib%name%soname
%_libdir/lib%name.so.%soname.%apiversion
%_libdir/lib%name.so.%{soname}.%apiversion.*

%files devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Tue Nov 17 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.0.0-alt1
- 3.5.0 -> 4.0.0
- added libgetdp4 subpackage
- added getdp-devel subpackage
- changed license
- changed Url

* Mon Jul 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.5.0-alt3
- Builded with eigen3-compat (thnx ulysses@)

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


