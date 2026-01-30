%define sover 0

Name:    nanosvg
Version: 2023.12.02
Release: alt2
Summary: Nano SVG fltk
License: AGPL-3.0-only
Group:   System/Base
URL:     https://github.com/fltk/nanosvg
VCS:     https://github.com/fltk/nanosvg
Source:  %name-%version.tar

Patch1: 0001-Add-versioning-for-future-updates.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

%description
NanoSVG is a simple stupid single-header-file SVG parse.
The output of the parser is a list of cubic bezier shapes.

%package devel
Summary: Nano SVG fltk
Group: System/Base
Conflicts: nanosvg-fltk-devel-static < %EVR

%description devel
NanoSVG is a simple stupid single-header-file SVG parse.
The output of the parser is a list of cubic bezier shapes.

%prep
%setup
%patch1 -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
%cmake_install

%files
%_libdir/libnanosvg.so.%sover
%_libdir/libnanosvgrast.so.%sover

%files devel
%_libdir/libnanosvg.so
%_libdir/libnanosvgrast.so
%_includedir/nanosvg/nanosvg.h
%_includedir/nanosvg/nanosvgrast.h
%_libexecdir/cmake/NanoSVG/NanoSVGConfig.cmake
%_libexecdir/cmake/NanoSVG/NanoSVGConfigVersion.cmake
%_libexecdir/cmake/NanoSVG/NanoSVGTargets-noconfig.cmake
%_libexecdir/cmake/NanoSVG/NanoSVGTargets.cmake

%changelog
* Tue Jan 20 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 2023.12.02-alt2
- Build as shared libraries instead static (Closes: 57537)
- Fix license (Closes: 57536).
- Rename nanosvg-fltk-devel-static to nanosvg.

* Thu Dec 04 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 2023.12.02-alt1
- Initial build.
