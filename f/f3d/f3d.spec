%define _unpackaged_files_terminate_build 1

%def_with python

Name: f3d
Version: 3.2.0
Release: alt1

Summary: Fast and minimalist 3D viewer
License: BSD-3-Clause
Group: Graphics
Url: https://github.com/f3d-app/f3d
VCS: https://f3d.app/
Source: %name-%version.tar
Patch: f3d-3.2.0-alt-vtk-9.4.patch

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: alembic-devel
BuildRequires: imath-devel
BuildRequires: opencascade-devel
BuildRequires: libstdc++-devel-static
BuildRequires: gcc-c++
BuildRequires: libvtk-devel
BuildRequires: pybind11-devel
BuildRequires: pkgconfig(assimp)
BuildRequires: libminizip-devel
BuildRequires: libpoly2tri-devel
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: python3-module-imath-devel
BuildRequires: libfast_float-devel
BuildRequires: libfmt-devel
BuildRequires: libGLEW-devel
BuildRequires: libglvnd-devel
BuildRequires: help2man


%if_with python
BuildRequires: python3-dev
BuildRequires(pre): rpm-build-python3
%endif

%description
F3D is a fast and minimalist 3D viewer desktop application. It supports
many file formats, from digital content to scientific datasets
(including glTF, STL, STEP, PLY, OBJ, FBX, Alembic), can show animations
and support thumbnails and many rendering and texturing options including
real time physically based rendering and raytracing.

%package devel
Summary: Development files for f3d
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development files for f3d.

%if_with python
%package -n python3-module-f3d
Summary: Python 3 bindings for f3d
Group: Development/Python
Requires: %name = %EVR

%description -n python3-module-f3d
This package contains Python 3 bindings for f3d.
%endif

%prep
%setup
%patch -p1

%build

%cmake \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTING=OFF \
    -DF3D_LINUX_APPLICATION_LINK_FILESYSTEM=ON \
    -DF3D_LINUX_GENERATE_MAN=ON \
    -DF3D_LINUX_INSTALL_DEFAULT_CONFIGURATION_FILE_IN_PREFIX=ON \
    -DF3D_MODULE_EXTERNAL_RENDERING=OFF \
    -DF3D_MODULE_RAYTRACING=OFF \
    -DF3D_LINUX_LIBRARY_LINK_ATOMIC=ON \
%if_with python
    -DF3D_BINDINGS_PYTHON=ON \
%endif

%cmake_build

%install
%cmake_install

%cmake_install --component mimetypes
%cmake_install --component sdk
%cmake_install --component configuration

rm -rfv %{buildroot}%{_docdir}/* # Remove duplicate docs

install -Dm 644 \
  %_cmake__builddir/%_lib/vtk/hierarchy/f3d_vtkext/vtkext-hierarchy.txt \
  -t %buildroot/%_libdir/vtk/hierarchy/f3d_vtkext/

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
%_libdir/libf3d.so*
%_libdir/libvtkext.so


%doc README.md LICENSE.md

%files devel
%_libdir/cmake/f3d_vtkext
%_includedir/%name
%_libdir/cmake/%name/*
%dir %_libdir/cmake/%name
%dir %_libdir/vtk/hierarchy/f3d_vtkext
%_libdir/vtk/hierarchy/f3d_vtkext/vtkext-hierarchy.txt

%if_with python
%files -n python3-module-f3d
%python3_sitelibdir/%name
%endif

%changelog
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
