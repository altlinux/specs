%define _unpackaged_files_terminate_build 1
# Upstream has no soversion; use major version as %%abiversion (Shared Libs Policy).
%global abiversion 1

Name: gpupixel
Version: 1.3.1
Release: alt1
Summary: Realtime image filter engine based on GPU
License: Apache-2.0
Group: Graphics
Url: https://github.com/pixpark/gpupixel

Source0: %name-%version.tar
Patch0: %name-%version-alt-linux.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xi)
BuildRequires: libGLU-devel
BuildRequires: libGL-devel

%description
GPUPixel is a high-performance, cross-platform image and video filter
library. Built with C++ and OpenGL ES, it provides beauty filters and
supports multiple platforms. This package is built without the proprietary
mars-face-kit face detector (no Linux binary in the release).

%package -n lib%{name}%{abiversion}
Summary: Shared library for %name
Group: System/Libraries
Requires: lib%{name}-common = %EVR

%description -n lib%{name}%{abiversion}
Shared libraries for %name (ABI %abiversion).

%package -n lib%{name}-common
Summary: Common data files for %name
Group: System/Libraries
BuildArch: noarch

%description -n lib%{name}-common
ABI-independent resources for %name (lookup textures and models).

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%{name}%{abiversion} = %EVR

%description -n lib%{name}-devel
Header files and development libraries for %name.

%prep
%setup
%patch0 -p1

%build
%cmake \
  -DGPUPIXEL_ENABLE_FACE_DETECTOR=OFF \
  -DGPUPIXEL_BUILD_DESKTOP_DEMO=OFF
%cmake_build

%install
%cmakeinstall_std

%files -n lib%name%abiversion
%_libdir/libgpupixel.so.%abiversion
%_libdir/libgpupixel.so.%version

%files -n lib%name-common
%dir %_datadir/%name
%dir %_datadir/%name/res
%_datadir/%name/res/*
%dir %_datadir/%name/models
%_datadir/%name/models/*

%files -n lib%name-devel
%doc README.md CHANGELOG.md LICENSE
%_libdir/libgpupixel.so
%_includedir/gpupixel

%changelog
* Mon Aug 03 2026 Pavel Shilov <zerospirit@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
