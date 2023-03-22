%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%def_with docs

%ifarch x86_64 %e2k
%def_with embree
%else
%def_without embree
%endif

%def_with jemalloc

Name: blender
Version: 3.4.1
Release: alt2
Summary: 3D modeling, animation, rendering and post-production
License: GPL-3.0-or-later
Group: Graphics
URL: https://www.blender.org

# Blender doesn't officially support 32-bit build since 2.80. See also:
# https://developer.blender.org/T67184
ExcludeArch: %ix86 %arm

# git://git.blender.org/blender.git
Source: %name-%version.tar

# git submodules
# before updating submodules via script don't forget
# to update relative submodule paths into absolute ones
Source1: %name-%version-release-datafiles-locale.tar
Source2: %name-%version-release-scripts-addons_contrib.tar
Source3: %name-%version-release-scripts-addons.tar
Source4: %name-%version-source-tools.tar

Patch21: blender-2.66-alt-pcre.patch
Patch22: blender-2.77-alt-enable-localization.patch
Patch24: blender-2.92-alt-include-deduplication-check-skip.patch
Patch25: blender-2.80-alt-use-system-glog.patch
Patch26: blender-2.83.1-alt-remove-python2-dependency.patch
Patch27: blender-2.90.0-alt-embree-components.patch
Patch28: blender-3.0.0-alt-doc.patch
Patch29: blender-2.90-alt-non-x86_64-linking.patch
Patch30: blender-2.93.0-suse-reproducible.patch


Patch2000: blender-e2k-support.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: boost-filesystem-devel boost-locale-devel
BuildRequires: cmake gcc-c++
BuildRequires: libGLEW-devel libXi-devel
BuildRequires: libavdevice-devel libavformat-devel
BuildRequires: libfftw3-devel libjack-devel libopenal-devel libsndfile-devel
BuildRequires: libjpeg-devel pkgconfig(libopenjp2) libpng-devel libtiff-devel libpcre-devel libswscale-devel libxml2-devel
BuildRequires: liblzo2-devel
BuildRequires: libopenCOLLADA-devel >= 0-alt3
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: libopenimageio-devel
BuildRequires: libopencolorio2.2-devel
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
BuildRequires: llvm-devel clang-devel clang-devel-static
BuildRequires: libgomp-devel
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: libharu-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libpotrace-devel
BuildRequires: openshadinglanguage-devel
BuildRequires: opensubdiv-devel
BuildRequires: libzstd-devel
BuildRequires: libepoxy-devel

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
Requires: %name = %EVR

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

%prep
%setup -a1 -a2 -a3 -a4

%patch21 -p1
%patch22 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

%ifarch %e2k
%patch2000 -p1
# lcc 1.25.15's EDG bug would fail building OPENVDB+TBB otherwise
sed -i "/-Werror=return-type/d" CMakeLists.txt
%endif

# Delete the bundled FindOpenJPEG to make find_package use the system version
# instead (the local version hardcodes the openjpeg version so it is not update
# proof)
rm -f build_files/cmake/Modules/FindOpenJPEG.cmake

# Remove bundled libraries which must not be used instead of system ones
rm -rf extern/{Eigen3,glew,lzo,gflags,glog}

%build
BUILD_DATE="$(stat -c '%%y' '%SOURCE0' | date -f - '+%%Y-%%m-%%d')"
BUILD_TIME="$(stat -c '%%y' '%SOURCE0' | date -f - '+%%H:%%M:%%S')"

# needed due to non-standard location of pcre.h header
%add_optflags "-I%_includedir/pcre"

%add_optflags -fPIC -funsigned-char -fno-strict-aliasing

%ifarch aarch64
# limit build jobs on aarch64
if [ %__nprocs -gt 48 ] ; then
	export NPROCS=48
fi
%endif

%cmake \
%ifnarch %{ix86} x86_64
	-DWITH_RAYOPTIMIZATION=OFF \
	-DWITH_CPU_SSE=OFF \
%endif
	-DBUILD_SHARED_LIBS=OFF \
	-DWITH_ALEMBIC:BOOL=ON \
	-DWITH_FFTW3=ON \
	-DWITH_JACK=ON \
	-DWITH_CODEC_SNDFILE=ON \
	-DWITH_IMAGE_OPENJPEG=ON \
	-DWITH_PYTHON=ON \
	-DWITH_PYTHON_INSTALL=OFF \
	-DWITH_CODEC_FFMPEG=ON \
	-DWITH_CXX_GUARDEDALLOC=OFF \
	-DWITH_INSTALL_PORTABLE=OFF \
	-DWITH_LLVM=ON \
	-DWITH_CLANG=ON \
	-DWITH_PYTHON_SAFETY=OFF \
	-DWITH_OPENMP=ON \
	-DWITH_OPENCOLLADA=ON \
	-DWITH_CYCLES=ON \
%if_with embree
	-DEMBREE_ROOT_DIR=%_prefix \
	-DWITH_CYCLES_EMBREE:BOOL=ON \
%else
	-DWITH_CYCLES_EMBREE:BOOL=OFF \
%endif
	-DWITH_OPENCOLORIO=ON \
	-DWITH_OPENIMAGEIO=ON \
	-DWITH_OPENVDB:BOOL=ON \
	-DWITH_OPENVDB_BLOSC:BOOL=ON \
	-DWITH_SYSTEM_GLEW=ON \
	-DWITH_SYSTEM_LZO=ON \
	-DWITH_SYSTEM_EIGEN3:BOOL=ON \
	-DWITH_SYSTEM_GFLAGS:BOOL=ON \
	-DWITH_SYSTEM_GLOG:BOOL=ON \
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

%cmake_build

%if_with docs
pushd doc/doxygen
doxygen -u Doxyfile
doxygen
popd
%endif

%install
%cmake_install

mkdir -p %buildroot%_datadir/metainfo
install -m644 release/freedesktop/*.appdata.xml %buildroot%_datadir/metainfo/

%files
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_datadir/%name/
%_datadir/metainfo/*.appdata.xml
%_defaultdocdir/%name/
%_man1dir/*.1*

%if_with docs
%files doc
%doc doc/doxygen/html
%endif

%changelog
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
