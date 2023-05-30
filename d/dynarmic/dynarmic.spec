%define sover 6

Name: dynarmic
Version: 6.4.8
Release: alt1

Summary: A dynamic recompiler for ARM.
License: 0BSD
Group: System/Libraries

Url: https://github.com/merryhime/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/merryhime/%name/archive/refs/tags/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: boost-devel
BuildRequires: catch2-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libmcl-devel
BuildRequires: librobin-map-devel
BuildRequires: libxbyak-devel
BuildRequires: libzydis-devel

%description
A dynamic recompiler for ARM.

%package -n lib%name%sover
Summary: A dynamic recompiler for ARM.
Group: System/Libraries

%description -n lib%name%sover
A dynamic recompiler for ARM.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C++

%description -n lib%name-devel
Header files for lib%name

%prep
%setup

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DDYNARMIC_USE_PRECOMPILED_HEADERS:BOOL=FALSE
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE.txt README.md
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/cmake/%name
%_libdir/lib%name.so
%_includedir/%name

%changelog
* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 6.4.8-alt1
- Initial build for ALT Linux
