%define _unpackaged_files_terminate_build 1
%define soname 7.9

Name: opencascade
Version: 7.9.3
Release: alt2

Summary: SDK for development applications dealing with 3D CAD data
License: LGPL-2.1-only with OCCT-exception-1.0
Group: Development/Tools
Url: http://www.opencascade.org
VCS: https://git.dev.opencascade.org/repos/occt.git

# Upstream requires a login to download sources.
# https://dev.opencascade.org/release
# VCS: https://git.dev.opencascade.org/repos/occt.git
Source: %name-%version.tar
Patch2: opencascade-alt-arm-build.patch
Patch2000: opencascade-e2k-disable-fenv.patch

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
# For FreeCAD
BuildRequires: rapidjson-devel

%description
Open CASCADE Technology (OCCT) is a suite for 3D surface and solid
modeling, visualization, data exchange and rapid application
development. It is an excellent platform for development of numerical
simulation software including CAD/CAM/CAE, AEC and GIS, as well as PDM
applications.

%package -n libTKBin%soname
Summary: Shared library of Open CASCADE: libTKBin
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBin%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKBinL%soname
Summary: Shared library of Open CASCADE: libTKBinL
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBinL%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKBinTObj%soname
Summary: Shared library of Open CASCADE: libTKBinTObj
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBinTObj%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKBinXCAF%soname
Summary: Shared library of Open CASCADE: libTKBinXCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBinXCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKBO%soname
Summary: Shared library of Open CASCADE: libTKBO
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBO%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKBool%soname
Summary: Shared library of Open CASCADE: libTKBool
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBool%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKBRep%soname
Summary: Shared library of Open CASCADE: libTKBRep
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKBRep%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKCAF%soname
Summary: Shared library of Open CASCADE: libTKCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKCDF%soname
Summary: Shared library of Open CASCADE: libTKCDF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKCDF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDCAF%soname
Summary: Shared library of Open CASCADE: libTKDCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDE%soname
Summary: Shared library of Open CASCADE: libTKDE
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDE%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDECascade%soname
Summary: Shared library of Open CASCADE: libTKDECascade
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDECascade%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDEGLTF%soname
Summary: Shared library of Open CASCADE: libTKDEGLTF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDEGLTF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDEIGES%soname
Summary: Shared library of Open CASCADE: libTKDEIGES
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDEIGES%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDEOBJ%soname
Summary: Shared library of Open CASCADE: libTKDEOBJ
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDEOBJ%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDEPLY%soname
Summary: Shared library of Open CASCADE: libTKDEPLY
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDEPLY%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDESTEP%soname
Summary: Shared library of Open CASCADE: libTKDESTEP
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDESTEP%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDESTL%soname
Summary: Shared library of Open CASCADE: libTKDESTL
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDESTL%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDEVRML%soname
Summary: Shared library of Open CASCADE: libTKDEVRML
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDEVRML%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKDraw%soname
Summary: Shared library of Open CASCADE: libTKDraw
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKDraw%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKernel%soname
Summary: Shared library of Open CASCADE: libTKernel
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKernel%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKExpress%soname
Summary: Shared library of Open CASCADE: libTKExpress
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKExpress%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKFeat%soname
Summary: Shared library of Open CASCADE: libTKFeat
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKFeat%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKFillet%soname
Summary: Shared library of Open CASCADE: libTKFillet
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKFillet%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKG2d%soname
Summary: Shared library of Open CASCADE: libTKG2d
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKG2d%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKG3d%soname
Summary: Shared library of Open CASCADE: libTKG3d
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKG3d%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKGeomAlgo%soname
Summary: Shared library of Open CASCADE: libTKGeomAlgo
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKGeomAlgo%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKGeomBase%soname
Summary: Shared library of Open CASCADE: libTKGeomBase
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKGeomBase%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKHLR%soname
Summary: Shared library of Open CASCADE: libTKHLR
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKHLR%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKIVtk%soname
Summary: Shared library of Open CASCADE: libTKIVtk
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKIVtk%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKIVtkDraw%soname
Summary: Shared library of Open CASCADE: libTKIVtkDraw
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKIVtkDraw%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKLCAF%soname
Summary: Shared library of Open CASCADE: libTKLCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKLCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKMath%soname
Summary: Shared library of Open CASCADE: libTKMath
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKMath%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKMesh%soname
Summary: Shared library of Open CASCADE: libTKMesh
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKMesh%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKMeshVS%soname
Summary: Shared library of Open CASCADE: libTKMeshVS
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKMeshVS%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKOffset%soname
Summary: Shared library of Open CASCADE: libTKOffset
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKOffset%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKOpenGl%soname
Summary: Shared library of Open CASCADE: libTKOpenGl
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKOpenGl%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKOpenGlTest%soname
Summary: Shared library of Open CASCADE: libTKOpenGlTest
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKOpenGlTest%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKPrim%soname
Summary: Shared library of Open CASCADE: libTKPrim
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKPrim%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKQADraw%soname
Summary: Shared library of Open CASCADE: libTKQADraw
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKQADraw%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKRWMesh%soname
Summary: Shared library of Open CASCADE: libTKRWMesh
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKRWMesh%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKService%soname
Summary: Shared library of Open CASCADE: libTKService
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKService%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKShHealing%soname
Summary: Shared library of Open CASCADE: libTKShHealing
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKShHealing%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKStd%soname
Summary: Shared library of Open CASCADE: libTKStd
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKStd%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKStdL%soname
Summary: Shared library of Open CASCADE: libTKStdL
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKStdL%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKTObj%soname
Summary: Shared library of Open CASCADE: libTKTObj
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKTObj%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKTObjDRAW%soname
Summary: Shared library of Open CASCADE: libTKTObjDRAW
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKTObjDRAW%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKTopAlgo%soname
Summary: Shared library of Open CASCADE: libTKTopAlgo
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKTopAlgo%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKTopTest%soname
Summary: Shared library of Open CASCADE: libTKTopTest
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKTopTest%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKV3d%soname
Summary: Shared library of Open CASCADE: libTKV3d
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKV3d%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKVCAF%soname
Summary: Shared library of Open CASCADE: libTKVCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKVCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKViewerTest%soname
Summary: Shared library of Open CASCADE: libTKViewerTest
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKViewerTest%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXCAF%soname
Summary: Shared library of Open CASCADE: libTKXCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXDEDRAW%soname
Summary: Shared library of Open CASCADE: libTKXDEDRAW
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXDEDRAW%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXMesh%soname
Summary: Shared library of Open CASCADE: libTKXMesh
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXMesh%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXml%soname
Summary: Shared library of Open CASCADE: libTKXml
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXml%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXmlL%soname
Summary: Shared library of Open CASCADE: libTKXmlL
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXmlL%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXmlTObj%soname
Summary: Shared library of Open CASCADE: libTKXmlTObj
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXmlTObj%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXmlXCAF%soname
Summary: Shared library of Open CASCADE: libTKXmlXCAF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXmlXCAF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSBase%soname
Summary: Shared library of Open CASCADE: libTKXSBase
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSBase%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAW%soname
Summary: Shared library of Open CASCADE: libTKXSDRAW
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAW%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWDE%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWDE
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWDE%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWGLTF%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWGLTF
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWGLTF%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWIGES%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWIGES
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWIGES%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWOBJ%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWOBJ
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWOBJ%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWPLY%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWPLY
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWPLY%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWSTEP%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWSTEP
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWSTEP%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWSTL%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWSTL
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWSTL%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package -n libTKXSDRAWVRML%soname
Summary: Shared library of Open CASCADE: libTKXSDRAWVRML
Group: System/Libraries
Obsoletes: libopencascade7.9

