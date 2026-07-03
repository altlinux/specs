%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%set_verify_elf_method none

Name: elmerfem
Version: 26.2.1
Release: alt3

Summary: Elmer FEM software
License: LGPL-2.0-only
Group: Engineering
Url: https://github.com/ElmerCSC/elmerfem

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: openmpi-devel

BuildRequires: libopenblas-devel
BuildRequires: liblapack-devel
BuildRequires: pkgconfig(UMFPACK)

BuildRequires: libgomp-devel

%ifnarch riscv64
BuildRequires: libhypre-devel
%endif

BuildRequires: pkgconfig(netcdf)
BuildRequires: pkgconfig(netcdf-fortran)
BuildRequires: pkgconfig(hdf5)

BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: libGLU-devel

BuildRequires: opencascade-devel
BuildRequires: libvtk-devel
BuildRequires: pkgconfig(fmt)

BuildRequires: pkgconfig(parmetis)

BuildRequires: mmg-devel

BuildRequires: /usr/bin/magick
BuildRequires: patchelf

# libarpack.so
Conflicts: libarpack-ng-devel

Requires: elmerfem-data = %{version}-%{release}

# needed by /usr/bin/elmerf90
Requires: gcc-fortran
Requires: libgomp-devel

%description
Elmer is computational tool for multi-physics problems. Elmer includes
physical models of fluid dynamics, structural mechanics, electromagnetics,
heat transfer and acoustics, for example. These are described by partial
differential equations which Elmer solves by the Finite Element Method (FEM).

%package data
Summary: Data files for %name
Group: Engineering
BuildArch: noarch

%description data
%summary.

This package provides data files of %name.

%prep
%setup
%patch -p1

%ifarch %ix86
sed -i 's|SET(ElmerIce_SRC ${ElmerIce_SRC} CalvingRemeshMMG.F90 )|MESSAGE(STATUS "Disabling CalvingRemeshMMG.F90 on %ix86 as not buildable.")|' elmerice/Solvers/CMakeLists.txt
%endif

%build
# Following https://github.com/flathub/fi.csc.Elmer/blob/master/fi.csc.Elmer.yaml
# and docker/elmer.def

# dependency problems - no nn-c and csa-c
#       -DWITH_ScatteredDataInterpolator=FALSE
# dependency problems - no ML, no trilinos
#       -DWITH_Trilinos=FALSE
#       -DTrilinos_DIR=%%_libdir/cmake/Trilinos
#       -DML_DIR=%%_libdir/cmake/ML
# dependency problems - no mumps
#       -DWITH_Mumps=FALSE
#       -DMUMPSROOT=/usr
# dependency problems - no paraview
#       -DWITH_PARAVIEW=FALSE

%cmake \
       -Wno-dev \
       -DWITH_MPI=TRUE \
       -DWITH_OpenMP=TRUE \
%ifnarch riscv64
       -DHYPRE_INCLUDE_DIR=%_includedir/hypre \
       -DWITH_Hypre=TRUE \
%endif
       -DWITH_ElmerIce=TRUE \
       -DWITH_QT5=TRUE \
       -DWITH_ELMERGUI=TRUE \
       -DWITH_QWT=FALSE \
       -DCMAKE_OpenGL_GL_PREFERENCE=GLVND \
       -DWITH_OCC=TRUE \
       -DWITH_VTK=TRUE \
       -DOCC_INCLUDE_DIR=%_includedir/opencascade \
       -DWITH_ELMERGUILOGGER=TRUE \
       -DWITH_CONTRIB=TRUE \
       -DWITH_OpenCASCADE=TRUE \
       -DWITH_LUA=TRUE \
       -DWITH_MATC=ON \
       -DWITH_MMG=TRUE \
       -DWITH_GridDataReader=TRUE \
       -DUSE_CONTIGUOUS=TRUE \
       -DParMetis_INCLUDE_DIR=%_includedir/parmetis \
       -DParMetis_LIBRARIES=%_libdir/libparmetis.so \
       -DSCALAPACK_LIBRARIES=%_libdir/libopenblas.so \
       -DLAPACK_LIBRARIES=%_libdir/libopenblas.so \
       -DEXTERNAL_UMFPACK=TRUE \
       -DUMFPACK_LIBRARIES="-L%_libdir/x86_64-linux-gnu/libumfpack.so -lumfpack -lamd -lcholmod -lsuitesparseconfig -lccolamd -lcamd -lbtf" \
       -DUMFPACK_INCLUDE_DIR="%_includedir/suitesparse" \
       -DELMER_SOLVER_HOME=%_datadir/elmersolver \
       -DELMER_INSTALL_LIB_DIR=%_libdir \
       -DELMER_INSTALL_BIN_DIR=%_bindir

