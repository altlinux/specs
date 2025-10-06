%define soname 0

Name: blend2d
Version: 0.21.0
Release: alt1

Summary: 2D Vector Graphics Engine

License: Zlib
Group: System/Libraries

Url: https://blend2d.com
Vcs: https://github.com/blend2d/blend2d

Source: %name-%version.tar
#https://blend2d.com/download/blend2d-%version.tar.gz

#Add soname to library
Patch: CMakeLists-0.21.0-alt-fixes.patch

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
Blend2D is a high performance 2D vector graphics engine written
in C++ and released under the Zlib license. The engine utilizes
a built-in JIT compiler to generate optimized pipelines at runtime
that take the advantage of host CPU features and is capable of
using multiple threads to boost the performance beyond the
possibilities of single-threaded rendering. Blend2D can render
rectangles, simple shapes, geometries composed of lines and Bezier
curves, and text. The 2D pipeline supports pixel composition, opacity
control, and styles such as solid colors, gradients, and images.

%package -n lib%name%soname
Group: System/Libraries
Summary: %name library
%description -n lib%name%soname
2D Vector Graphics Engine.

%package devel
Group:Development/C++
Summary: Development files for %name
%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n lib%name%soname
%_libdir/lib%name.so.%soname

%files devel
%_libdir/lib%name.so
%_includedir/%name
%_includedir/*.h
%_libdir/cmake/%name

%changelog
* Mon Oct 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.21.0-alt1
- 0.20.0 -> 0.21.0

* Sun Oct 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.20.0-alt1
- Initial build for ALT Linux.
