%define _unpackaged_files_terminate_build 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define dynname dynamicedt3d
%define ocvname octovis

%define abiversion 1

Name:    octomap
Version: 1.10.0
Release: alt2

Summary: An Efficient Probabilistic 3D Mapping Framework Based on Octrees
License: BSD
Group:   Development/C++
Url: 	 http://octomap.github.io
Vcs:     https://github.com/OctoMap/octomap.git

Source: %name-%version.tar

BuildRequires(pre): cmake ninja-build
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: qt5-base-devel
BuildRequires: libQGLViewer-devel
BuildRequires: libGL-devel libGLU-devel

Patch0: 0001-Fixed-libdir-paths-and-deleted-static-libraries.patch

Requires:      lib%name = %EVR

%description
OctoMap - An Efficient Probabilistic 3D Mapping Framework Based on Octrees.
OctoMap consists of two separate libraries each in its own subfolder: octomap,
the actual library, and octovis, our visualization libraries and tools.

%package 	-n lib%name
Summary: 	An Efficient Probabilistic 3D Mapping Framework Based on Octrees
Group: 		System/Libraries

%description 	-n lib%name
OctoMap - An Efficient Probabilistic 3D Mapping Framework Based on Octrees.
OctoMap consists of two separate libraries each in its own subfolder: octomap,
the actual library, and octovis, our visualization libraries and tools.

%package 	devel
Summary:	Development files and libraries for %name
Group:		Development/C++	
Requires: 	lib%name = %EVR

%description 	devel
This package contains the header files and development libraries
for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%package 	-n lib%dynname
Summary: 	Dynamic Euclidian Distance Transform Implementation
Group:		System/Libraries
Requires: 	lib%name = %EVR

%description 	-n lib%dynname
The dynamicEDT3D library implements an incrementally updatable Euclidean
distance transform (EDT) in 3D. It comes with a wrapper to use the OctoMap
3D representation and hooks into the change detection of the OctoMap library
to propagate changes to the EDT.

%package 	-n %dynname-devel
Summary: 	Development files and libraries for dynamicEDT3D
Group:		Development/C++
Requires: 	%name-devel = %EVR
Requires: 	lib%dynname = %EVR

%description 	-n %dynname-devel
This package contains the header files and development libraries
for dynamic-edt-3d. If you like to develop programs using dynamic-edt-3d,
you will need to install dynamic-edt-3d-devel.

%package        -n %ocvname
Summary:        Qt-based 3D viewer for OctoMap (%ocvname)
Group:          Development/C++
Requires:       %name = %EVR
Requires:       lib%ocvname = %EVR

%description    -n %ocvname
%ocvname is a Qt-based 3D visualization tool for the OctoMap library,
built on top of libQGLViewer.

%package        -n lib%ocvname
Summary:        Shared libraries for %ocvname
Group:          System/Libraries

%description    -n lib%ocvname
This package provides the shared libraries used by %ocvname.

%package 	-n %ocvname-devel
Summary: 	Development files and libraries for %ocvname
Group: 		Development/C++
Requires: 	lib%ocvname = %EVR
Requires: 	%name-devel

%description 	-n %ocvname-devel
This package contains the header files and development libraries
for octovis. If you like to develop programs using octovis,
you will need to install octovis-devel.

%prep
%setup
%autopatch -p1

%build
# We install octomap into a staging DESTDIR during build so that other
# subprojects (dynamicEDT3D, octovis) can find it via CMake config-mode
# find_package(octomap) using a *valid* installed octomap-config.cmake.
# Without this staging install, they may pick up the broken build-tree
# config and fail during configure, e.g.:
#   CMake Error at lib/cmake/octomap/octomap-config.cmake:36 (message):
#     ... referenced by variable OCTOMAP_INCLUDE_DIRS does not exist !
#   ... dynamicEDT3D/CMakeLists.txt:54 (find_package)

STAGE="%_builddir/%name-%version/.stage"
rm -rf "$STAGE"
%define _cmake__builddir build-octomap
pushd octomap
	%cmake
	%cmake_build
	DESTDIR="$STAGE" cmake --install build-octomap
popd
OCTOMAP_PREFIX="$STAGE%_prefix"
OCTOMAP_DIR="$STAGE%_libdir/cmake/octomap"
%define _cmake__builddir build-dynamicEDT3D
pushd dynamicEDT3D
        %cmake  -DCMAKE_PREFIX_PATH="$OCTOMAP_PREFIX" \
  		-Doctomap_DIR="$OCTOMAP_DIR" 
        %cmake_build
popd
%define _cmake__builddir build-octovis
pushd octovis
        %cmake  -DCMAKE_PREFIX_PATH="$OCTOMAP_PREFIX" \
  		-Doctomap_DIR="$OCTOMAP_DIR"
        %cmake_build
popd


%install
%define _cmake__builddir build-octomap
pushd octomap
        %cmake_install
popd
%define _cmake__builddir build-dynamicEDT3D
pushd dynamicEDT3D
        %cmake_install
popd
pushd octovis
	%define _cmake__builddir build-octovis
        %cmake_install
popd

%files
%doc *.md
%_bindir/binvox2bt
%_bindir/bt2vrml
%_bindir/compare_octrees
%_bindir/convert_octree
%_bindir/edit_octree
%_bindir/eval_octree_accuracy
%_bindir/graph2tree
%_bindir/log2graph

%files		-n lib%name
%_libdir/lib%name.so.%{abiversion}*
%_libdir/liboctomath.so.%{abiversion}*

%files 		devel
%_includedir/%name
%_libdir/lib%name.so
%_libdir/liboctomath.so
%_pkgconfigdir/%name.pc
%_cmakedir/%name
%_datadir/%name
%_datadir/ament_index

%files 		-n lib%dynname
%_libdir/lib%dynname.so.%{abiversion}*

%files 		-n %dynname-devel
%_includedir/dynamicEDT3D
%_libdir/lib%dynname.so
%_pkgconfigdir/dynamicEDT3D.pc
%_cmakedir/dynamicEDT3D
%_datadir/dynamic_edt_3d

%files 		-n %ocvname
%_bindir/%ocvname

%files 		-n lib%ocvname
%_libdir/lib%ocvname.so.%{abiversion}*

%files 		-n %ocvname-devel
%_includedir/%ocvname
%_libdir/lib%ocvname.so
%_datadir/%ocvname
%_cmakedir/%ocvname

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 1.10.0-alt2
- Added ABI versioning.

* Fri Jan 23 2026 Nikita Shmatko <nash@altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus.