%cmake_build

%install
%cmake_install

patchelf %buildroot/usr/share/elmersolver/lib/EliminatePeriodic.so --add-rpath /usr/share/elmersolver/lib
patchelf %buildroot/usr/share/elmersolver/lib/ElmerIceSolvers.so --add-rpath /usr/share/elmersolver/lib
patchelf %buildroot/usr/share/elmersolver/lib/ElmerIceUSF.so --add-rpath /usr/share/elmersolver/lib/

install -D -m644 ElmerGUI/Application/fi.csc.Elmer.desktop %buildroot%_desktopdir/fi.csc.Elmer.desktop

install -D -p -m644 pics/ElmerLogoPlain128x128.png \
        %buildroot%_iconsdir/hicolor/128x128/apps/fi.csc.Elmer.png

for size in 16 24 32 48 64; do
  mkdir -p %buildroot%_iconsdir/hicolor/${size}x${size}/apps ;
  magick pics/ElmerLogoPlain128x128.png -filter Lanczos -resize ${size}x${size} %buildroot%_iconsdir/hicolor/${size}x${size}/apps/fi.csc.Elmer.png ;
done

rm -fv %buildroot/usr/lib/ElmerGUI/ngcore/libng.a

%files
%doc README.adoc
%_bindir/ElmerGUI
%_bindir/ElmerGUIlogger
%_bindir/ElmerGrid
%_bindir/ElmerSolver
%_bindir/ElmerSolver_mpi
%_bindir/Mesh2D
%_bindir/Radiators
%_bindir/ViewFactors
%_bindir/elmerf90
%_bindir/elmerld
%_bindir/matc
%_desktopdir/fi.csc.Elmer.desktop
%_iconsdir/hicolor/*/apps/fi.csc.Elmer.png

%_libdir/libarpack.so
%_libdir/libelmersolver.so
%_libdir/libfhuti.so
%_libdir/libmatc.so
%_libdir/libparpack.so

%dir %_datadir/elmersolver/lib
%_datadir/elmersolver/lib/*

%post
echo "NOTE: at the present time %name can use only ElmerVTK for"
echo "      post-processing, user have to select it manually by"
echo "      the longpress on P button on the toolbar and/or use"
echo "      Run -> Start ElmerVTK menu option to view results."

%files data
%dir %_datadir/ElmerGUI
%_datadir/ElmerGUI/*
%dir %_datadir/elmersolver/include
%_datadir/elmersolver/include/*
%dir %_datadir/elmersolver/lua-scripts
%dir %_datadir/elmersolver/license_texts
%_datadir/elmersolver/license_texts/*
%_datadir/elmersolver/lua-scripts/defaults.lua

%changelog
* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 26.2.1-alt3
- Build without libqwt6-qt5-devel (closes: #59717).

* Mon Jun 22 2026 Nikolay Strelkov <snk@altlinux.org> 26.2.1-alt2
- Enable build on i586 and riscv64.
- Added post-install message about using ElmerVTK as default instead of non-compilable ElmerPost.

* Sat Jun 20 2026 Nikolay Strelkov <snk@altlinux.org> 26.2.1-alt1
- Initial build for Sisyphus