%description -n libTKXSDRAWVRML%soname
Shared libraries of Open CASCADE, development platform for 3D modeling
and numerical simulation applications.

%package devel
Summary: Development files for Open CASCADE Technology
Group: Development/C++
Provides: OCE-devel = %EVR
Obsoletes: OCE-devel < %EVR

%description devel
Development files for Open CASCADE, development platform for 3D
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
%ifarch %arm
%patch2 -p2
%endif
%ifarch %e2k
%patch2000 -p1
%endif

%build
# opencascade does some manual install trickery that does not respect
# DESTDIR.  Make DESTDIR and environment variable that can be passed
# into the CMake config.
export DESTDIR="%buildroot"
# For FreeCAD: -DUSE_RAPIDJSON=ON
%cmake_insource -GNinja \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_TBB=False \
       -DUSE_VTK=True \
       -DINSTALL_DIR_DOC=%_datadir/doc/opencascade \
       -D3RDPARTY_VTK_INCLUDE_DIR=%_includedir/vtk-%vtk_version \
       -DINSTALL_DIR_LIB=%_lib \
       -DINSTALL_DIR_CMAKE=%_lib/cmake/opencascade \
       -DUSE_RAPIDJSON=ON
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

%files -n libTKBin%soname
%_libdir/libTKBin.so.%soname
%_libdir/libTKBin.so.%version

