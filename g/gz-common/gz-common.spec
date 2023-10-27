%define _unpackaged_files_terminate_build 1

Name:    gz-common
Version: 5.4.0
Release: alt3

Summary: Gazebo Common : AV, Graphics, Events, and much more
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-common

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: gz-common-alt-fix-build.patch
Patch1: gz-common-alt-gcc13.patch
Patch2: gz-common-alt-gdal-without-version.patch

# XXX: gz_remotery_vis calls `xdg-open` if available tries
# XXX: `open` if not (presumably to support both Linux and macos).
# XXX: This causes a spurious dependency on gnustep (which tries
# XXX: to mimic macos)
%filter_from_requires /\/bin\/open$/d

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-math-devel
BuildRequires: libgz-utils-devel
BuildRequires: libuuid-devel
BuildRequires: libswscale-devel
BuildRequires: libswresample-devel
BuildRequires: libavdevice-devel
BuildRequires: libavformat-devel
BuildRequires: libavfilter-devel
BuildRequires: libavcodec-devel
BuildRequires: libavutil-devel
BuildRequires: libgts-devel
BuildRequires: libpostproc-devel
BuildRequires: libpcre2-devel
BuildRequires: libfreeimage-devel
BuildRequires: libstdc++-devel-static
#TODO: error build
BuildRequires: libgdal-devel
BuildRequires: libassimp-devel
BuildRequires: libminizip-devel
BuildRequires: libstbi-devel
BuildRequires: libpoly2tri-devel

%description
An audio-visual library supports processing audio and video files, a graphics
library can load a variety 3D mesh file formats into a generic in-memory
representation, and the core library of Gazebo Common contains functionality
that spans Base64 encoding/decoding to thread pools.

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake -GNinja -Wno-dev
#cmake_build
%ninja_build -C "%_cmake__builddir"

%install
#cmake_install
%ninja_install -C "%_cmake__builddir"

%files
%doc AUTHORS README.md
%_prefix/libexec/gz/gz-common*/gz_remotery_vis
%_datadir/gz/gz-common*

%files -n lib%name
%_libdir/lib*.so.*
%_libdir/lib*.so

%files -n lib%{name}-devel
%_includedir/gz/common*
%_libdir/cmake/gz-common*
%_libdir/pkgconfig/*.pc

%changelog
* Fri Oct 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.4.0-alt3
- NMU: avoid spurious dependency on gnustep.

* Wed Sep 20 2023 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt2
- FTBFS: removed libavresample-devel.

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt2
- Moved .so files to main package.

* Fri May 26 2023 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 3.15.1-alt1
- Initial build for Sisyphus.
