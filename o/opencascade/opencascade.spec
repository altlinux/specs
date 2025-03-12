%define _unpackaged_files_terminate_build 1
%define soname 7.9

Name: opencascade
Version: 7.9.0
Release: alt1

Summary: SDK for development applications dealing with 3D CAD data
License: LGPL-2.1-only-with-OCCT-exception-1.0
Group: Development/Tools
Url: http://www.opencascade.org
VCS: https://git.dev.opencascade.org/repos/occt.git

# Upstream requires a login to download sources. 
# https://dev.opencascade.org/release
# VCS: https://git.dev.opencascade.org/repos/occt.git
Source: %name-%version.tar
Patch1: opencascade-cmake.patch
Patch2: opencascade-alt-arm-build.patch
Patch2000: opencascade-e2k-disable-fenv.patch

Requires: libopencascade%soname = %EVR
Requires: opencascade-data = %EVR

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-macros-vtk
BuildRequires: doxygen
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: java-devel-default
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libcoin3d-devel
BuildRequires: libfltk-devel
BuildRequires: libfreeimage-devel
BuildRequires: libfreetype-devel
BuildRequires: libftgl-devel
BuildRequires: libgl2ps-devel
BuildRequires: libvtk-devel
BuildRequires: tcl-devel
BuildRequires: tcl-tix
BuildRequires: tk-devel
BuildRequires: zlib-devel

%description
Open CASCADE Technology (OCCT) is a suite for 3D surface and solid
modeling, visualization, data exchange and rapid application development. It
is an excellent platform for development of numerical simulation software
including CAD/CAM/CAE, AEC and GIS, as well as PDM applications.

%package -n libopencascade%soname
Summary: Shared libraries of Open CASCADE
Group: System/Libraries

%description -n libopencascade%soname
Shared libraries of Open CASCADE, development platform for 3D modeling and
numerical simulation applications.

%package devel
Summary: Development files for Open CASCADE Technology
Group: Development/C++
Requires: libopencascade%soname = %EVR
Provides: OCE-devel = %EVR
Obsoletes: OCE-devel < %EVR

%description devel
Development files for Open CASCADE Technology, development platform for 3D
modeling and numerical simulation applications.

%package data
Summary: Data for Open CASCADE
Group: Development/Tools
BuildArch: noarch

%description data
This package contains data and resources for Open CASCADE.

%package samples
Summary: Samples for Open CASCADE
Group: Development/Documentation
BuildArch: noarch

%description samples
This package contains samples for Open CASCADE.

%package doc
Summary: Documentation for Open CASCADE
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains documentation for Open CASCADE.

%prep
%setup
%patch1 -p1
%ifarch %arm
%patch2 -p2
%endif
%ifarch %e2k
%patch2000 -p1
%endif

%build
# opencascade does some manual install trickery that does not respect DESTDIR.
# Make DESTDIR and environment variable that can be passed into the CMake config.
export DESTDIR="%buildroot"
%cmake_insource -GNinja \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_TBB=False \
       -DUSE_VTK=True \
       -DINSTALL_DIR_DOC=%_datadir/doc/opencascade \
       -D3RDPARTY_VTK_INCLUDE_DIR=%_includedir/vtk-%vtk_version \
       -DINSTALL_DIR_LIB=%_lib \
       -DINSTALL_DIR_CMAKE=%_lib/cmake/opencascade
%ninja_build

%install
%ninja_install
mv %buildroot%_bindir/DRAWEXE-* %buildroot%_bindir/DRAWEXE

# Remove installed files with licenses
rm -f /usr/share/doc/opencascade/*

%files
%_bindir/DRAWEXE
%_bindir/ExpToCasExe
%_bindir/ExpToCasExe-%version

%files -n libopencascade%soname
%_libdir/*.so.%soname
%_libdir/*.so.%version

%files devel
%_bindir/*.sh
%_libdir/*.so
%_includedir/*
%_libdir/cmake/opencascade

%files data
%_datadir/opencascade
%exclude %_datadir/opencascade/samples

%files samples
%_datadir/opencascade/samples

%files doc
%_datadir/doc/opencascade

%changelog
* Wed Mar 12 2025 Constantin Sunzow <protvin@altlinux.org> 7.9.0-alt1
- Update summary.
- New version.

* Fri Feb 14 2025 Constantin Sunzow <protvin@altlinux.org> 7.7.2-alt3
- Rebuild with vtk 9.4.

* Thu Jan 23 2025 Ivan A. Melnikov <iv@altlinux.org> 7.7.2-alt2.1
- NMU: Backport upstream fix for FTBFS.

* Mon Jan 29 2024 Anton Farygin <rider@altlinux.ru> 7.7.2-alt2
- built with  vtk 9.3

* Sat Jul 22 2023 Andrey Cherepanov <cas@altlinux.org> 7.7.2-alt1
- New version.

* Tue Mar 21 2023 Andrey Cherepanov <cas@altlinux.org> 7.7.1-alt1
- New version.

* Tue Nov 08 2022 Andrey Cherepanov <cas@altlinux.org> 7.7.0-alt1
- New version.

* Thu Jul 28 2022 Andrey Cherepanov <cas@altlinux.org> 7.6.3-alt1
- New version.

* Sun May 01 2022 Andrey Cherepanov <cas@altlinux.org> 7.6.2-alt1
- New version (ALT #42460).

* Fri Feb 04 2022 Andrey Cherepanov <cas@altlinux.org> 7.6.1-alt1
- New version.

* Mon Jan 24 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 7.5.3-alt3
- Rebuilt with VTK-9.1.0.

* Fri Oct 22 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 7.5.3-alt2
- e2k: disabled use of "feclearexcept" (freecad crashes with SIGILL)

* Mon Aug 16 2021 Andrey Cherepanov <cas@altlinux.org> 7.5.3-alt1
- New version.
- Build from upstream tag.

* Wed May 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.5.0-alt2
- Rebuilt with VTK-9.0.1.

* Mon Nov 30 2020 Andrey Cherepanov <cas@altlinux.org> 7.5.0-alt1
- New version.

* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 7.4.0-alt1
- New version.
- Build all data and documentation packages from one source package.
- Obsoletes OCE package.

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.8.0-alt2
- Fixed build with new glibc.

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.8.0-alt1.qa1
- Rebuilt against Tcl/Tk 8.6

* Fri Mar 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.8.0-alt1
- Version 6.8.0

* Wed May 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.7.1-alt1
- Version 6.7.1

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6.0-alt1
- Version 6.6.0

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.4-alt1
- Version 6.5.4

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.3-alt2
- Fixed build with gcc 4.7

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.3-alt1
- Version 6.5.3

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt3
- Fixed build

* Sun Mar 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt2
- Fixed build with TBB 40_297

* Wed Feb 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt1
- Version 6.5.2

* Thu Sep 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.1-alt1
- Version 6.5.1

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt1
- Version 6.5.0

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt10
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt9
- Rebuilt for soname set-versions

* Sat Oct 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt8
- Fixed underlinking of libraries

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt7
- Fixed for checkbashisms

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt6
- Reduced optimization level: -O2 -> -O1
- Rebuilt with java

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt5
- Set opencascade-commom as noarch

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt4
- Rebuilt without java

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt3
- Changed owner of %_datadir/%name: %name -> %name-common
- Rebuild with gcc4.4

* Wed May 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt2
- Removed %name directory from /usr/lib
- Fixed channel permission

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1
- Initial build for Sisyphus

