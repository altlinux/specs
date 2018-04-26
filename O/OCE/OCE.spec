%set_verify_elf_method unresolved=relaxed
%global ver_major 0
%global ver_minor 18

Name:    OCE
Version: 0.18.3
Release: alt1
Summary: OpenCASCADE Community Edition

Group:   System/Libraries
License: LGPLv2 with exception
URL:     https://github.com/tpaviot/oce
Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source1: DRAWEXE.1
Source2: opencascade-draw.desktop
Source3: oce-256.png
Source4: oce-128.png
Source5: oce-64.png
Source6: oce-48.png

BuildRequires(pre): cmake 
BuildRequires: gcc-c++
BuildRequires: xorg-proto-devel
BuildRequires: libXxf86misc-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXrandr-devel
BuildRequires: libXpm-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXinerama-devel
BuildRequires: libXres-devel
BuildRequires: libXtst-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXv-devel
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libXmu-devel
BuildRequires: ftgl-devel
BuildRequires: libfreeimage-devel
BuildRequires: libgl2ps-devel
BuildRequires: libgomp
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: tbb-devel
BuildRequires: desktop-file-utils
BuildRequires: ctest

%description
OpenCASCADE Community Edition (OCE) is a suite for 3D surface and solid
modeling, visualization, data exchange and rapid application development. It
is an excellent platform for development of numerical simulation software
including CAD/CAM/CAE, AEC and GIS, as well as PDM applications.

%package foundation
Summary: OpenCASCADE CAE platform shared libraries
Group: System/Libraries

%description foundation
OpenCASCADE CAE platform shared libraries.
This package contains foundation classes which provide a variety of
general-purpose services such as automated management of heap memory,
exception handling, classes for manipulating aggregates of data, basic
math tools.

%package modeling
Summary: OpenCASCADE CAE platform shared libraries
Group:   System/Libraries

%description modeling
OpenCASCADE CAE platform shared libraries

This package supplies data structures to represent 2D and 3D geometric models,
as well as topological and geometrical algorithms.

%package ocaf
Summary: OpenCASCADE CAE platform shared libraries
Group:   System/Libraries

%description ocaf
OpenCASCADE CAE platform shared libraries.
This package provides OpenCASCADE Application Framework services and
support for data exchange.

%package visualization
Summary: OpenCASCADE CAE platform shared libraries
Group:   System/Libraries

%description visualization
OpenCASCADE CAE platform shared libraries.
This package provides services for displaying 2D and 3D graphics.

%package examples
Summary: OpenCASCADE CAE platform shared libraries
Group:   System/Libraries

%description examples
OpenCASCADE CAE platform shared libraries.
This package contains example input files for OpenCASCADE in various formats.

%package draw
Summary: OpenCASCADE CAE platform shared libraries
Group:   System/Libraries

%description draw
OpenCASCADE CAE DRAW test harness.


%package devel
Summary: OpenCASCADE CAE platform library development files
Group:   Development/C++
Requires: %name-draw = %EVR
Requires: %name-foundation = %EVR
Requires: %name-modeling = %EVR
Requires: %name-ocaf = %EVR
Requires: %name-visualization = %EVR
Requires: libfreeimage-devel
Requires: libfreetype-devel
Requires: libgl2ps-devel
Requires: libICE-devel
Requires: libSM-devel
Requires: libX11-devel
Requires: libXext-devel
Requires: libXxf86misc-devel
Requires: libXScrnSaver-devel
Requires: libXrandr-devel
Requires: libXpm-devel
Requires: libxkbfile-devel
Requires: libXinerama-devel
Requires: libXres-devel
Requires: libXtst-devel
Requires: libXcomposite-devel
Requires: libXcursor-devel
Requires: libXdmcp-devel
Requires: libXi-devel
Requires: libXv-devel
Requires: libGL-devel
Requires: libGLU-devel
Requires: tbb-devel
Requires: tcl-devel
Requires: tk-devel

%description devel
OpenCASCADE CAE platform library development files.

%prep
%setup -n OCE-%version

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DOCE_INSTALL_PREFIX=%_prefix \
       -DOCE_INSTALL_LIB_DIR=%_lib \
       -DOCE_WITH_FREEIMAGE=ON \
       -DOCE_WITH_GL2PS=ON \
       -DOCE_MULTITHREAD_LIBRARY:STRING=TBB \
       -DCMAKE_SKIP_RPATH=FALSE \
       -DOCE_DRAW=ON \
       -DOCE_TESTING=ON 
%cmake_build

%install
%cmakeinstall_std

# Install manpage for DRAWEXE
install -Dm 0644 %SOURCE1 %buildroot%_man1dir/DRAWEXE.1

