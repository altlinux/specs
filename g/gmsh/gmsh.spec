%define _unpackaged_files_terminate_build 1
%define soname 4.15

Name: gmsh
Version: 4.15.2
Release: alt2

Summary: 3D finite element mesh generator
License: GPL-2.0-or-later with Gmsh-exception
Group: Sciences/Mathematics
Url: https://gmsh.info
VCS: https://gitlab.onelab.info/gmsh/gmsh.git

Source: %name-%version.tar
Patch1: 0001-include-missing-cstdint.patch
Patch4: 30_delete_gl2ps_from_source.patch

Requires: libgmsh%soname = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: getfemxx
BuildRequires: libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: libann-devel
BuildRequires: libfltk-devel
BuildRequires: libfreeglut-devel
BuildRequires: libfreetype-devel
BuildRequires: libgl2ps-devel
BuildRequires: libglvnd-devel
BuildRequires: libjpeg-devel
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel
BuildRequires: libpng-devel
BuildRequires: opencascade-devel
BuildRequires: zlib-devel
BuildRequires: eigen3-devel

%description
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.


%package -n libgmsh%soname
Summary: Shared library for Gmsh
Group: Sciences/Mathematics
%description -n libgmsh%soname
This package contains libgmsh shared library.


%package -n libgmsh-devel
Summary: Shared library for Gmsh
Group: Sciences/Mathematics
%description -n libgmsh-devel
This package contains development files for libgmsh.


%package -n python3-module-gmsh
Summary: Python interface for libgmsh
Group: Sciences/Mathematics
BuildArch: noarch
%description -n python3-module-gmsh
This package contains python interface for libgmsh.


%package demos
Summary: Tutorial and example files for Gmsh
Group: Sciences/Mathematics
BuildArch: noarch
%description demos
This package contains tutorial and example files for gmsh.

%prep
%setup
%patch1 -p2
%ifarch %e2k
# need to disable workarounds for GCC
sed -i "s/EIGEN_GNUC_AT_LEAST(6,0)/0/" \
  contrib/eigen/Eigen/src/Core/products/GeneralBlockPanelKernel.h
%endif
%patch4 -p1

# cleanup contrib like fedora, but
# mathex not packaged
# WinslowUntangler is introduced in 4.15.0
(
cd contrib;
ls -1 | \
    grep -v ^DiscreteIntegration$ | \
    grep -v ^HighOrderMeshOptimizer$ | \
    grep -v ^MathEx$ | \
    grep -v ^MeshOptimizer$ | \
    grep -v ^QuadTri$ | \
    grep -v ^WinslowUntangler$ | \
    grep -v ^bamg$ | \
    grep -v ^hxt$ | \
    grep -v ^kbipack$ | \
    grep -v ^onelab$ | \
    grep -v ^tinyobjloader$ | \
xargs rm -rf
)

%build
# 1. Dynamic library and private API is needed for compiling getdb
# (ENABLE_PRIVATE_API=YES)
# 2. blossoms is nonfree, see contrib/blossoms/README.txt
%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_SYSTEM_CONTRIB=YES \
	-DENABLE_BUILD_SHARED=YES \
	-DENABLE_BUILD_DYNAMIC=YES \
	-DENABLE_EIGEN=YES \
	-DENABLE_BLAS_LAPACK=YES \
	-DBLAS_LIBRARIES="-lopenblas" \
	-DLAPACK_LIBRARIES="-llapack -lopenblas" \
	-DENABLE_BLOSSOM=NO \
	-DENABLE_PRIVATE_API=YES \
%nil
%cmake_build

%install
%cmake_install

