# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%def_without check
%_tune_parallel_build_by_procsize 3072

Name: SuperSlicer
Summary: A PrusaSlicer fork (which is a slic3r fork) (previously Slic3r++)
Version: 2.7.61.10
Release: alt5
License: AGPL-3.0-only
Group: Engineering
URL: https://superslicer.net
VCS: https://github.com/supermerill/SuperSlicer

Source: %name-%version.tar

ExcludeArch: %ix86

Provides: super-slicer = %EVR

Patch1: 0001-Fix-libexpat-build-config.patch
Patch2: 0011-Fix-GLEW-init.patch
Patch3: 0005-cgal6.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-intro
BuildRequires: libblosc-devel
BuildRequires: cereal-devel
BuildRequires: cgal-devel >= 5.6
BuildRequires: cmake
BuildRequires: eigen3 >= 3

BuildRequires: gcc-c++
BuildRequires: libgtest >= 1.7
BuildRequires: boost-devel
BuildRequires: boost-asio-devel
BuildRequires: boost-atomic-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-geometry-devel
BuildRequires: boost-iostreams-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-log-devel
BuildRequires: boost-polygon-devel
BuildRequires: boost-regex-devel
BuildRequires: boost-system-devel
BuildRequires: boost-thread-devel
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libnlopt-devel
BuildRequires: openexr-devel
BuildRequires: openvdb-devel >= 5
BuildRequires: tbb-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: pkgconfig(libudev)
BuildRequires: libdbus-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgmpxx-devel
BuildRequires: libglew-devel
BuildRequires: libqhull-devel
BuildRequires: libbgcode-devel
BuildRequires: libbgcode
BuildRequires: libjpeg-devel
BuildRequires: opencascade-devel
BuildRequires: nanosvg-devel
BuildRequires: openssl-devel
BuildRequires: heatshrink-devel

BuildRequires: libwebkit2gtk4.1-devel
%if_with check
BuildRequires: catch2-devel
BuildRequires: ctest
%endif
BuildRequires: libpcre2-devel
BuildRequires: libffi-devel
BuildRequires: bzlib-devel
BuildRequires: libbrotli-devel
BuildRequires: libsystemd-devel
BuildRequires: nlohmann-json-devel
BuildRequires: libz3-devel
BuildRequires: boost-beast-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libmount-devel
BuildRequires: libmount-devel-static

BuildRequires: python3-module-glad2

%description
SuperSlicer takes 3D models (STL, OBJ, AMF) and converts them into G-code
instructions for FFF printers or PNG layers for mSLA 3D printers.
It's compatible with any modern printer based on the RepRap toolchain which is
running a firmware based on Marlin, Prusa, Klipper, etc.

%prep
%setup -n %name-%version
sed -i 's/\r$//' src/slic3r/GUI/GCodeViewer.cpp
sed -i 's/\r$//' src/slic3r/GUI/GLCanvas3D.cpp
sed -i 's/\r$//' src/slic3r/GUI/Gizmos/GLGizmoBase.cpp
%autopatch -p1
# this is not prusaslicer specific, space mouse users install it themselves
rm resources/udev/90-3dconnexion.rules

%build
# -DSLIC3R_FHS=1 - Enable FHS layout instead of installing things into the resources directory
# -DSLIC3R_WX_STABLE=1 - Allow use of wxGTK version 3.0 instead of 3.1.
%cmake \
  -DSLIC3R_FHS=1 \
  -DSLIC3R_GTK=3 \
  -DSLIC3R_EGL=ON \
  -DSLIC3R_WX_STABLE=1 \
  -DSLIC3R_BUILD_TESTS=1 \
  -DCMAKE_BUILD_TYPE=Release \
  -DOPENVDB_FIND_MODULE_PATH=%_libdir/cmake/OpenVDB \
  -DWITH_WERROR=OFF \
%if_with check
  -DBUILD_TESTING=ON \
  -DSLIC3R_BUILD_TESTS=ON \
%else
  -DBUILD_TESTING=OFF \
  -DSLIC3R_BUILD_TESTS=OFF \
%endif
  -DCMAKE_SUPPRESS_DEVELOPER_WARNINGS=ON

%cmake_build
%cmake_build -t gettext_po_to_mo

%install
%cmake_install

find %buildroot/%_datadir/%name/localization/ -name \*.po -delete
find %buildroot/%_datadir/%name/localization/ -name settings.ini -delete
rm -r %buildroot/%_libexecdir/cmake
rm %buildroot/%_libexecdir/libangelscript.a
rm %buildroot/%_includedir/angelscript.h

%check
pushd %_cmake__builddir
ctest --output-on-failure
popd

%files
%_bindir/superslicer
%_bindir/superslicer-gcodeviewer
%dir %_libdir/superslicer
%_libdir/superslicer/OCCTWrapper.so
%_datadir/SuperSlicer/
%_desktopdir/SuperSlicer-Gcodeviewer.desktop
%_desktopdir/SuperSlicer.desktop
%_iconsdir/hicolor/*/apps/SuperSlicer*
%doc README.md doc/

%changelog
* Mon Jun 08 2026 Anton Midyukov <antohami@altlinux.org> 2.7.61.10-alt5
- Rebuild with libwebkit2gtk4.1-devel.

* Thu Feb 12 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 2.7.61.10-alt4
- Add memory limit 3072 per thread.

* Tue Jan 20 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 2.7.61.10-alt3
- Recompiled using dynamic libraries.

* Sun Jan 18 2026 Anton Midyukov <antohami@altlinux.org> 2.7.61.10-alt2
- Rebuild with shared library qhullcpp instead static.

* Mon Dec 22 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 2.7.61.10-alt1
- Initial build.
