%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: musacad
Version: 0.5.0
Release: alt1

Summary: High-performance, multi-threaded 2D CAD in modern C++23
License: LGPL-3.0-or-later
Group: Engineering
Url: https://github.com/MusaCAD/MusaCAD

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(vulkan)
BuildRequires: /usr/bin/glslc
BuildRequires: /usr/bin/glslangValidator

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

Requires: libredwg

ExcludeArch: %ix86

%description
Musa CAD is a fast, modern 2D CAD application. It mirrors AutoCAD's UI layout,
command line, and classic shortcuts, on a multi-threaded, GPU-accelerated,
data-oriented core targeting a smooth 144 Hz+ viewport.

Features:

* 2D drafting: lines, polylines, circles, arcs, rectangles, hatches;
* Full Modify suite: move, copy, rotate, mirror, scale, offset, trim, fillet, array;
* Dimensions, leaders, and text (TrueType and stroke fonts);
* Blocks, layers, linetypes, and a Properties palette with MATCHPROP;
* Dynamic input on the canvas and multi-document tabs;
* DXF read/write built in; DWG via an external converter;
* PDF / print plotting with true vector output.

%prep
%setup
sed -i "s|assets/branding/||" README.md
sed -i "s|assets/screenshots/||g" README.md
%patch -p1

%build
%cmake \
       -DCMAKE_BUILD_TYPE=Release \
       -DMUSACAD_BUILD_DEV_TOOLS=OFF \
%if_with check
       -DMUSACAD_BUILD_TESTS=ON
%else
       -DMUSACAD_BUILD_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%doc assets/branding/musacad_logo.svg assets/screenshots/*.png
%doc CONTRIBUTORS.md docs
%doc LICENSE COPYING COPYING.LESSER
%_bindir/musacad_app
%_desktopdir/org.musacad.MusaCAD.desktop
%_iconsdir/hicolor/scalable/apps/org.musacad.MusaCAD.svg
%_datadir/metainfo/org.musacad.MusaCAD.metainfo.xml

%changelog
* Mon Sep 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
