%define _unpackaged_files_terminate_build 1
%define sover 1

Name: plutovg
Version: 1.0.0
Release: alt1

Summary: Standalone 2D vector graphics library
License: MIT
Group: System/Libraries

Url: https://github.com/sammycage/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/sammycage/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: clang
BuildRequires: cmake
BuildRequires: lld
BuildRequires: llvm
BuildRequires: ninja-build

%description
PlutoVG is a standalone 2D vector graphics library in C.

Features:
   - Path Filling, Stroking and Dashing
   - Solid, Gradient and Texture Paints
   - Fonts and Texts
   - Clipping and Compositing
   - Transformations
   - Images

%package -n lib%name%sover
Summary: Standalone 2D vector graphics library
Group: System/Libraries

%description -n lib%name%sover
PlutoVG is a standalone 2D vector graphics library in C.

Features:
   - Path Filling, Stroking and Dashing
   - Solid, Gradient and Texture Paints
   - Fonts and Texts
   - Clipping and Compositing
   - Transformations
   - Images

%package -n lib%name-devel
Summary: Development files for PlutoVG
Group: Development/C

%description -n lib%name-devel
This package contains development files for PlutoVG.

%prep
%setup

%build
export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-GNinja
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/lib%name.so.%sover

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_cmakedir/%name

%changelog
* Fri Apr 04 2025 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux

