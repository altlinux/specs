%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed
%define git %nil
%define kern_dir scripts/addons_core/cycles/lib

%def_with docs

%ifarch aarch64 x86_64 %e2k
%def_with embree
%else
%def_without embree
%endif

%ifarch x86_64
%def_with cuda
%def_with hiprt
%else
%def_without cuda
%def_without hiprt
%endif

%ifarch x86_64 aarch64 loongarch64
%def_with mold
%else
%def_without mold
%endif

%ifarch x86_64 aarch64
%def_with openpgl
%def_with usd
%def_with oidn
%else
%def_without openpgl
%def_without usd
%def_without oidn
%endif

%ifarch %e2k
# error: cpio archive too big - 4690M
%define optflags_debug -g0
%endif

# https://devtalk.blender.org/t/does-blender-use-jemalloc-and-or-tbb/13388/10
%def_with jemalloc

%ifarch x86_64 aarch64
# HIP should work on other 64-bit arches but clr needs to get built first
%def_with hip
%else
%def_without hip
%endif

%ifarch x86_64
# OneAPI/SYCL for Intel GPU support
%def_with oneapi
%else
%def_without oneapi
%endif

%if_with oneapi
# oneapi library is built with SYCL compiler without debug info
%filter_from_requires /libcycles_kernel_oneapi_aot\.so/d
%add_verify_elf_skiplist %_libdir/libcycles_kernel_oneapi_aot.so
%add_debuginfo_skiplist %_libdir/libcycles_kernel_oneapi_aot.so
%endif

Name: blender
Version: 4.5.11
Release: alt1
Summary: 3D modeling, animation, rendering and post-production
License: GPL-3.0-or-later
Group: Graphics
URL: https://www.blender.org
VCS: https://projects.blender.org/blender/blender.git

# Blender doesn't officially support 32-bit build since 2.80. See also:
# https://developer.blender.org/T67184
ExcludeArch: %ix86 %arm

Source: %name-%version.tar
# git lfs from blender git release
Source1: blender-lfs-%version.tar
# freedesktop thumbnailer file
Source2: blender.thumbnailer
# cheryy-picked upstream commits
Patch1: %name-%version-%release.patch

Patch21: blender-2.77-alt-enable-localization.patch
Patch22: blender-4.5-eigen-fix-build.patch
Patch23: blender-2.80-alt-use-system-glog.patch
Patch24: blender-2.90-alt-non-x86_64-linking.patch

# needed for static clang libs
Patch30: blender-alt-fix-clang-linking.patch
Patch31: blender-alt-osl-shader-dir.patch

# needed for dynamic clang libs
Patch32: blender-4.1-alt-use-libclang.patch
Patch33: blender-alt-cycles-aarch64-hip-cuda-fix.patch

# need to send this to upstream:
# gfx900 needs -O1 on Linux too, otherwise it will fail
# https://github.com/ROCm/llvm-project/issues/58#issuecomment-2041433424
Patch34: blender-cycles-fix-hip-kernels.patch
# FFmpeg 8.0 compatibility (AV_INPUT_BUFFER_MIN_SIZE removed)
Patch35: blender-4.5-ffmpeg-8.0.patch
# ALT Linux: install oneapi library to /usr/lib64 instead of /usr/share/blender/lib
Patch40: blender-4.5-alt-oneapi-libdir.patch
Patch2000: blender-e2k-support.patch

# Required since the io_scene_gltf2 addon loads libdraco.so at runtime
# using cdll.LoadLibrary and relies on it for
# Draco mesh compression/decompression.
Requires: libdraco

BuildRequires(pre): rpm-build-python3
BuildRequires: boost-filesystem-devel boost-locale-devel boost-wave-devel boost-python3-devel
BuildRequires: cmake gcc-c++
BuildRequires: ninja-build /proc
BuildRequires: libGLEW-devel libXi-devel
BuildRequires: libavdevice-devel libavformat-devel libavfilter-devel libswresample-devel
BuildRequires: libfftw3-devel >= 3.3.9 pipewire-jack-libs-devel libopenal-devel libsndfile-devel
BuildRequires: libjpeg-devel pkgconfig(libopenjp2) libpng-devel libtiff-devel libpcre-devel libswscale-devel libxml2-devel
BuildRequires: liblzo2-devel
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libopenimageio-devel
BuildRequires: libopencolorio-devel
BuildRequires: openexr-devel
BuildRequires: imath-devel
BuildRequires: libpugixml-devel
BuildRequires: libglog-devel libgflags-devel eigen3-devel
BuildRequires: libXxf86vm-devel libXrender-devel
BuildRequires: tbb-devel
BuildRequires: libfreetype-devel
# Remove following dependency when libopenjpeg2.0-devel is fixed
BuildRequires: openjpeg-tools2.0
BuildRequires: alembic-devel
BuildRequires: openvdb-devel libblosc-devel
BuildRequires: libgomp-devel
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: libharu-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libpotrace-devel
BuildRequires: openshadinglanguage-devel
BuildRequires: opensubdiv-devel
BuildRequires: libzstd-devel
BuildRequires: libepoxy-devel
BuildRequires: libwayland-egl-devel wayland-protocols libwayland-cursor-devel libxkbcommon-devel libdecor-devel
BuildRequires: libvulkan-devel libshaderc-devel
BuildRequires: libspnav-devel
BuildRequires: libwebp-devel
BuildRequires: openxr-devel
BuildRequires: MaterialX-devel
BuildRequires: libmanifold-devel libClipper2-devel libassimp-devel
BuildRequires: libdraco-devel

%if_with oneapi
BuildRequires: intel-ocloc
# Intel GPU (OneAPI/SYCL) support
BuildRequires: libsycl-devel libze-devel
BuildRequires: clang-dpcpp-devel llvm-dpcpp-devel
BuildRequires: clang-dpcpp-tools libigc2
%endif

%ifarch aarch64
BuildRequires: sse2neon-devel
%endif

%if_with embree
BuildRequires: embree-devel
%endif

%if_with jemalloc
BuildRequires: libjemalloc-devel
%endif