# Install and validate desktop file
desktop-file-install \
    --dir=%buildroot%_desktopdir \
    %SOURCE2

# Install icons
for size in 256 128 64 48; do
    icon=%{_sourcedir}/oce-${size}.png
    install -Dm 0644 $icon \
 %buildroot%_iconsdir/hicolor/${size}x${size}/apps/oce.png
done

mkdir -p %buildroot%_datadir/doc/%name-devel-%version
cp -a examples %buildroot%_datadir/doc/%name-devel-%version

%check
export CTEST_OUTPUT_ON_FAILURE=1
%cmake_build test

%files foundation
%doc AUTHORS.md NEWS.md README.md LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt
%_libdir/libTKernel.so.*
%_libdir/libTKMath.so.*
%_datadir/oce-%ver_major.%ver_minor/

%files modeling
# Modeling Data
%_libdir/libTKG2d.so.*
%_libdir/libTKG3d.so.*
%_libdir/libTKGeomBase.so.*
%_libdir/libTKBRep.so.*
# Modeling Algorithms
%_libdir/libTKGeomAlgo.so.*
%_libdir/libTKTopAlgo.so.*
%_libdir/libTKPrim.so.*
%_libdir/libTKBO.so.*
%_libdir/libTKHLR.so.*
%_libdir/libTKMesh.so.*
%_libdir/libTKShHealing.so.*
%_libdir/libTKXMesh.so.*
%_libdir/libTKBool.so.*
%_libdir/libTKFillet.so.*
%_libdir/libTKFeat.so.*
%_libdir/libTKOffset.so.*
# Data exchange
%_libdir/libTKSTL.so.*
%_libdir/libTKXSBase.so.*
%_libdir/libTKSTEPBase.so.*
%_libdir/libTKIGES.so.*
%_libdir/libTKSTEPAttr.so.*
%_libdir/libTKSTEP209.so.*
%_libdir/libTKSTEP.so.*
%_libdir/libTKVRML.so.*
%_libdir/libTKXCAF.so.*
%_libdir/libTKXCAFSchema.so.*
%_libdir/libTKXmlXCAF.so.*
%_libdir/libTKBinXCAF.so.*
%_libdir/libTKXDEIGES.so.*
%_libdir/libTKXDESTEP.so.*

%files visualization
# Visualization Dependents
%_libdir/libTKService.so.*
%_libdir/libTKV3d.so.*
# Visualization
%_libdir/libTKOpenGl.so.*
%_libdir/libTKMeshVS.so.*
%_libdir/libTKNIS.so.*
%_libdir/libTKVoxel.so.*

%files ocaf
# Application framework
%_libdir/libTKCDF.so.*
%_libdir/libPTKernel.so.*
%_libdir/libTKLCAF.so.*
%_libdir/libFWOSPlugin.so.*
%_libdir/libTKPShape.so.*
%_libdir/libTKBinL.so.*
%_libdir/libTKXmlL.so.*
%_libdir/libTKPLCAF.so.*
%_libdir/libTKTObj.so.*
%_libdir/libTKShapeSchema.so.*
%_libdir/libTKStdLSchema.so.*
%_libdir/libTKCAF.so.*
%_libdir/libTKBin.so.*
%_libdir/libTKXml.so.*
%_libdir/libTKPCAF.so.*
%_libdir/libTKBinTObj.so.*
%_libdir/libTKXmlTObj.so.*
%_libdir/libTKStdSchema.so.*

%files draw
%dir %_libdir/oce-%ver_major.%ver_minor
%_libdir/oce-%ver_major.%ver_minor/libTKDraw.so.*
%_libdir/oce-%ver_major.%ver_minor/libTKTopTest.so.*
%_libdir/oce-%ver_major.%ver_minor/libTKViewerTest.so.*
%_libdir/oce-%ver_major.%ver_minor/libTKXSDRAW.so.*
%_libdir/oce-%ver_major.%ver_minor/libTKDCAF.so.*
%_libdir/oce-%ver_major.%ver_minor/libTKXDEDRAW.so.*
%_libdir/oce-%ver_major.%ver_minor/libTKTObjDRAW.so.*
# DRAWEXE application
%_bindir/DRAWEXE
%_man1dir/DRAWEXE.1*
%_desktopdir/opencascade-draw.desktop
%_iconsdir/hicolor/*/apps/*

%files devel
%doc examples
%_includedir/*
%_libdir/*.so
%_libdir/oce-%ver_major.%ver_minor/*.so
%_libdir/oce-%ver_major.%ver_minor/*.cmake

%changelog
* Thu Apr 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.18.3-alt1
- Initial build in Sisyphus (based on Fedora package).

