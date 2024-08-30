%define        _unpackaged_files_terminate_build 1
%define        oname openMVG

Name:          openmvg
Version:       2.1
Release:       alt5
Summary:       open Multiple View Geometry
License:       MPL-2.0
Group:         System/Libraries
Url:           https://github.com/openMVG/openMVG
Vcs:           https://github.com/openMVG/openMVG.git

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: ghostscript
BuildRequires: eigen3
BuildRequires: libgomp-devel
#BuildRequires: libflann-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libopencv-devel
BuildRequires: libmetis-devel
BuildRequires: libcoinor-utils-devel
BuildRequires: libcoinor-osi-devel
BuildRequires: libcoinor-clp-devel
BuildRequires: libcoinor-osi-clp-devel
BuildRequires: libcoinor-lemon-devel
BuildRequires: libeasyexif-devel
#BuildRequires: libfast-devel
BuildRequires: libglog-devel
BuildRequires: ceres-solver-devel
# NOTE not defined in CMakeLists
BuildRequires: cereal-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: libsphinxclient-devel
BuildRequires: libsuitesparse-devel
BuildRequires: python3-module-cmake_build_extension

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
open Multiple View Geometry library. Basis for 3D computer vision and Structure
from Motion.

OpenMVG provides an end-to-end 3D reconstruction from images framework
compounded of libraries, binaries, and pipelines.

* The libraries provide easy access to features like: images manipulation,
  features description and matching, feature tracking, camera models,
  multiple-view-geometry, robust-estimation, structure-from-motion algorithms.
* The binaries solve unit tasks that a pipeline could require: scene
  initialization, feature detection & matching and structure-from-motion
  reconstruction, export the reconstructed scene to others
  Multiple-View-Stereovision framework to compute dense point clouds or textured
  meshes.
* The pipelines are created by chaining various binaries to compute image
  matching relation, solve the Structure from Motion problem (reconstruction,
  triangulation, localization).

OpenMVG is developed in C++ and runs on Android, iOS, Linux, macOS, and Windows.


%package       -n lib%name
Summary:       open Multiple View Geometry library
Group:         System/Libraries

%description   -n lib%name
open Multiple View Geometry library. Basis for 3D computer vision and Structure
from Motion.

OpenMVG provides an end-to-end 3D reconstruction from images framework
compounded of libraries, binaries, and pipelines.

* The libraries provide easy access to features like: images manipulation,
  features description and matching, feature tracking, camera models,
  multiple-view-geometry, robust-estimation, structure-from-motion algorithms.
* The binaries solve unit tasks that a pipeline could require: scene
  initialization, feature detection & matching and structure-from-motion
  reconstruction, export the reconstructed scene to others
  Multiple-View-Stereovision framework to compute dense point clouds or textured
  meshes.
* The pipelines are created by chaining various binaries to compute image
  matching relation, solve the Structure from Motion problem (reconstruction,
  triangulation, localization).

OpenMVG is developed in C++ and runs on Android, iOS, Linux, macOS, and Windows.


%package       -n lib%name-devel
Summary:       open Multiple View Geometry library development files
Group:         Development/Other
Requires:      %name = %version-%release

Requires:      cmake
Requires:      gcc-c++
Requires:      doxygen
Requires:      ghostscript
Requires:      eigen3
Requires:      libgomp-devel
#Requires:      libflann-devel
Requires:      libjpeg-devel
Requires:      libpng-devel
Requires:      libopencv-devel
Requires:      libmetis-devel
Requires:      libcoinor-utils-devel
Requires:      libcoinor-osi-devel
Requires:      libcoinor-clp-devel
Requires:      libcoinor-osi-clp-devel
Requires:      libcoinor-lemon-devel
Requires:      libeasyexif-devel
Requires:      libglog-devel
Requires:      ceres-solver-devel
Requires:      cereal-devel
Requires:      qt5-base-devel
Requires:      qt5-svg-devel
Requires:      libsphinxclient-devel
Requires:      libsuitesparse-devel
Requires:      python3-module-cmake_build_extension

%description   -n lib%name-devel
open Multiple View Geometry library. Basis for 3D computer vision and Structure
from Motion.