%if_with docs
BuildRequires: /usr/bin/doxygen
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink python3-module-sphinx_rtd_theme
%endif

%if_with hip
BuildRequires: hip-devel
%endif

%if_with hiprt
BuildRequires: hiprt-devel clang-rocm-devel
%endif

%if_with openpgl
BuildRequires: openpgl-devel
%endif

%if_with usd
BuildRequires: OpenUSD-devel
%endif

%if_with cuda
BuildRequires: nvidia-cuda-devel
# CUDA 12.x nvcc cannot parse GCC 15 <type_traits> (new __is_pointer
# and __is_volatile builtins). Fall back to gcc-14 as the CUDA host
# compiler on Sisyphus (GCC 15); older branches keep the default GCC.
# %_priority_distbranch lives in /usr/lib/rpm/macros (read by rpm 4.13)
# but legacy rpmbuild 4.0.4 does not load it; shell out to `rpm --eval`.
%if "%(rpm --eval '%%_priority_distbranch' 2>/dev/null)" == "sisyphus"
BuildRequires: gcc14-c++
%endif
# .cubin files are ELF files but we still don't know how
# to handle them.
%add_verify_elf_skiplist %_datadir/%name/*/%kern_dir/*.cubin
%endif

%if_with oidn
BuildRequires: openimagedenoise-devel
%endif

%if_with mold
BuildRequires: mold
%endif

Requires: python3-module-numpy

%add_python3_path %_datadir/%name/scripts
%add_python3_req_skip _bpy
%add_python3_req_skip _bpy_path
%add_python3_req_skip _cycles
%add_python3_req_skip _freestyle
%add_python3_req_skip bgl
%add_python3_req_skip blend
%add_python3_req_skip blf
%add_python3_req_skip idprop.types
%add_python3_req_skip gpu
%add_python3_req_skip io_scene_gltf2.blender.com
%add_python3_req_skip io_scene_gltf2.blender.exp
%add_python3_req_skip io_scene_gltf2.io.com
%add_python3_req_skip io_scene_gltf2.io.exp
%add_python3_req_skip mathutils
%add_python3_req_skip mathutils.bvhtree
%add_python3_req_skip mathutils.geometry
%add_python3_req_skip mathutils.noise
%add_python3_req_skip oscurart_tools.files
%add_python3_req_skip oscurart_tools.mesh
%add_python3_req_skip oscurart_tools.object
%add_python3_req_skip oscurart_tools.render
%add_python3_req_skip setuptools
%add_python3_req_skip bmesh
%add_python3_req_skip bpy.app.handlers
%add_python3_req_skip bpy.app.translations
%add_python3_req_skip bpy.props
%add_python3_req_skip bpy.types

AutoProv: no

Obsoletes: %name-i18n

%description
Fully integrated creation suite, offering a broad range of essential
tools for the creation of 3D content, including modeling, uv-mapping,
texturing, rigging, skinning, animation, particle and other simulation,
scripting, rendering, compositing, post-production and game creation

%description -l ru_RU.UTF-8
Полностью интегрированный пакет разработки, предлагающий широкий
выбор инструментов необходимых для создания 3D-графики. Включает
средства моделирования, анимации, рендеринга, постобработки видео,
а также создания интерактивных игр. Пакет имеет такие функции,
как динамика твердых тел, жидкостей и мягких тел, систему горячих
клавиш, большое количество легко доступных расширений, написанных
на языке Python.

%package doc
Summary: Documentation for Blender
Group: Documentation
BuildArch: noarch

%description doc
Fully integrated creation suite, offering a broad range of essential
tools for the creation of 3D content, including modeling, uv-mapping,
texturing, rigging, skinning, animation, particle and other simulation,
scripting, rendering, compositing, post-production and game creation.

This package contains documentation for Blender.

%description doc -l ru_RU.UTF-8
Полностью интегрированный пакет разработки, предлагающий широкий
выбор инструментов необходимых для создания 3D-графики. Включает
средства моделирования, анимации, рендеринга, постобработки видео,
а также создания интерактивных игр. Пакет имеет такие функции,
как динамика твердых тел, жидкостей и мягких тел, систему горячих
клавиш, большое количество легко доступных расширений, написанных
на языке Python.

Данный пакет содержит документацию для Blender.

%if_with hip
%package cycles-hip-kernels
Summary: Cycles precompiled binaries for HIP
Group: System/Libraries
Requires: %name = %EVR, hip-runtime-amd

%description cycles-hip-kernels
Precompiled GPU binaries for GPU accelerated rendering with Cycles on various
graphics cards.

This package contains binaries for AMD GPUs to use with HIP.
%endif

%if_with hiprt
%package cycles-hiprt-kernels
Summary: Cycles precompiled binaries for HIPRT
Group: System/Libraries
Requires: %name = %EVR, hip-runtime-amd
# hiprt version hardcoded in sources
Requires: libhiprt = 2.5-alt2.4e650d5

%description cycles-hiprt-kernels
Precompiled GPU binaries for GPU accelerated rendering with Cycles on various
graphics cards.

This package contains binaries for AMD GPUs to use with HIPRT.
NOTE: If you use HIPRT you don't need HIP kernels and vice versa!

%endif

%if_with cuda
%package cycles-cuda-kernels
Summary: Cycles precompiled binaries for CUDA
Group: System/Libraries
Provides: blender-cycles-nvidia-kernels = %EVR
Obsoletes: blender-cycles-nvidia-kernels < %EVR
Requires: %name = %EVR, libcuda

%description cycles-cuda-kernels
Precompiled GPU binaries for GPU accelerated rendering with Cycles on various
graphics cards.

This package contains binaries for Nvidia GPUs to use with CUDA.
%endif

%prep
%setup -a1
%patch1 -p1

%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch31 -p1
%ifarch aarch64
# https://github.com/OE4T/meta-tegra/pull/1445
%patch33 -p1
mkdir -p /tmp/bits
cat >/tmp/bits/math-vector.h <<EOF
#include <bits/libm-simd-decl-stubs.h>
#undef __ADVSIMD_VEC_MATH_SUPPORTED
#undef __SVE_VEC_MATH_SUPPORTED
EOF
%endif
%patch34 -p1 -b .hip-kernels-fixes
%patch35 -p1
%if_with oneapi
%patch40 -p1
%endif

%ifarch %e2k
%patch2000 -p1
# lcc 1.25.15's EDG bug would fail building OPENVDB+TBB otherwise
sed -i "/-Werror=return-type/d" CMakeLists.txt
sed -i 's/"${CMAKE_C_COMPILER_VERSION}" VERSION_LESS/"100" VERSION_LESS/' CMakeLists.txt
sed -i 's/-freciprocal-math//' intern/cycles{,/kernel}/CMakeLists.txt
%endif

# Delete the bundled FindOpenJPEG to make find_package use the system version
# instead (the local version hardcodes the openjpeg version so it is not update
# proof)
rm -f build_files/cmake/Modules/FindOpenJPEG.cmake

# Remove bundled libraries which must not be used instead of system ones
rm -rf extern/{Eigen3,glew,lzo,gflags,glog,draco}

# overlay LFS files over git-lfs pointers (must be after all patches)
cp -rf blender-lfs-%version/* .
rm -rf blender-lfs-%version

%build
BUILD_DATE="$(stat -c '%%y' '%SOURCE0' | date -f - '+%%Y-%%m-%%d')"
BUILD_TIME="$(stat -c '%%y' '%SOURCE0' | date -f - '+%%H:%%M:%%S')"

# Explicitly use python3 in hashbangs.
pushd scripts/addons_core
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)
popd

# needed due to non-standard location of pcre.h header
%add_optflags -I%_includedir/pcre -DGLOG_USE_GLOG_EXPORT

%if_with hiprt
export ALTWRAP_LLVM_VERSION=rocm
%endif
%cmake -G Ninja \
%if_with hip
	-DWITH_CYCLES_HIP_BINARIES:BOOL=ON \
%endif #hip
%if_with cuda
	-DWITH_CYCLES_CUDA_BINARIES:BOOL=ON \
	-DWITH_CYCLES_CUDA_BUILD_SERIAL:BOOL=ON \
%if "%(rpm --eval '%%_priority_distbranch' 2>/dev/null)" == "sisyphus"
	-DCUDA_HOST_COMPILER=%_bindir/gcc-14 \
%endif
%endif #cuda
%if_with hiprt
	-DHIPRT_ROOT_DIR=%prefix \
	-DWITH_CYCLES_DEVICE_HIPRT:BOOL=ON \
	-DHIPRT_INCLUDE_DIR=%_includedir \
	-DHIP_LINKER_EXECUTABLE=%_bindir/clang++-rocm \
	-DHIPRT_COMPILER_PARALLEL_JOBS=4 \
%endif #hiprt
%if_with oneapi
	-DLEVEL_ZERO_ROOT_DIR=%prefix \
	-DSYCL_ROOT_DIR=%prefix/lib/llvm-dpcpp \
	-DOCLOC_INSTALL_DIR=%prefix \
	-DSYCL_OFFLINE_COMPILER_PARALLEL_JOBS=2 \
	-DWITH_CYCLES_DEVICE_ONEAPI:BOOL=ON \
	-DWITH_CYCLES_ONEAPI_BINARIES:BOOL=ON \
%endif #oneapi
	-DBUILD_SHARED_LIBS=OFF \
	-DWITH_ALEMBIC:BOOL=ON \
	-DWITH_FFTW3=ON \
	-DWITH_JACK=ON \
	-DJACK_LIBRARY=%_libdir/pipewire-0.3/jack/libjack.so \
	-DWITH_CODEC_SNDFILE=ON \
	-DWITH_IMAGE_OPENJPEG=ON \
	-DWITH_PYTHON=ON \
	-DWITH_PYTHON_INSTALL=OFF \
	-DWITH_CODEC_FFMPEG=ON \
	-DWITH_CXX_GUARDEDALLOC=OFF \
	-DWITH_INSTALL_PORTABLE=OFF \
	-DWITH_PYTHON_SAFETY=OFF \
	-DWITH_OPENMP=ON \
	-DWITH_CYCLES=ON \
%if_with embree
	-DEMBREE_ROOT_DIR=%_prefix \
	-DWITH_CYCLES_EMBREE:BOOL=ON \
%else
	-DWITH_CYCLES_EMBREE:BOOL=OFF \
%endif
%if_with usd
	-DWITH_USD:BOOL=ON \
%else
	-DWITH_USD:BOOL=OFF \
%endif
%if_with mold
	-DWITH_LINKER_MOLD=YES \
%endif
	-DWITH_OPENCOLORIO=ON \
	-DWITH_OPENVDB:BOOL=ON \
	-DWITH_OPENVDB_BLOSC:BOOL=ON \
	-DWITH_SYSTEM_DRACO=ON \
	-DWITH_SYSTEM_LZO=ON \
	-DWITH_SYSTEM_EIGEN3:BOOL=ON \
	-DWITH_SYSTEM_GFLAGS:BOOL=ON \
	-DWITH_SYSTEM_GLOG:BOOL=ON \
	-DWITH_SYSTEM_FREETYPE:BOOL=ON \
	-DWITH_IMAGE_OPENEXR=ON \
	-DWITH_TBB:BOOL=ON \
	-DPYTHON_VERSION="%_python3_version" \
	-DBUILDINFO_OVERRIDE_DATE="$BUILD_DATE" \
	-DBUILDINFO_OVERRIDE_TIME="$BUILD_TIME" \
	-DWITH_DOC_MANPAGE:BOOL=ON \
	-DWITH_ASSERT_ABORT:BOOL=OFF \
	-DWITH_LINKER_GOLD:BOOL=OFF \
	-DWITH_OPENSUBDIV:BOOL=ON \
	-DOPENEXR_INCLUDE_DIRS=%_includedir/OpenEXR \
	%nil

ninja-build -v -C %_cmake__builddir

%if_with docs
pushd doc/doxygen
doxygen -u Doxyfile
doxygen
popd
%endif

%install
# Pre-generate man page with LD_LIBRARY_PATH for oneapi library
%if_with oneapi
export LD_LIBRARY_PATH=%_cmake__builddir/intern/cycles/kernel:$LD_LIBRARY_PATH
%endif
%if_with docs
python3 doc/manpage/blender.1.py \
    --blender %_cmake__builddir/bin/blender \
    --output %_cmake__builddir/source/creator/blender.1
%endif
%cmake_install

# Install thumbnailer for file managers
install -Dm644 %SOURCE2 %buildroot%_datadir/thumbnailers/blender.thumbnailer

%files
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/thumbnailers/%name.thumbnailer
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_datadir/%name/
%if_with hip
%exclude %_datadir/%name/*/%kern_dir/kernel_gfx*.fatbin*
%endif
%if_with hiprt
%exclude %_datadir/%name/*/%kern_dir/kernel_rt_gfx*.hipfb*
%endif
%if_with cuda
%exclude %_datadir/%name/*/%kern_dir/kernel_compute*.ptx*
%exclude %_datadir/%name/*/%kern_dir/kernel_sm_*.cubin*
%endif
%if_with oneapi
%_libdir/libcycles_kernel_oneapi_aot.so
%endif
%_datadir/metainfo/*.metainfo.xml
%_defaultdocdir/%name/
%_man1dir/%name.1*

%if_with hip
%files cycles-hip-kernels
%_datadir/%name/*/%kern_dir/kernel_gfx*.fatbin*
%endif

