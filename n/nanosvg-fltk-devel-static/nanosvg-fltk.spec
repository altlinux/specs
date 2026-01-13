Name:    nanosvg-fltk-devel-static
Version: 2023.12.02
Release: alt1
Summary: Nano SVG fltk
License: GPL-3.0-only
Group:   System/Base
URL:     https://github.com/fltk/nanosvg
VCS:     https://github.com/fltk/nanosvg
Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

%global optflags_lto %optflags -ffat-lto-objects

%description
NanoSVG is a simple stupid single-header-file SVG parse.
The output of the parser is a list of cubic bezier shapes.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libexecdir/libnanosvg.a
%_libexecdir/libnanosvgrast.a
%_includedir/nanosvg/nanosvg.h
%_includedir/nanosvg/nanosvgrast.h
%_libexecdir/cmake/NanoSVG/NanoSVGConfig.cmake
%_libexecdir/cmake/NanoSVG/NanoSVGConfigVersion.cmake
%_libexecdir/cmake/NanoSVG/NanoSVGTargets-noconfig.cmake
%_libexecdir/cmake/NanoSVG/NanoSVGTargets.cmake

%changelog
* Thu Dec 04 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 2023.12.02-alt1
- Initial build.