OpenMVG provides an end-to-end 3D reconstruction from images framework
compounded of libraries, binaries, and pipelines.

* The libraries provide easy access to features like: images manipulation,
  features description and matching, feature tracking, camera models,
  multiple-view-geometry, robust-estimation, structure-from-motion algorithms.
* The binaries solve unit tasks that a pipeline could require: scene
  initialization, feature detection & matching and structure-from-motion
  reconstruction, export the reconstructed scene to others
  Multiple-View-Stereovision framework to compute dense point clouds or textured
  meshes.
* The pipelines are created by chaining various binaries to compute image
  matching relation, solve the Structure from Motion problem (reconstruction,
  triangulation, localization).

OpenMVG is developed in C++ and runs on Android, iOS, Linux, macOS, and Windows.


%prep
%setup
%autopatch -p1
%ifarch %e2k
# needs to be linked with the -fopenmp option
sed -i '/include_directories(${OpenMP_C_INCLUDE_DIR})/i add_link_options(-fopenmp)' src/CMakeLists.txt
# workaround for "extern template class"
sed -i '1i #define IMAGE_IO_CPP' src/openMVG/image/image_io.cpp
sed -i '/^extern template/s/.*/#ifndef IMAGE_IO_CPP\n&\n#endif/' src/openMVG/image/image_io.hpp
# fix num_threads in pragmas
sed -i -E "/^[[:space:]]*#pragma omp .*[[:space:]]num_threads\(/{s/#/for(long &/;\
s/(#.*num_threads\()([^()]*)\)/_xxxn=\\2,\\1_xxxn)/;\
s/#/_xxxc=1;_xxxc;_xxxc=0)\n&/}" \
	src/third_party/flann/src/cpp/flann/algorithms/*.h \
	src/third_party/ceres-solver/internal/ceres/*.h
# fix endianness and collision with other LCC
sed -i 's/defined(__LCC__)/0/;s/defined(__LITTLE_ENDIAN__)/1/' src/nonFree/sift/vl/host.h
%endif

%build
cd src
%cmake \
   -DCMAKE_MODULE_PATH=%_libdir/cmake/ \
   -DBUILD_SHARED_LIBS=ON \
   -DOpenMVG_BUILD_SHARED=ON \
   -DOpenMVG_BUILD_DOC=OFF \
   -DOpenMVG_USE_OPENCV=ON \
   -DOpenMVG_USE_OPENMP=ON \
   -DOSI_INCLUDE_DIR_HINTS=ON \
   -DCLP_INCLUDE_DIR_HINTS=ON \
   -DCOINUTILS_INCLUDE_DIR_HINTS=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo
#false
%cmake_build

%install
cd src
%cmakeinstall_std
rm -f %buildroot%_libexecdir/pkgconfig/flann.pc
rm -rf %buildroot%_libdir/openMVG/webgl
rm -f %buildroot%_libdir/openMVG/sensor_width_camera_database.txt
rm -rf %buildroot%_includedir/openMVG_dependencies/
%ifarch loongarch64
rm -f %buildroot%_libdir/libopenMVG_ceres.a
%endif

%files
%doc *.md AUTHORS LICENSE
%_bindir/openMVG_*
%_bindir/ui_openMVG_*

%files         -n lib%name
%doc *.md AUTHORS LICENSE
%_libdir/lib%{oname}_*.so.*
%_libdir/libvlsift.so

%files         -n lib%name-devel
%doc *.md AUTHORS LICENSE
%_libdir/lib%{oname}_*.so
%_cmakedir/%oname/
%_includedir/%oname/


%changelog
* Wed Aug 28 2024 Pavel Skrylev <majioa@altlinux.org> 2.1-alt5
- + added explicit requires for glog package
- ! for newer version of glog 1.7.1 this is required expicit exprt
    declaration must be provided
- ! closed specific loongarch code

* Sat May 25 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1-alt4
- fix e2k build again

* Sat Mar 23 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.1-alt3
- Fixed FTBFS on LoongArch (remove static library).

* Fri Mar 22 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1-alt2
- Fixed build for Elbrus

* Sat Mar 02 2024 Pavel Skrylev <majioa@altlinux.org> 2.1-alt1
- Initial build v2.1 for Sisyphus
