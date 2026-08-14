Name:    artoolkitx
Version: 1.1.22
Release: alt1

Summary: artoolkitX: high-performance AR video, marker & texture tracking
License: LGPL-3.0-only
Group:   Graphics
URL:     https://www.artoolkitx.org
VCS:     https://github.com/artoolkitx/artoolkitx

Source: %name-%version.tar
Patch: artoolkitx-error.h-gcc15.patch
Patch1: artoolkitx-videoGStreamer-gcc15.patch
Patch2: artoolkitx-libdir.patch
Patch3: artoolkitx-march.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libopencv-devel libcurl-devel libjpeg-devel zlib-devel
BuildRequires: libGL-devel libGLU-devel libudev-devel libdc1394-devel
BuildRequires: libssl-devel gstreamer1.0-devel glib2-devel libSDL2-devel
BuildRequires: libsqlite3-devel

%description
artoolkitX  is a software development kit (SDK) consisting of libraries
and utilities that help developers implement the foundation of great
augmented and mixed reality applications. The SDK includes some examples
of applications that demonstrate the capabilities of artoolkitX.

%package -n libARX1
Summary: Shared library for artoolkitX
Group:   System/Libraries

%description -n libARX1
artoolkitX is an open-source software development kit for building
augmented and mixed reality applications. This package provides the
shared library (libARX) implementing video, marker and texture tracking.

%package -n libARX-devel
Summary: Development files for artoolkitX
Group:   Development/C++
Requires: libARX1 = %EVR

%description -n libARX-devel
artoolkitX is an open-source software development kit for building
augmented and mixed reality applications. This package provides the
header files, CMake configuration and development symlink needed to
build applications against libARX.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd Source
%cmake \
    -Wno-dev

%cmake_build

%install
cd Source
%cmake_install

%files
%doc LICENSE.txt README.md
%_bindir/artoolkitx_*

%files -n libARX1
%doc LICENSE.txt
%_libdir/libARX.so.1*

%files -n libARX-devel
%doc LICENSE.txt
%_includedir/ARX
%_libdir/libARX.so
%_libdir/ARX

%changelog
* Thu Aug 13 2026 Sergey Palcheh <minergenon@altlinux.org> 1.1.22-alt1
- Initial build for Sisyphus
