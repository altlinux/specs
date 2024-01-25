%define        _unpackaged_files_terminate_build 1
%define        oname OpenMesh
%define        oname1 OpenMeshCore
%define        oname2 OpenMeshTools
%define        name1 openmesh-core
%define        name2 openmesh-tools

Name:          openmesh
Version:       10.0
Release:       alt1
Summary:       A generic and efficient polygon mesh data structure
License:       BSD-3-Clause
Group:         Sciences/Mathematics
Url:           https://www.graphics.rwth-aachen.de/software/openmesh/
Vcs:           https://www.graphics.rwth-aachen.de:9000/OpenMesh/OpenMesh.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Source1:       FindOpenMesh.cmake
Patch:         patch.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake-library
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: texlive
BuildRequires: libglfw-devel
%ifnarch armh
BuildRequires: qt5-base-devel
%endif

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n %{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      %{name} = %EVR
Requires:      lib%{name1}-devel = %EVR
Requires:      lib%{name2}-devel = %EVR

%description   -n %{name}-devel
OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n lib%{name1}
Group:         System/Libraries
Summary:       Library Core code for %name

%description   -n lib%{name1}
OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n lib%{name1}-devel
Group:         Development/C++
Summary:       Development Core files for %name

Requires:      lib%{name1} = %EVR
Requires:      cmake-library
Requires:      gcc-c++
Requires:      doxygen
Requires:      texlive
Requires:      libglfw-devel

%description   -n lib%{name1}-devel
OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n lib%{name1}-devel-static
Group:         Development/C++
Summary:       Development Core static files for %name

Requires:      lib%{name1}-devel = %EVR

%description   -n lib%{name1}-devel-static
Development Core static files for %name.

OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n lib%{name2}
Group:         System/Libraries
Summary:       Library Tools code for %name

%description   -n lib%{name2}
OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n lib%{name2}-devel
Group:         Development/C++
Summary:       Development Tools files for %name

Requires:      lib%{name2} = %EVR
Requires:      cmake-library
Requires:      gcc-c++
Requires:      doxygen
Requires:      texlive
Requires:      libglfw-devel

%description   -n lib%{name2}-devel
OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%package       -n lib%{name2}-devel-static
Group:         Development/C++
Summary:       Development Tools static files for %name

Requires:      lib%{name2}-devel = %EVR

%description   -n lib%{name2}-devel-static
Development Tools static files for %name.

OpenMesh is a generic and efficient data structure for representing and
manipulating polygonal meshes. For more information about OpenMesh and its
features take a look at the Introduction page.

OpenMesh is a C++ library.


%prep
%setup
%autopatch

%build
%cmake -DOpenGL_GL_PREFERENCE:STRING=GLVND \
       -DOPENMESH_BUILD_SHARED:BOOL=ON \
       -DCMAKE_CONFIG_DIR:STRING=%_libexecdir/cmake/%{oname} \
       -DPKGCONFIG_DIR:STRING=%_pkgconfigdir \
       -DOPENMESH_DOCS:BOOL=ON \
       -DCMAKE_MODULE_PATH:PATH=%_libdir/cmake/VCI

%cmake_build

%install
%cmakeinstall_std
install -Dm644 %SOURCE1 %buildroot%_datadir/cmake/Modules/FindOpenMesh.cmake

%files
%doc README*
%_bindir/*

%files         -n %{name}-devel
%_pkgconfigdir/%{name}.pc
%_libexecdir/cmake/%{oname}
%_datadir/cmake/Modules/

%files         -n lib%{name1}
%_libdir/lib%{oname1}*.so.*

%files         -n lib%{name1}-devel
%_libdir/lib%{oname1}*.so
%_includedir/%{oname}/Core

%files         -n lib%{name1}-devel-static
%_libdir/lib%{oname1}.a

%files         -n lib%{name2}
%_libdir/lib%{oname2}*.so.*

%files         -n lib%{name2}-devel
%_libdir/lib%{oname2}*.so
%_includedir/%{oname}/Tools

%files         -n lib%{name2}-devel-static
%_libdir/lib%{oname2}.a

%changelog
* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 10.0-alt1
- initial build for Sisyphus