%files -n libTKBinL%soname
%_libdir/libTKBinL.so.%soname
%_libdir/libTKBinL.so.%version

%files -n libTKBinTObj%soname
%_libdir/libTKBinTObj.so.%soname
%_libdir/libTKBinTObj.so.%version

%files -n libTKBinXCAF%soname
%_libdir/libTKBinXCAF.so.%soname
%_libdir/libTKBinXCAF.so.%version

%files -n libTKBO%soname
%_libdir/libTKBO.so.%soname
%_libdir/libTKBO.so.%version

%files -n libTKBool%soname
%_libdir/libTKBool.so.%soname
%_libdir/libTKBool.so.%version

%files -n libTKBRep%soname
%_libdir/libTKBRep.so.%soname
%_libdir/libTKBRep.so.%version

%files -n libTKCAF%soname
%_libdir/libTKCAF.so.%soname
%_libdir/libTKCAF.so.%version

%files -n libTKCDF%soname
%_libdir/libTKCDF.so.%soname
%_libdir/libTKCDF.so.%version

%files -n libTKDCAF%soname
%_libdir/libTKDCAF.so.%soname
%_libdir/libTKDCAF.so.%version

%files -n libTKDE%soname
%_libdir/libTKDE.so.%soname
%_libdir/libTKDE.so.%version

%files -n libTKDECascade%soname
%_libdir/libTKDECascade.so.%soname
%_libdir/libTKDECascade.so.%version

%files -n libTKDEGLTF%soname
%_libdir/libTKDEGLTF.so.%soname
%_libdir/libTKDEGLTF.so.%version

%files -n libTKDEIGES%soname
%_libdir/libTKDEIGES.so.%soname
%_libdir/libTKDEIGES.so.%version

%files -n libTKDEOBJ%soname
%_libdir/libTKDEOBJ.so.%soname
%_libdir/libTKDEOBJ.so.%version

%files -n libTKDEPLY%soname
%_libdir/libTKDEPLY.so.%soname
%_libdir/libTKDEPLY.so.%version

%files -n libTKDESTEP%soname
%_libdir/libTKDESTEP.so.%soname
%_libdir/libTKDESTEP.so.%version

%files -n libTKDESTL%soname
%_libdir/libTKDESTL.so.%soname
%_libdir/libTKDESTL.so.%version

%files -n libTKDEVRML%soname
%_libdir/libTKDEVRML.so.%soname
%_libdir/libTKDEVRML.so.%version

%files -n libTKDraw%soname
%_libdir/libTKDraw.so.%soname
%_libdir/libTKDraw.so.%version