%if_with hiprt
%files cycles-hiprt-kernels
%_datadir/%name/*/%kern_dir/kernel_rt_gfx*.hipfb*
%endif

%if_with cuda
%files cycles-cuda-kernels
%_datadir/%name/*/%kern_dir/kernel_compute*.ptx*
%_datadir/%name/*/%kern_dir/kernel_sm_*.cubin*
%endif

%if_with docs
%files doc
%doc doc/doxygen/html
%endif

%changelog
* Thu Jun 25 2026 Anton Farygin <rider@altlinux.org> 4.5.11-alt1
- 4.5.10 -> 4.5.11

* Sat May 30 2026 Anton Farygin <rider@altlinux.org> 4.5.10-alt1
- 4.5.9 -> 4.5.10

* Mon Apr 27 2026 Anton Farygin <rider@altlinux.org> 4.5.9-alt1
- 4.5.8 -> 4.5.9
- use gcc-14 as CUDA host compiler on Sisyphus
  (nvcc 12.x is incompatible with GCC 15 type_traits)
- added python3-module-numpy dependency (Closes: #58817)

* Tue Mar 24 2026 Anton Farygin <rider@altlinux.org> 4.5.8-alt1
- 4.5.7 -> 4.5.8

* Wed Mar 04 2026 Anton Farygin <rider@altlinux.org> 4.5.7-alt1
- 4.5.6 -> 4.5.7

* Tue Feb 04 2026 Anton Farygin <rider@altlinux.org> 4.5.6-alt2
- added freedesktop thumbnailer file for generating .blend file previews
  in file managers (Closes: #57740)
- removed the blender dependency from the documentation package and made
  it noarch (Closes: #54980)

* Tue Jan 27 2026 Anton Farygin <rider@altlinux.org> 4.5.6-alt1
- 4.5.5 -> 4.5.6

* Tue Dec 31 2025 Anton Farygin <rider@altlinux.com> 4.5.5-alt1
- 4.3.2 -> 4.5.5
- Built with external libdraco.
- Added OneAPI/SYCL support for Intel GPU rendering (x86_64 only).
- Added FFmpeg 8.0 compatibility patch.
- Added OpenXR support for VR headsets.
- Added MaterialX support.
- Added libmanifold, libClipper2, libassimp dependencies.
- Switched from libjack to pipewire-jack for JACK audio support.

* Fri Sep 12 2025 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1.1
- NMU: fixed building with python3.13.

* Mon Jul 21 2025 L.A. Kostis <lakostis@altlinux.ru> 4.3.2-alt1
- Update to 4.3.2.
- cycles: more updates for OIIO API 3.x changes (upstream
  c3c05559d6a7e10981ad8e3c13a8ee7862399c78).
- extern/mantaflow: fix crash with python3.12 (closes ALT #54359).
- Added lost assets (upstream uses lfs now and we have to fetch them
  manually). Closes ALT #54568 #54567 #54565.

* Mon Jul 21 2025 L.A. Kostis <lakostis@altlinux.ru> 4.3.0-alt9
- cycles: fix build with OIIO >= 3.x.

* Mon May 19 2025 L.A. Kostis <lakostis@altlinux.ru> 4.3.0-alt8
- cycles: fix build with OSL >= 1.14.
- spec: cleanup cuda build.
- spec: remove OpenCOLLADA dependency (use OpenUSD as replacement).

* Mon Apr 14 2025 Michael Shigorin <mike@altlinux.org> 4.3.0-alt7
- Build for Sisyphus.

* Fri Apr 04 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.3.0-alt6.1
- Fixed build for Elbrus.

* Thu Feb 13 2025 L.A. Kostis <lakostis@altlinux.ru> 4.3.0-alt6
- Rebuild with new rocm-6.3.2 and HIPRT 2.5:
  + cycles/hiprt: simplify hiprt kernel compilation (use system
    kernels instead of manual compilation).
  + hiprt: move hiprt kernels to separate package - you don't
    need HIP if you use HIPRT and vice versa!

* Thu Feb 13 2025 L.A. Kostis <lakostis@altlinux.ru> 4.3.0-alt5
- Added fixes from upstream:
  + cycles: added openvdb 12.x support.

* Thu Feb 06 2025 Egor Ignatov <egori@altlinux.org> 4.3.0-alt4
- Fix incorrect Provides/Obsoletes made in the previous release.

* Tue Feb 04 2025 Egor Ignatov <egori@altlinux.org> 4.3.0-alt3
- Move hiprt-devel dependency to cycles-hip-kernels subpackage (Closes: #52732)
- Rename cycles-nvidia-kernels to cycles-cuda-kernels

* Fri Dec 20 2024 Ivan A. Melnikov <iv@altlinux.org> 4.3.0-alt2.1
- NMU: loongarch64 update
  + update loongarch64 patch;
  + extract common part from e2k and loongarch64 patches
    to common generic-64bit patch;
  + build with mold on loongarch64.

* Mon Dec 16 2024 Egor Ignatov <egori@altlinux.org> 4.3.0-alt2
- Backport upstream patches to fix build with ffmpeg >= 7.0.

* Mon Nov 25 2024 Egor Ignatov <egori@altlinux.org> 4.3.0-alt1
- Update to 4.3.0.
- Enable hiprt (thx lakostis@).
- Update cycles-fix-kernels patch (thx lakostis@).
- Fix cuda build: downgrade gcc to 13 (thx lakostis@).

* Mon Sep 23 2024 Ivan A. Melnikov <iv@altlinux.org> 4.2.1-alt1.1
- NMU: update loongarch64 patch

* Wed Aug 28 2024 Egor Ignatov <egori@altlinux.org> 4.2.1-alt1
- Update to 4.2.1.
- Don't pack addons and addons_contrib as they are now part of extensions
  platform.
- Update cycles patch: gfx1031 still needs -O1 but not hipcc-func-supp
  (thx lakostis@).

* Tue Aug 27 2024 Anton Farygin <rider@altlinux.ru> 4.1.1-alt3
- added -DGLOG_USE_GLOG_EXPORT  to fix build with glog 0.7.0

* Tue May 14 2024 L.A. Kostis <lakostis@altlinux.ru> 4.1.1-alt2
- usd/hydra: Apply fix to compile with recent USD (upstream PR #121636).

* Tue Apr 16 2024 L.A. Kostis <lakostis@altlinux.ru> 4.1.1-alt1
- Update to 4.1.1.
- cycles: update hip kernels patch (apply opt workaround for
  gfx900 not only on windows).

* Wed Apr 10 2024 Michael Shigorin <mike@altlinux.org> 4.1.0-alt0.5.1
- NMU: align hip arches with those for clr, even

* Mon Apr 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.1.0-alt0.5
- NMU: fixed FTBFS on LoongArch

* Sun Apr 07 2024 L.A. Kostis <lakostis@altlinux.ru> 4.1.0-alt0.4
- Fix cycles-gfx1031-kernel patch.

* Sun Apr 07 2024 L.A. Kostis <lakostis@altlinux.ru> 4.1.0-alt0.3
- Applied fixes for cycles:
  + cycles/hip: reduce opt level and enable hipcc-func-supp for
    gfx1031 kernel (see https://github.com/ROCm/llvm-project/issues/58)

* Thu Apr 04 2024 L.A. Kostis <lakostis@altlinux.ru> 4.1.0-alt0.2
- HIP: Enable on all supported 64-bit arches.
- aarch64: added HIP/CUDA build workaround.

* Wed Apr 03 2024 L.A. Kostis <lakostis@altlinux.ru> 4.1.0-alt0.1
- Update to 4.1.0:
  + Rediffed/update -alt patches.
  + Drop obsoleted/merged patches.
  + Link with mold on supported 64-bit platforms.
  + Use ninja-build (~7-8%% faster on x86_64).
  + Enable LTO.
  + Cycles: disable HIP on aarch64/ppc64le (will enable after ROCm upgrade).
  + Cleanup .spec.

* Sun Mar 17 2024 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.9
- Fix OSL shader dir.
- Cycles: enable HIP on aarch64.
- Added upstream patches from blender-v4.1-release:
  + Cycles: Remove and update deprecated compiler options for HIP
  + Fix #112983: Cycles HIP-RT crash on deleting all objects
  + Fix: Cycles HIP incorrect rendering of clip image textures

* Sat Mar 16 2024 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.8
- aarch64: build with openimagedenoise support.

* Thu Mar 14 2024 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.7
- Added patches from upstream/main:
  + cycles: added OSL >= 1.13.5 compatiblity patch.

* Thu Mar 14 2024 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.6
- Added patches from upstream:
  + cycles: added openpgl 0.6.0 support (upstream PR #118328).

* Tue Mar 12 2024 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.5
- Added patches from upstream:
  + hip: added rocm6 compatibility patch.

* Thu Feb 22 2024 Michael Shigorin <mike@altlinux.org> 4.0.2-alt0.4.1
- E2K: update patch (ilyakurdyukov@).

* Fri Jan 05 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt0.4
- NMU: fixed build with python3.12.

* Fri Dec 29 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.3
- Disable hiprt (as hiprt compiled against obsoleted rocm version
  and doesn't work see upstream HIPRTSDK issue #18).

* Wed Dec 06 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.2
- Added CUDA support (tnx to fidel@ for packages).

* Wed Dec 06 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0.2-alt0.1
- Update to 4.0.2:
  + Rediffed patches and drop merged ones.

* Wed Nov 29 2023 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt0.1
- Update to 4.0.1:
  + Rediffed patches and drop obsoleted ones.
  + Added patch to fix man page generation in isolated env.
  + BR: Added OpenUSD dependency.
  + ppc64le: fix build.

* Tue Nov 14 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.5-alt2
- Update BR:
  + Added WebP support.
  + Added libspnav support.
  + remove deprecated options.

* Wed Oct 25 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.5-alt1
- Update to 3.6.5.
- fix link with recent lld (due https://reviews.llvm.org/D135402).

* Fri Sep 22 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.3-alt1
- Update to 3.6.3.
- alt-hiprt-enable: rebase to 3.6.3.

* Thu Sep 21 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.6.2-alt1.1
- Fixed build for Elbrus.

* Mon Aug 28 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.2-alt1
- Update to 3.6.2.
- Cleanup applied patches.

* Mon Jul 31 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.1-alt2
- Cycles: apply some fixes from main:
  + Fix MNEE not accounting for closure Fresnel
  + HIP RT crash with multi device rendering (upstream issue #109417).

* Wed Jul 19 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.1-alt1
- Update to 3.6.1.

* Thu Jul 13 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt5.gfc44305e720
- v3.6.0-55-gfc44305e720.
- Fix unowned dir for cycles kernels.

* Sun Jul 09 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt4
- aarch64: enable embree.
- .spec: cleanup obsoleted build options.

* Sat Jul 08 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt3
- x86_64: Added experimental HIP RT support.
- Build with vulkan.

* Thu Jul 06 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt2
- aarch64 and x86_64: Build with openpgl.
- aarch64: build with sse2neon.
- x86_64: pack HIP kernels as separate package.
- Rebuild w/ updated TBB.

* Wed Jul 05 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt1
- Update to 3.6.0:
  - drop e2k support (patch outdated).
  + enable HIP kernels compilation.

* Thu Jun 22 2023 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt2.6
- cycles: apply fix to build with gcc-13 (tnx to glebfm@).

* Wed Jun 21 2023 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt2.5
- x86_64: build with openimagedenoise.

* Sun Jun 18 2023 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt2.4
- ppc64le: use lld for linking.

* Sun Jun 18 2023 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt2.3
- fix unresolved symbols with gold linker.

* Fri Jun 16 2023 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt2.2
- NMU:
  - remove deps to clang static libs.
  - x86_64: use lld for linking.
  - ldd: use sha1 for build-id (default fast is too short for rpm).

* Wed Mar 22 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.4.1-alt2.1
- Fixed build for Elbrus.

* Mon Mar 20 2023 Alexander Burmatov <thatman@altlinux.org> 3.4.1-alt2
- Fix build requires.

* Fri Dec 30 2022 Egor Ignatov <egori@altlinux.org> 3.4.1-alt1
- Update to 3.4.1

* Wed Dec 07 2022 Egor Ignatov <egori@altlinux.org> 3.4.0-alt1
- Update to 3.4.0

* Fri Oct 07 2022 Egor Ignatov <egori@altlinux.org> 3.3.1-alt1
- Update to 3.3.1

* Wed Sep 07 2022 Egor Ignatov <egori@altlinux.org> 3.3.0-alt1
- Update to 3.3.0
- Update blender-2.80-alt-use-system-glog patch
- Disable python_api documentation build

* Wed Aug 03 2022 Egor Ignatov <egori@altlinux.org> 3.2.2-alt1
- Updated to upstream version 3.2.2.

* Mon Jul 11 2022 Egor Ignatov <egori@altlinux.org> 3.2.1-alt1
- Updated to upstream version 3.2.1.

* Thu Jul 07 2022 Egor Ignatov <egori@altlinux.org> 3.2.0-alt3
- Fix branch check

* Thu Jul 07 2022 Egor Ignatov <egori@altlinux.org> 3.2.0-alt2
- Add blender-3.2.0-alt-python39 patch
- Disable LTO for p10 to fix build

* Fri Jun 24 2022 Egor Ignatov <egori@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.

* Fri Mar 25 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.0-alt1
- Updated to upstream version 3.1.0.

* Tue Feb 01 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.1-alt1
- Updated to upstream version 3.0.1.

* Wed Dec 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt2
- Rebuilt without Open Image Denoise.

* Mon Dec 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Fri Dec 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.6-alt1
- Updated to upstream version 2.93.6.

* Thu Oct 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.5-alt2
- Fixed build with new glibc.

* Fri Oct 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.5-alt1
- Updated to upstream version 2.93.5.

* Fri Oct 01 2021 Michael Shigorin <mike@altlinux.org> 2.93.4-alt2.1
- Build with openshadinglanguage on %%e2k too (thx ilyakurdyukov@).
- Fixed bogus date in 2008's changelog.

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.4-alt2
- Rebuilt with new OpenColorIO and OpenImageIO.

* Fri Sep 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.4-alt1
- Updated to upstream version 2.93.4.

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.3-alt1
- Updated to upstream version 2.93.3.

* Mon Aug 16 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.93.2-alt4
- Fixed build with TBB on Elbrus.

* Wed Aug 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.2-alt3
- Disabled provides autogeneration (Closes: #40706).

* Wed Aug 11 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.93.2-alt2
- Added patch for Elbrus.

* Fri Aug 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.2-alt1
- Updated to upstream version 2.93.2.

* Mon Jun 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.1-alt1
- Updated to upstream version 2.93.1.

* Wed Jun 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.0-alt2
- Rebuilt with Open Image Denoise, Open Shading Language, OpenSubdiv and Potrace.

* Thu Jun 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.93.0-alt1
- Updated to upstream version 2.93.0.
- Built with jemalloc, libharu and pulseaudio.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.92.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Feb 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.92.0-alt1
- Updated to upstream version 2.92.0.
- Updated build and runtime dependencies.

* Wed Jan 27 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.91.2-alt2
- Updated runtime dependencies.

* Fri Jan 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.91.2-alt1
- Updated to upstream version 2.91.2.

* Fri Jan 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.91.0-alt2
- Circumvented build issues on aarch64 caused by gcc-10 consuming more resources.

* Fri Nov 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.91.0-alt1
- Updated to upstream version 2.91.0.

* Thu Sep 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.90.1-alt1
- Updated to upstream version 2.90.1.

* Tue Sep 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.90.0-alt1
- Updated to upstream version 2.90.0.
- Enabled dependencies: embree, openmp, llvm, openvdb, alembic.
- Built documentation.
- Disabled build for 32bit architectures.

* Mon Aug 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.83.5-alt1
- Updated to upstream version 2.83.5.

* Thu Aug 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.83.4-alt1
- Updated to upstream version 2.83.4.

* Mon Jul 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.83.3-alt1
- Updated to upstream version 2.83.3.

* Fri Jul 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.83.1-alt2
- Removed dependency to python2-base.

* Thu Jul 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.83.1-alt1
- Updated to upstream version 2.83.1.

* Mon Jun 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.83-alt1
- Updated to upstream version 2.83.

* Wed Apr 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.82-alt1.a
- Updated to upstream version 2.82a.

* Tue Mar 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.82-alt1
- Updated to upstream version 2.82.

* Tue Jan 21 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.81-alt1.a
- Updated to upstream version 2.81a.

* Wed Jul 31 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.80-alt1
- Updated to upstream version 2.80.

* Tue May 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt7
- Fixed compatibility with python-3.7.
- Rebuilt with openimageio-2.0.8.
- Switched to upstream desktop file.

* Fri Nov 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt6
- Fixed build with gcc-8 (Closes: #35699)

* Mon Oct 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt5
- Enabled Cycles render engine (Closes: #29162)
- Cleaned up spec.

* Fri Oct 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt4
- Fixed build.

* Mon Jun 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt3
- Rebuilt with ffmpeg-4.0.
- Moved i18n files back into main package.

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt2
- Rebuilt with boost-1.67.0.

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.79b-alt1
- Updated to 2.79b.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.78c-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Jun 13 2017 Anton Farygin <rider@altlinux.ru> 2.78c-alt1
- Updated to 2.78c.

* Mon Oct 31 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.78a-alt1
- Updated to 2.78a.

* Thu Apr 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.77a-alt1.1
- (NMU) Rebuild with rpm-build-python3-0.1.10.2 (more autoreqs/provs).

* Fri Apr 15 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.77a-alt1
- Updated to 2.77a.
- Enable localization by default (ALT#31561).

* Wed Mar 30 2016 Denis Medvedev <nbr@altlinux.org> 2.76b-alt2
- Changed provides to macros.

* Tue Mar 08 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.76b-alt1
- Updated to 2.76b.
- Rebuilt with python 3.5.

* Tue Dec 10 2013 Andrey Liakhovets <aoliakh@altlinux.org> 2.69-alt1
- 2.69
- buildreq adjusted for new fontconfig
- temporary cmake patch to find freetype 2.5.1
- 'Conflicts' with old Collada changed to 'Requires' new Collada

* Mon Sep 23 2013 Andrey Liakhovets <aoliakh@altlinux.org> 2.68a-alt3
- lost conflict with libopenCOLLADA <= 0-alt1_16.git9665d16 added

* Sun Sep 22 2013 Andrey Liakhovets <aoliakh@altlinux.org> 2.68a-alt2
- COLLADA upstream fixes, to make blender work with OpenCOLLADA-828b603
  (blender bug #36325 fixed: "Collada Import: Vertex-Groups missing")
- clean spec from some unneeded patches
- *-2.66-alt-libav.patch updated  (it also matches with P7 libav*, but:
  blender-for-P7 now requires separate build, due to av_update_cur_dts)
- specsubst used to build for Sisyphus and P7

* Thu Aug 01 2013 Andrey Liakhovets <aoliakh@altlinux.org> 2.68a-alt1
- New release (bugfix)

* Sun Jul 21 2013 Andrey Liakhovets <aoliakh@altlinux.org> 2.68-alt1
- New version
- *-2.67b-node_efficiency_tools.patch dropped (2.67b-only)
- 0006-locales_directory_install.patch updated
- 0011-look_for_droid_ttf_with_fontconfig.patch updated

* Mon Jun 17 2013 Andrey Liakhovets <aoliakh@altlinux.org> 2.67b-alt2
- Build with boost (+ boost-filesystem, boost-locale)
- Build with OpenCOLLADA
- Build with fontconfig
- Build with pcre: *-2.66-alt-pcre.patch added
- no blenpluginapi (removed in upstream)
- remove default WITH_BUILTIN_GLEW=OFF and WITH_BOOST=ON options
- *-2.67b-node_efficiency_tools.patch added (fix syntax error in 2.67b)
- RNA patch from Fedora expanded
- *-alt-libav.patch reworked
   (*-2.62-* fixed in upstream, *-2.66-* corresponds to alt libav*)
- 0006-locales_directory_install.patch: *.mo and languages separated
- 0009-do_not_use_version_number_in_the_system_path.patch updated
- 0011-look_for_droid_ttf_with_fontconfig.patch updated and corrected
- skip _bpy_path python requirement

* Wed Jun 05 2013 Sergei Epiphanov <serpiph@altlinux.ru> 2.67b-alt1
- New version
- Add RNA patch from Fedora

* Wed Apr 10 2013 Sergei Epiphanov <serpiph@altlinux.ru> 2.66-alt1
- New version

* Thu Mar 14 2013 Aleksey Avdeev <solo@altlinux.ru> 2.63-alt0.2
- Rebuilt with python3-3.3

* Tue Aug 21 2012 Yuriy Kashirin <uka@altlinux.ru> 2.63-alt0.1
- 2.63 test build

* Sat Mar 31 2012 Sergei Epiphanov <serpiph@altlinux.ru> 2.62-alt1
- Build with new rpm-build-python3
- Fix libav patch

* Sat Mar  3 2012 Sergey Kurakin <kurakin@altlinux.org> 2.62-alt0.2
- jack support
- sndfile codec support
- openjpeg support

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt9.3
- Rebuilt with qhull 2012.1

* Sat Feb 18 2012 Sergey Kurakin <kurakin@altlinux.org> 2.62-alt0.1
- 2.62 test build

* Fri Feb 17 2012 Sergey Kurakin <kurakin@altlinux.org> 2.61-alt0.2
- patches from Debian:
  + scripts in libexecdir
  + non-versioned scripts directory
  + use fontconfig to get interface font

* Tue Feb 14 2012 Sergey Kurakin <kurakin@altlinux.org> 2.61-alt0.1
- 2.61 test build

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt9.2
- Rebuilt with qhull 2011.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.49b-alt9.1
- Rebuild with Python-2.7

* Thu Aug 04 2011 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt9
- Build with libav fixed once again

* Wed Aug 03 2011 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt8
- Fixed build with libav

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt7
- Rebuilt with qhull 2011.1

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt6
- Rebuilt for debuginfo

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt5
- Added libalut-devel into BuildPreReq
- Built with system qhull instead of build-in

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.49b-alt4
- Fixed build

* Sun Dec 19 2010 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt3
- added Provides: python(BPyMesh) (closes: #24769)
- removed useless python pseudo-modules, containing sources
  of the python API reference
- really linked with system libFTGL instead of bundled one
- built with system libGLEW instead of bundled one

* Tue Sep 28 2010 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt2
- added Provides: python(bpy) (closes: #24147)
- languages support moved to -i18n subpackage
- blender-wrapper refactoring
- spare font removed from package

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 2.49b-alt1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Sergey Kurakin <kurakin@altlinux.org> 2.49b-alt1
- 2.49b: bugfix release

* Thu Jul 23 2009 Sergey Kurakin <kurakin@altlinux.org> 2.49a-alt2
- removed deprecated Requires: python = pyton_version
  (repocop warning)

* Fri Jun 26 2009 Sergey Kurakin <kurakin@altlinux.org> 2.49a-alt1
- 2.49a
- warning: yafray support is completely removed in 2.49
- dropped openal_source patch (fixed in upstream)
- dropped alt-gimp patch (fixed in upstream)
- dropped alt-ffmpeg52 patch (fixed in upstream)
- removed spare BuildRequires

* Tue May  5 2009 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt5
- blender-wrapper fixed on x86_64
- blender-wrapper improved to take care with blender scripts
  from other packages
- Provides: python(Blender) for other packages with blender scripts
- Requires: symlinks (needed for blender-wrapper)
- minor spec cleanup

* Mon Mar 16 2009 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt4
- build fixed (BuldRequires)
- description corrected (russian)

* Thu Feb 12 2009 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt3
- fixed build with libavcodec52

* Tue Dec  9 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt2
- libopenal support enabled again
  (see 2.48a-alt0.1 chengelog entry)

* Fri Nov 28 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt1
- post-scripts removed (update_menus & update_desktopdb)
- additional code in wrapper: move ~/.blender/.B.blend to ~/.B.blend
  (see .B.blend issue in 2.46-alt1 changelog)

* Tue Oct 28 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48a-alt0.1
- 2.48a (bugfix release)
- libopenal support temporary removed
  in order to build with gcc4.3

* Thu Oct 16 2008 Sergey Kurakin <kurakin@altlinux.org> 2.48-alt0.1
- 2.48
- gimp used as external image editor

* Fri Oct 10 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.47-alt2
- summary and description updated
- libtiff4 patch restored and updated,
  fixing libtiff.so.4 loading on x86_64
- new usertempdir patch fixes tmp directory issues
- removed .menu files
- updated .desktop files:
  + fixed repocop warnings
  + #16829
  + run in terminal (for window mode only)
- unnecessary icons removed from sources (included in tarball)
- more spec cleanup

* Mon Aug 25 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.47-alt1
- 2.47

* Mon Jul 14 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.46-alt1
- 2.46
- removed verify_elf_skiplist, useless for now
- removed long list of add_python_req_skip, useless for now
- removed tiff4 patch
- removed fix-temp patch
- user configuration file .B.blend moved back to original
  location $HOME/.B.blend (see 2.45-alt1 changelog entry)
- spec cleanup

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.45-alt2.2.1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for blender

* Fri Feb 29 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.45-alt2.2.1
- Rebuilt due to libIlmImf.so.4 -> libIlmImf.so.6 soname change.

* Sun Feb 17 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.45-alt2.2
- Rebuild with libavformat.52

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.45-alt2.1
- Rebuilt with python-2.5.

* Mon Oct 22 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.45-alt2
- Fix owner/group of plugins

* Sat Oct 13 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.45-alt1
- New version
- Fix temp dir
- Move user defaults file from ~ to ~/.blender
- Fix plugin rights
- Fix execution script
- Fix verify_elf
- Set hard depend to python2.4

* Tue Sep 11 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt4
- Fix python dependencies

* Fri Jun 29 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt3
- Swap windowed and fullscreen mode

* Sat May 26 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt2
- Cleaning .spec
- Add russian description
- Fix build process

* Mon May 14 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.44-alt1
- New version
- Replace illegal Requires with right stuff
- Fix 'blender' script for x86_64

* Mon Mar 12 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.43-alt2
- Fix Provides/Requires section

* Sat Feb 24 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.43-alt1
- New version

* Thu Feb 15 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt4
- Add selection between desktop and menu files
- Add blender startup in window mode

* Thu Dec 14 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt3
- rebuild

* Wed Sep 20 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt2
- fixing error in build

* Sun Sep 10 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.42-alt1
- New version

* Fri Sep 08 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.41-alt2
- Fixing load of libtiff4.

* Sat Mar 04 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.41-alt1
- New version
- Cleanup spec for X.Org 7.0

* Fri Mar 03 2006 Sergei Epiphanov <serpiph@altlinux.ru> 2.40-alt3
- Correcting spec (correcting icons dir).

* Wed Dec 28 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.40-alt2
- Correction of blender.menu file

* Mon Dec 26 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.40-alt1
- New version

* Wed Mar 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.36-alt1.1
- Rebuilt with python-2.4.

* Sun Jan 30 2005 Andrey Astafiev <andrei@altlinux.ru> 2.36-alt1
- 2.36
- Some features incorporated from Debian package.

* Mon Mar 01 2004 Kachalov Anton <mouse@altlinux.ru> 2.32-alt1
- new version 2.32

* Sun Dec 28 2003 Kachalov Anton <mouse@altlinux.ru> 2.30-alt1
- new version 2.30

* Wed Sep 17 2003 Kachalov Anton <mouse@altlinux.ru> 2.28a-alt1
- new version 2.28a

* Tue Jun 24 2003 Kachalov Anton <mouse@altlinux.ru> 2.27-alt1
- new version 2.27

* Mon Jan 20 2003 Kachalov Anton <mouse@altlinux.ru> 2.25b-alt2
- fixed buildrequires

* Tue Nov 12 2002 Kachalov Anton <mouse@altlinux.ru> 2.25b-alt1
- build for Sisyphus
