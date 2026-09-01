%define _unpackaged_files_terminate_build 1
%global sover 3
%define libname lib%name%sover

Name:    lexbor
Version: 3.0.0
Release: alt1

Summary: Development of an open source HTML renderer library
License: Apache-2.0
Group:   System/Libraries
URL:     https://lexbor.com
VCS:     https://github.com/lexbor/lexbor

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
Lexbor is development of an open source HTML Renderer library.

%package -n %libname
Summary: Lexbor HTML renderer library
Group:   System/Libraries

%description -n %libname
Lexbor is development of an open source HTML Renderer library.
This package contains the shared library.

%package -n liblexbor-devel
Summary: Development files for lexbor
Group:   Development/C
Requires: %libname = %EVR

%description -n liblexbor-devel
Development headers, CMake and pkg-config files for lexbor.

%prep
%setup

%build
%cmake \
    -DLEXBOR_BUILD_STATIC=OFF

%cmake_build

%install
%cmake_install

%files -n %libname
%doc LICENSE README.md
%_libdir/liblexbor.so.%{sover}*

%files -n liblexbor-devel
%_includedir/lexbor/
%_libdir/liblexbor.so
%dir %_libdir/cmake
%_libdir/cmake/lexbor/
%_libdir/pkgconfig/lexbor.pc

%changelog
* Tue Sep 01 2026 Sergey Palcheh <minergenon@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
