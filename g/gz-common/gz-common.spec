%define _unpackaged_files_terminate_build 1

Name:    gz-common
Version: 4.6.2
Release: alt1

Summary: Gazebo Common : AV, Graphics, Events, and much more
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/gazebosim/gz-common

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: gz-common-alt-fix-build.patch

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
BuildRequires: libavresample-devel
BuildRequires: libgts-devel
BuildRequires: libpostproc-devel
BuildRequires: libpcre2-devel
BuildRequires: libfreeimage-devel

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

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README.md
%_prefix/libexec/ignition/ignition-common*/ign_remotery_vis
%_datadir/ignition/ignition-common*

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%{name}-devel
%_includedir/ignition/common*
%_libdir/lib*.so
%_libdir/cmake/ignition-common*
%_libdir/pkgconfig/*.pc

%changelog
* Fri May 26 2023 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version.

* Thu May 18 2023 Andrey Cherepanov <cas@altlinux.org> 3.15.1-alt1
- Initial build for Sisyphus.