%files -n libTKernel%soname
%_libdir/libTKernel.so.%soname
%_libdir/libTKernel.so.%version

%files -n libTKExpress%soname
%_libdir/libTKExpress.so.%soname
%_libdir/libTKExpress.so.%version

%files -n libTKFeat%soname
%_libdir/libTKFeat.so.%soname
%_libdir/libTKFeat.so.%version

%files -n libTKFillet%soname
%_libdir/libTKFillet.so.%soname
%_libdir/libTKFillet.so.%version

%files -n libTKG2d%soname
%_libdir/libTKG2d.so.%soname
%_libdir/libTKG2d.so.%version

%files -n libTKG3d%soname
%_libdir/libTKG3d.so.%soname
%_libdir/libTKG3d.so.%version

%files -n libTKGeomAlgo%soname
%_libdir/libTKGeomAlgo.so.%soname
%_libdir/libTKGeomAlgo.so.%version

%files -n libTKGeomBase%soname
%_libdir/libTKGeomBase.so.%soname
%_libdir/libTKGeomBase.so.%version

%files -n libTKHLR%soname
%_libdir/libTKHLR.so.%soname
%_libdir/libTKHLR.so.%version

%files -n libTKIVtk%soname
%_libdir/libTKIVtk.so.%soname
%_libdir/libTKIVtk.so.%version

%files -n libTKIVtkDraw%soname
%_libdir/libTKIVtkDraw.so.%soname
%_libdir/libTKIVtkDraw.so.%version

%files -n libTKLCAF%soname
%_libdir/libTKLCAF.so.%soname
%_libdir/libTKLCAF.so.%version

%files -n libTKMath%soname
%_libdir/libTKMath.so.%soname
%_libdir/libTKMath.so.%version

%files -n libTKMesh%soname
%_libdir/libTKMesh.so.%soname
%_libdir/libTKMesh.so.%version

%files -n libTKMeshVS%soname
%_libdir/libTKMeshVS.so.%soname
%_libdir/libTKMeshVS.so.%version

%files -n libTKOffset%soname
%_libdir/libTKOffset.so.%soname
%_libdir/libTKOffset.so.%version

%files -n libTKOpenGl%soname
%_libdir/libTKOpenGl.so.%soname
%_libdir/libTKOpenGl.so.%version

%files -n libTKOpenGlTest%soname
%_libdir/libTKOpenGlTest.so.%soname
%_libdir/libTKOpenGlTest.so.%version

%files -n libTKPrim%soname
%_libdir/libTKPrim.so.%soname
%_libdir/libTKPrim.so.%version

%files -n libTKQADraw%soname
%_libdir/libTKQADraw.so.%soname
%_libdir/libTKQADraw.so.%version

%files -n libTKRWMesh%soname
%_libdir/libTKRWMesh.so.%soname
%_libdir/libTKRWMesh.so.%version

%files -n libTKService%soname
%_libdir/libTKService.so.%soname
%_libdir/libTKService.so.%version

%files -n libTKShHealing%soname
%_libdir/libTKShHealing.so.%soname
%_libdir/libTKShHealing.so.%version

%files -n libTKStd%soname
%_libdir/libTKStd.so.%soname
%_libdir/libTKStd.so.%version

%files -n libTKStdL%soname
%_libdir/libTKStdL.so.%soname
%_libdir/libTKStdL.so.%version

%files -n libTKTObj%soname
%_libdir/libTKTObj.so.%soname
%_libdir/libTKTObj.so.%version

%files -n libTKTObjDRAW%soname
%_libdir/libTKTObjDRAW.so.%soname
%_libdir/libTKTObjDRAW.so.%version

%files -n libTKTopAlgo%soname
%_libdir/libTKTopAlgo.so.%soname
%_libdir/libTKTopAlgo.so.%version

%files -n libTKTopTest%soname
%_libdir/libTKTopTest.so.%soname
%_libdir/libTKTopTest.so.%version

