%define _unpackaged_files_terminate_build 1
#Support HDF5
%def_with hdf5

#Support for OpenEXR images.
%def_with exr

#Support for WebP images.
%def_with webp

#Support for FBX, DAE, OFF, DXF, X and 3MF file formats.
%def_with assimp

#Support for ABC file format.
%def_with alembic

#Support for STEP, IGES, BREP, and XBF file formats.
%def_with occt

#Generate C bindings.
%def_with C

#Generate Java bindings.
%def_with java

#Generate Python3 bindings.
%def_with python3


Name: f3d
Version: 3.4.1
Release: alt1

Summary: Fast and minimalist 3D viewer
License: BSD-3-Clause
Group: Graphics

Url: https://f3d.app/
VCS: https://github.com/f3d-app/f3d

Source: %name-%version.tar

Patch: f3d_3.4.1_Assimp.patch
Patch2: f3d_3.4.1_vtk_9.5.2.patch
Patch3: f3d_3.4.1_EXRReader.patch
Patch4: f3d_3.4.1_WebPReader.patch
Patch5: f3d_3.4.1_AlembicReader.patch
Patch6: f3d_3.4.1_OCCTReader.patch


BuildRequires(pre): cmake

BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: libvtk-devel
BuildRequires: help2man
BuildRequires: libstdc++-devel-static
BuildRequires: libfreetype-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: pybind11-devel
%endif


%if_with java
BuildRequires(pre): rpm-build-java
BuildRequires: java-1.8.0-openjdk-devel
%endif

%{?_with_occt:BuildRequires: opencascade-devel}
%{?_with_exr:BuildRequires: openexr-devel}
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_assimp:BuildRequires: libassimp-devel libminizip-devel libpoly2tri-devel}
%{?_with_alembic:BuildRequires: alembic-devel}
%{?_with_hdf5:BuildRequires: libhdf5-devel}

%description
F3D is a fast and minimalist 3D viewer desktop application. It supports
many file formats, from digital content to scientific datasets
(including glTF, STL, STEP, PLY, OBJ, FBX, Alembic), can show animations
and support thumbnails and many rendering and texturing options including
real time physically based rendering and raytracing.


%package -n lib%name
Summary: f3d runtime libraries
Group: System/Libraries

%description -n lib%name
This package contains shared libraries required by F3D 3D viewer
and its plugins at runtime.

%package -n lib%name-devel
Summary: Development files for f3d
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains development files for f3d.

%if_with python3
%package -n python3-module-%name
Summary: Python 3 bindings for f3d
Group: Development/Python3

%description -n python3-module-%name
This package contains Python 3 bindings for f3d.
%endif


%if_with C
%package -n lib%name-c
Summary: C bindings for f3d
Group: Development/C

%description -n lib%name-c
This package contains C bindings for f3d.
%endif


%if_with java
%package -n %name-java
Summary: Java bindings for f3d
Group: Development/Java

%description -n %name-java
This package contains Java bindings for f3d.
%endif


%prep
%setup
%patch -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1


%build

%cmake \
    -Wno-dev \
    -DCMAKE_INSTALL_DOCDIR:PATH=%_docdir/%name \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=OFF \
    -DF3D_LINUX_LINK_FILESYSTEM=ON \
    -DF3D_LINUX_GENERATE_MAN=ON \
    -DF3D_LINUX_INSTALL_DEFAULT_CONFIGURATION_FILE_IN_PREFIX=ON \
    -DF3D_MODULE_RAYTRACING=OFF \
    -DF3D_MODULE_EXR=%{with exr} \
    -DF3D_MODULE_WEBP=%{with webp} \
    -DF3D_PLUGIN_BUILD_HDF=%{with hdf5} \
    -DF3D_PLUGIN_BUILD_ALEMBIC=%{with alembic} \
    -DF3D_PLUGIN_BUILD_ASSIMP=%{with assimp} \
    -DF3D_PLUGIN_BUILD_OCCT=%{with occt} \
    -DF3D_LINUX_LIBRARY_LINK_ATOMIC=ON \
    -DF3D_BINDINGS_PYTHON=%{with python3} \
    -DF3D_BINDINGS_C=%{with C} \
    -DF3D_BINDINGS_JAVA=%{with java}

%cmake_build

%install
%cmake_install

%cmake_install --component mimetypes
%cmake_install --component sdk
%cmake_install --component configuration

rm -rv %buildroot%_docdir/*

install -Dm 644 \
  %_cmake__builddir/%_lib/cmake/f3d_vtkext/* \
  -t %buildroot/%_libdir/cmake/f3d_vtkext/

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/applications/*
%_datadir/%name/*
%dir %_datadir/%name
%_datadir/thumbnailers/*
%_datadir/mime/*
%_datadir/fish/*
%_datadir/metainfo/*
%_datadir/zsh/*
%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/HighContrast/scalable/apps/%name.svg
%_man1dir/%name.1.xz

%doc README.md LICENSE.md

%files -n lib%name
%_libdir/*.so.*
%_libdir/libvtkext.so

%files -n lib%name-devel
%_libdir/lib%name.so
%_libdir/cmake/f3d_vtkext
%_includedir/%name
%_libdir/cmake/%name/*
%dir %_libdir/cmake/%name

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/%name
%endif


%if_with C
%files -n libf3d-c
%_libdir/libf3d_c_api.so
%endif


%if_with java
%files -n f3d-java
%_javadir/%name.jar
%_libdir/libf3d-java.so
%endif

%changelog
* Tue Mar 10 2026 Valentin Sokolov <sova@altlinux.org> 3.4.1-alt1
- Update to version 3.4.1.

* Thu Aug 21 2025 Valentin Sokolov <sova@altlinux.org> 3.2.0-alt1
- Update to version 3.2.0.

* Fri Apr 29 2025 Valentin Sokolov <sova@altlinux.org> 3.0.0-alt3
- Rebuild with libraries and bindings for python3

* Mon Feb 17 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.0-alt2
- Rebuild against vtk 9.4.

* Fri Jan 24 2025 Anastasia Osmolovskaya <lola@altlinux.org> 3.0.0-alt1
- Updated to version 3.0.0.

* Tue Jan 07 2025 Anastasia Osmolovskaya <lola@altlinux.org> 2.5.1-alt1
- Updated to version 2.5.1.

* Wed Aug 07 2024 Anastasia Osmolovskaya <lola@altlinux.org> 2.5.0-alt1
- Initial build for ALT.