mkdir -p %buildroot%python3_sitelibdir_noarch
mv %buildroot%_libdir/*.py %buildroot%python3_sitelibdir_noarch
mv %buildroot%_bindir/*.py %buildroot%python3_sitelibdir_noarch
mv %buildroot%_libdir/gmsh-%version.dev1.dist-info \
   %buildroot%python3_sitelibdir_noarch/gmsh-%version.dist-info

rm -f %buildroot%_libdir/*.jl

%files
%_bindir/gmsh
%_man1dir/gmsh.*
%dir %_docdir/gmsh
%doc %_docdir/gmsh/*.txt

%files -n libgmsh%soname
%_libdir/libgmsh.so.%soname
%_libdir/libgmsh.so.%version

%files -n libgmsh-devel
%_includedir/*
%_libdir/libgmsh.so
%_datadir/gmsh/gmshConfig.cmake
%_datadir/gmsh/gmshTargets-release.cmake
%_datadir/gmsh/gmshTargets.cmake

%files -n python3-module-gmsh
%python3_sitelibdir_noarch/*

%files demos
%_docdir/gmsh/examples
%_docdir/gmsh/tutorials


%changelog
* Tue Jun 02 2026 Ulysses Apokin <ulysses@altlinux.org> 4.15.2-alt2
- NMU: built with eigen3 for FreeCAD FEM Workbench.

* Wed Apr 29 2026 Anton Farygin <rider@altlinux.org> 4.15.2-alt1
- updated from 4.15.0 to 4.15.2

* Mon Oct 27 2025 Constantin Sunzow <protvin@altlinux.org> 4.15.0-alt1
- Python module bump to 3 version.
- New version.

* Wed Mar 12 2025 Constantin Sunzow <protvin@altlinux.org> 4.13.1-alt1
- New version.

* Sat Jul 15 2023 Vladislav Zavjalov <slazav@altlinux.org> 4.11.1-alt1
- New version
- patch: include missing cstdint (fix for gcc13)

* Wed May 24 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.11.0-alt1.1
- Fixed build for Elbrus

* Mon Dec 12 2022 Vladislav Zavjalov <slazav@altlinux.org> 4.11.0-alt1
- New version

* Sun Aug 21 2022 Vladislav Zavjalov <slazav@altlinux.org> 4.10.5-alt1
- New version

* Mon Mar 21 2022 Andrey Cherepanov <cas@altlinux.org> 4.9.5-alt1
- New version
- Add watch file

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt3.1
- NMU: rebuild with opencascade-devel

* Sun Sep 20 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.6.0-alt3
- use libopenblas + liblapack instead of libatlas, remove ExclusiveArch
- remove Requires: getdp (gmsh can be used without it)

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.6.0-alt2
- Enable libgmsh shared library, private API (for building getdp)
  and python-module-gmsh

* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.6.0-alt1
- Version 4.6.0, return the package to Altlinux.
- Cleanup spec, build in the default upstream configuration.
- No library, no python/julia/c/c++ interfaces.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.8.5-alt2.svn20140707.1
- NMU: added BR: texinfo

* Thu Mar 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt2.svn20140707
- Rebuilt with OpenCASCADE 6.8.0

* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt1.svn20140707
- New snapshot

* Thu Jun 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt1.svn20140618
- Version 2.8.5

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.4-alt1.svn20131112
- Version 2.8.4

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt2.svn20130710
- Rebuilt with OpenCASCADE 6.6.0

* Wed Jul 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt1.svn20130710
- Version 2.8.1

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1.svn20130201
- Version 2.7.2

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt6.svn20130201
- Fixed build

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt5.svn20130201
- Rebuilt with OpenCASCADE 6.5.4

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20130201
- New snapshot

* Wed Oct 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20120814
- Rebuilt with gcc 4.7

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt3.svn20120814
- Rebuilt with libpng15

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt2.svn20120814
- Rebuilt with external ANN, ParMetis, Mmg3d and Netgen
- Built with OpenCASCADE

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.svn20120814
- Version 2.6.2

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt7.svn20100906
- Fixed build

* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt6.svn20100906
- Rebuilt with PETSc 3.2_p7-alt3

* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt5.svn20100906
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt4.svn20100906
- Fixed build

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.svn20100906
- Built without OSMesa

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2.svn20100906
- Rebuilt with PETSc 3.2

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.8
- Rebuilt with cgns 3.1.3

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.7
- Rebuilt with FLTK 1.3.0.r8575

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.6
- Rebuilt

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.5
- Built with GotoBLAS2 instead of ATLAS

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.4
- Rebuilt for debuginfo

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.3
- Added -g into compiler flags

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.2
- Rebuilt with libfltk13

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.1
- Fixed clear() function in Geo/MZoneBoundary.h

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906
- Version 2.5.1

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100620.1
- Enabled MPI parallelization
- Rebuilt with PETSc 3.1

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100620
- Version 2.5.0

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.svn20091216
- Version 2.4.3

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.svn20091109
- Version 2.4.2
- Rebuilt with texlive instead of tetex

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus

