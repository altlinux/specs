%define _unpackaged_files_terminate_build 1
%define soversion 7

Name: gz-common
Version: 7.3.0
Release: alt1

Summary: Gazebo Common : AV, Graphics, Events, and much more
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/common/
Vcs: https://github.com/gazebosim/gz-common

Source: %name-%version.tar
Patch1: gz-common-7.0.0-alt-fix-path-conflict-when-tests-parallelized.patch

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
BuildRequires: libpcre2-devel
BuildRequires: libfreeimage-devel
BuildRequires: libstdc++-devel-static
BuildRequires: libgdal-devel
BuildRequires: libassimp-devel
BuildRequires: libminizip-devel
BuildRequires: libpoly2tri-devel
BuildRequires: ctest

%description
An audio-visual library supports processing audio and video files, a graphics
library can load a variety 3D mesh file formats into a generic in-memory
representation, and the core library of Gazebo Common contains functionality
that spans Base64 encoding/decoding to thread pools.

%package -n libgz-common%soversion
Summary: Library libgz-common of gz-common
Group: System/Libraries

%description -n libgz-common%soversion
This package contains libgz-common, part of gz-common.

%package -n libgz-common-av%soversion
Summary: Library libgz-common-av of gz-common
Group: System/Libraries

%description -n libgz-common-av%soversion
This package contains libgz-common-av, part of gz-common.

%package -n libgz-common-events%soversion
Summary: Library libgz-common-events of gz-common
Group: System/Libraries

%description -n libgz-common-events%soversion
This package contains libgz-common-events, part of gz-common.

%package -n libgz-common-geospatial%soversion
Summary: Library libgz-common-geospatial of gz-common
Group: System/Libraries

%description -n libgz-common-geospatial%soversion
This package contains libgz-common-geospatial, part of gz-common.

%package -n libgz-common-graphics%soversion
Summary: Library libgz-common-graphics of gz-common
Group: System/Libraries

%description -n libgz-common-graphics%soversion
This package contains libgz-common-graphics, part of gz-common.

%package -n libgz-common-io%soversion
Summary: Library libgz-common-io of gz-common
Group: System/Libraries

%description -n libgz-common-io%soversion
This package contains libgz-common-io, part of gz-common.

%package -n libgz-common-profiler%soversion
Summary: Library libgz-common-profiler of gz-common
Group: System/Libraries

%description -n libgz-common-profiler%soversion
This package contains libgz-common-profiler, part of gz-common.

%package -n libgz-common-testing%soversion
Summary: Library libgz-common-testing of gz-common
Group: System/Libraries

%description -n libgz-common-testing%soversion
This package contains libgz-common-testing, part of gz-common.

%package -n libgz-common-devel
Summary: Development files for gz-common
Group: Development/C++

%description -n libgz-common-devel
This package contains development files of gz-common.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -GNinja \
    -Wno-dev \
    #
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc AUTHORS README.md
%_prefix/libexec/gz/gz-common/gz_remotery_vis
%_datadir/gz/gz-common

%files -n libgz-common%soversion
%_libdir/libgz-common.so.%soversion
%_libdir/libgz-common.so.%version

%files -n libgz-common-av%soversion
%_libdir/libgz-common-av.so.%soversion
%_libdir/libgz-common-av.so.%version

%files -n libgz-common-events%soversion
%_libdir/libgz-common-events.so.%soversion
%_libdir/libgz-common-events.so.%version

%files -n libgz-common-geospatial%soversion
%_libdir/libgz-common-geospatial.so.%soversion
%_libdir/libgz-common-geospatial.so.%version

%files -n libgz-common-graphics%soversion
%_libdir/libgz-common-graphics.so.%soversion
%_libdir/libgz-common-graphics.so.%version

%files -n libgz-common-io%soversion
%_libdir/libgz-common-io.so.%soversion
%_libdir/libgz-common-io.so.%version

%files -n libgz-common-profiler%soversion
%_libdir/libgz-common-profiler.so.%soversion
%_libdir/libgz-common-profiler.so.%version

%files -n libgz-common-testing%soversion
%_libdir/libgz-common-testing.so.%soversion
%_libdir/libgz-common-testing.so.%version

%files -n libgz-common-devel
%_includedir/gz/common%soversion
%_libdir/libgz-common*.so
%_cmakedir/gz-common
%_cmakedir/gz-common-all
%_cmakedir/gz-common-av
%_cmakedir/gz-common-events
%_cmakedir/gz-common-geospatial
%_cmakedir/gz-common-graphics
%_cmakedir/gz-common-io
%_cmakedir/gz-common-profiler
%_cmakedir/gz-common-testing
%_pkgconfigdir/gz-common.pc
%_pkgconfigdir/gz-common-av.pc
%_pkgconfigdir/gz-common-events.pc
%_pkgconfigdir/gz-common-geospatial.pc
%_pkgconfigdir/gz-common-graphics.pc
%_pkgconfigdir/gz-common-io.pc
%_pkgconfigdir/gz-common-profiler.pc
%_pkgconfigdir/gz-common-testing.pc

%changelog
* Mon Aug 10 2026 Pavel Petrykin <silverducks@altlinux.org> 7.3.0-alt1
- New version.

* Tue Dec 23 2025 Pavel Petrykin <silverducks@altlinux.org> 7.0.0-alt1
- New version.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.

* Wed Nov 22 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.0-alt3.1
- BR: remove stbi (not used).

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
