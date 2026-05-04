%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define abiversion 3

# Issue URL:
# https://github.com/maplibre/maplibre-native-qt/issues/119
# linking with lto generates some strange warnings and temporary disabled
%define optflags_lto %nil

Name: libmaplibre-native-qt
Version: 3.0.0
Release: alt2

Summary: MapLibre Native Qt bindings
License: BSD-2-Clause
Group: Sciences/Geosciences
URL: https://maplibre.org
VCS: https://github.com/maplibre/maplibre-native-qt.git

Source0: %name-%version.tar
Patch0: libmaplibre-native-qt-3.0.0-upstream-fix-gcc15.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-location-devel
BuildRequires: zlib-devel

%description
MapLibre Native is a free and open-source library for publishing maps
in your apps and desktop applications on various platforms. Fast
displaying of maps is possible thanks to GPU-accelerated vector
tile rendering.

%package -n %name%abiversion
Summary: %summary
Group: System/Libraries

%description -n %name%abiversion
MapLibre Native is a free and open-source library for publishing maps
in your apps and desktop applications on various platforms. Fast
displaying of maps is possible thanks to GPU-accelerated vector
tile rendering.

%package devel
Summary: Development libraries and headers for %name
Group: Development/C++
Requires: %name%abiversion = %EVR

%description devel
Development libraries and headers for %name.

%prep
%setup
%patch0 -p2

%build
%cmake \
    -DMLN_QT_WITH_LOCATION=OFF \
    -DMLN_QT_WITH_WIDGETS=OFF \
    -DBUILD_TESTING=OFF \
    %nil
%cmake_build

%install
%cmake_install

%files -n %name%abiversion
%_libdir/libQMapLibre.so.%abiversion
%_libdir/libQMapLibre.so.%abiversion.*

%files devel
%_includedir/mbgl/
%_includedir/QMapLibre/
%_libdir/libQMapLibre.so
%_libdir/cmake/QMapLibre/

%changelog
* Wed Apr 29 2026 Egor Shestakov <ved@altlinux.org> 3.0.0-alt2
- Fix build with gcc15.

* Tue Oct 14 2025 Egor Shestakov <ved@altlinux.org> 3.0.0-alt1
- Initial build.
