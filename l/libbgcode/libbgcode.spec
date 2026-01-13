%define name_orig LibBGCode
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name:    libbgcode
Version: 0.0
Release: alt1
Summary: Prusa Block & Binary G-code reader / writer / converter
License: GPL-3.0-only
Group:   System/Base
URL:     https://github.com/prusa3d/libbgcode
VCS:     https://github.com/prusa3d/libbgcode
Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libgtkmm3-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: heatshrink
BuildRequires: heatshrink-devel-static
BuildRequires: boost-devel
BuildRequires: boost-beast-devel
BuildRequires: catch-devel
BuildRequires: zlib-devel
BuildRequires: libstdc++-devel
BuildRequires: glibc-devel

%description
Prusa Block & Binary G-code reader / writer / converter

%package devel-static
Summary: Prusa Block & Binary G-code reader / writer / converter
Group: System/Base

%description devel-static
Prusa Block & Binary G-code reader / writer / converter

%prep
%setup

%build
%cmake #--preset default -DLibBGCode_BUILD_DEPS=ON
%cmake_build

%install
%cmake_install

%files
%_bindir/bgcode

%files devel-static
%_includedir/%name_orig/
%_libdir/cmake/%name_orig/
%_libdir/libbgcode_binarize.a
%_libdir/libbgcode_convert.a
%_libdir/libbgcode_core.a

%changelog
* Thu Nov 27 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.0-alt1
- Initial build.
