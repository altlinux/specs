# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%_tune_parallel_build_by_procsize 3072

Name: PrusaSlicer
Summary: G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
Version: 2.9.4
Release: alt5
License: AGPL-3.0-only
Group: Engineering
URL: https://www.prusa3d.com/prusaslicer/
VCS: https://github.com/prusa3d/PrusaSlicer

# Source-url: https://github.com/prusa3d/PrusaSlicer/archive/refs/tags/version_%version.tar.gz
Source: %name-%version.tar

ExcludeArch: %ix86

Provides: prusa-slicer

Patch1: PrusaSlicer-2.9.0-pr13081-cgal6.0.patch
Patch2: PrusaSlicer-2.9.1-pr14214-egl-support.patch
Patch10: PrusaSlicer-2.9.1-glad-system.patch
Patch11: PrusaSlicer-2.9.1-glad-cmake-new.patch
Patch20: PrusaSlicer-2.9.4-adapting-to-eigen5.patch
Patch21: PrusaSlicer-2.9.4-occt_wrapper-make-fix.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-intro
BuildRequires: libblosc-devel
BuildRequires: cereal-devel
BuildRequires: cgal-devel >= 5.6
BuildRequires: cmake
BuildRequires: eigen3 >= 3.4

BuildRequires: gcc-c++
BuildRequires: libgtest >= 1.7
BuildRequires: ctest
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
BuildRequires: libbgcode
BuildRequires: libbgcode-devel
BuildRequires: libjpeg-devel
BuildRequires: opencascade-devel
BuildRequires: nanosvg-devel
BuildRequires: openssl-devel
BuildRequires: heatshrink-devel

BuildRequires: libwebkit2gtk4.1-devel
BuildRequires: catch-devel
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
PrusaSlicer takes 3D models (STL, OBJ, AMF) and converts them into G-code
instructions for FFF printers or PNG layers for mSLA 3D printers. It's
compatible with any modern printer based on the RepRap toolchain, including
all those based on the Marlin, Prusa, Sprinter and Repetier firmware.
It also works with Mach3, LinuxCNC and Machinekit controllers.

%prep
%setup -n %name-%version
sed -i 's/\r$//' src/slic3r/GUI/GCodeViewer.cpp
sed -i 's/\r$//' src/slic3r/GUI/GLCanvas3D.cpp
sed -i 's/\r$//' src/slic3r/GUI/Gizmos/GLGizmoBase.cpp
%autopatch -p1

# this is not prusaslicer specific, space mouse users install it themselves
rm resources/udev/90-3dconnexion.rules
# Generating gl initialization via glad2
rm src/libvgcode/glad/include/KHR/khrplatform.h
rm src/libvgcode/glad/include/glad/gl.h
rm src/libvgcode/glad/include/glad/gles2.h
rm src/libvgcode/glad/src/gl.c
rm src/libvgcode/glad/src/gles2.c

GDIR="bundled_deps/glad"
mkdir -p "$GDIR"
glad --reproducible \
  --out-path="$GDIR" \
  --api='gl:compatibility=4.6' \
  --extensions='GL_ARB_compatibility,GL_ARB_framebuffer_object,GL_EXT_framebuffer_blit,GL_EXT_framebuffer_multisample,GL_EXT_framebuffer_object,GL_EXT_texture_compression_s3tc,GL_EXT_texture_filter_anisotropic,GL_KHR_debug' \
  c --loader

glad --reproducible \
  --out-path="$GDIR" \
  --api='gles2=3.2' \
  --extensions='GL_EXT_texture_compression_s3tc,GL_EXT_texture_filter_anisotropic,GL_KHR_debug' \
  c --loader

#sed -i 's|slic3r_jobs_tests.cpp||' tests/slic3rutils/CMakeLists.txt
# Disable libseqarrange_tests as it looks like they are stuck in an infinite
# loop somewhere in Z3_solver_get_model
sed -i 's|SLIC3R_BUILD_TESTS|FALSE|' src/libseqarrange/CMakeLists.txt

%build
# sse2 flags for 32-bit: see gh#prusa3d/PrusaSlicer#3781
%ifarch %ix86
  export CFLAGS="%optflags -mfpmath=sse -msse2"
  export CXXFLAGS="$CFLAGS"
%endif

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
  -DCMAKE_SUPPRESS_DEVELOPER_WARNINGS=ON
%cmake_build

%install
%cmake_install

%check
pushd %_cmake__builddir
ctest --output-on-failure
popd

%files
%_bindir/prusa-gcodeviewer
%_bindir/prusa-slicer
%dir %_libdir/prusaslicer
%_libdir/prusaslicer/OCCTWrapper.so
%_datadir/PrusaSlicer
%_desktopdir/PrusaGcodeviewer.desktop
%_desktopdir/PrusaSlicer.desktop
%_iconsdir/hicolor/*/apps/PrusaSlicer*
%doc README.md doc/

%changelog
* Mon Jun 08 2026 Anton Midyukov <antohami@altlinux.org> 2.9.4-alt5
- Rebuild with libwebkit2gtk4.1-devel.

* Thu Feb 12 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 2.9.4-alt4
- Add memory limit 3072 per thread.

* Tue Jan 20 2026 Arseniy Romenskiy <romenskiy@altlinux.org> 2.9.4-alt3
- Recompiled using dynamic libraries.

* Sun Jan 18 2026 Anton Midyukov <antohami@altlinux.org> 2.9.4-alt2
- Rebuild with shared library qhullcpp instead static.

* Thu Dec 04 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 2.9.4-alt1
- new version (2.9.4)

* Thu Apr 28 2022 Anton Midyukov <antohami@altlinux.org> 2.4.2-alt1
- new version (2.4.2) with rpmgs script

* Sun Apr 24 2022 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- initial build for ALT Sisyphus (Closes: 42501)
