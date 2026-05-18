%define _unpackaged_files_terminate_build 1
%define sover 0

Name: plutosvg
Version: 0.0.8
Release: alt1

Summary: Compact and efficient SVG rendering library
License: MIT
Group: System/Libraries

Url: https://github.com/sammycage/%name
Vcs: https://github.com/sammycage/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/sammycage/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: clang
BuildRequires: cmake
BuildRequires: libplutovg-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: ninja-build

%description
PlutoSVG is a compact and efficient SVG rendering library written in C. It is specifically designed for parsing and
rendering SVG documents embedded in OpenType fonts, providing an optimal balance between speed and minimal
memory usage. It is also suitable for rendering scalable icons.

%package -n lib%name%sover
Summary: Compact and efficient SVG rendering library
Group: System/Libraries

%description -n lib%name%sover
PlutoSVG is a compact and efficient SVG rendering library written in C. It is specifically designed for parsing and
rendering SVG documents embedded in OpenType fonts, providing an optimal balance between speed and minimal
memory usage. It is also suitable for rendering scalable icons.

%package -n lib%name-devel
Summary: Development files for PlutoSVG
Group: Development/C

%description -n lib%name-devel
This package contains development files for PlutoSVG.

%prep
%setup

%build
export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

sed -i 's/0.0.4/1.0.0/' CMakeLists.txt

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
%_pkgconfigdir/%name.pc

%changelog
* Tue May 19 2026 Nazarov Denis <nenderus@altlinux.org> 0.0.8-alt1
- New version 0.0.8.

* Thu Jul 03 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.7-alt1
- New version 0.0.7.

* Sat Apr 05 2025 Nazarov Denis <nenderus@altlinux.org> 0.0.6-alt1
- Initial build for ALT Linux