%files -n libTKV3d%soname
%_libdir/libTKV3d.so.%soname
%_libdir/libTKV3d.so.%version

%files -n libTKVCAF%soname
%_libdir/libTKVCAF.so.%soname
%_libdir/libTKVCAF.so.%version

%files -n libTKViewerTest%soname
%_libdir/libTKViewerTest.so.%soname
%_libdir/libTKViewerTest.so.%version

%files -n libTKXCAF%soname
%_libdir/libTKXCAF.so.%soname
%_libdir/libTKXCAF.so.%version

%files -n libTKXDEDRAW%soname
%_libdir/libTKXDEDRAW.so.%soname
%_libdir/libTKXDEDRAW.so.%version

%files -n libTKXMesh%soname
%_libdir/libTKXMesh.so.%soname
%_libdir/libTKXMesh.so.%version

%files -n libTKXml%soname
%_libdir/libTKXml.so.%soname
%_libdir/libTKXml.so.%version

%files -n libTKXmlL%soname
%_libdir/libTKXmlL.so.%soname
%_libdir/libTKXmlL.so.%version

%files -n libTKXmlTObj%soname
%_libdir/libTKXmlTObj.so.%soname
%_libdir/libTKXmlTObj.so.%version

%files -n libTKXmlXCAF%soname
%_libdir/libTKXmlXCAF.so.%soname
%_libdir/libTKXmlXCAF.so.%version

%files -n libTKXSBase%soname
%_libdir/libTKXSBase.so.%soname
%_libdir/libTKXSBase.so.%version

%files -n libTKXSDRAW%soname
%_libdir/libTKXSDRAW.so.%soname
%_libdir/libTKXSDRAW.so.%version

%files -n libTKXSDRAWDE%soname
%_libdir/libTKXSDRAWDE.so.%soname
%_libdir/libTKXSDRAWDE.so.%version

%files -n libTKXSDRAWGLTF%soname
%_libdir/libTKXSDRAWGLTF.so.%soname
%_libdir/libTKXSDRAWGLTF.so.%version

%files -n libTKXSDRAWIGES%soname
%_libdir/libTKXSDRAWIGES.so.%soname
%_libdir/libTKXSDRAWIGES.so.%version

%files -n libTKXSDRAWOBJ%soname
%_libdir/libTKXSDRAWOBJ.so.%soname
%_libdir/libTKXSDRAWOBJ.so.%version

%files -n libTKXSDRAWPLY%soname
%_libdir/libTKXSDRAWPLY.so.%soname
%_libdir/libTKXSDRAWPLY.so.%version

%files -n libTKXSDRAWSTEP%soname
%_libdir/libTKXSDRAWSTEP.so.%soname
%_libdir/libTKXSDRAWSTEP.so.%version

%files -n libTKXSDRAWSTL%soname
%_libdir/libTKXSDRAWSTL.so.%soname
%_libdir/libTKXSDRAWSTL.so.%version

%files -n libTKXSDRAWVRML%soname
%_libdir/libTKXSDRAWVRML.so.%soname
%_libdir/libTKXSDRAWVRML.so.%version

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
* Tue Jun 23 2026 Ulysses Apokin <ulysses@altlinux.org> 7.9.3-alt2
- NMU: Enable rapidjson option for FreeCAD.

* Thu Dec 11 2025 Constantin Sunzow <protvin@altlinux.org> 7.9.3-alt1
- New version.

* Sun Oct 26 2025 Constantin Sunzow <protvin@altlinux.org> 7.9.2-alt1
- New version.

* Thu Jul 24 2025 Constantin Sunzow <protvin@altlinux.org> 7.9.1-alt1
- Update license tag for correct parsing exception.
- Split libraries on related subpackages.
- Update e2k patch (by ilyakurdyukov@).
- New version.

* Mon Jul 14 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 7.9.0-alt2
- e2k build fix

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

