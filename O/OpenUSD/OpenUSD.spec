%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 0
# endless sigh
%define lversion 26.5
%define qt_ver 6
%define stage %nil

%def_enable alembic
%def_enable draco
%def_enable embree
%def_disable jemalloc
%def_enable openshading
%def_enable openvdb
%def_enable ocio
%def_enable oiio
%def_enable ptex
%def_enable pyside6
%def_enable usdview
%def_enable hdf5
%def_enable materialx

Name: OpenUSD
Version: 26.05
Release: alt0.1
Summary: Universal Scene Description library
Group: Development/Other
License: TOST-1.0
Url: https://openusd.org
VCS: https://github.com/PixarAnimationStudios/OpenUSD.git
Source0: %name-%version.tar
Source1: org.openusd.usdview.desktop
# Latest stb_image.patch that applies cleanly against 2.27:
#   %%{url}/raw/8f9bb9563980b41e7695148b63bf09f7abd38a41/pxr/imaging/hio/stb/stb_image.patch
# We treat this as a source file because it is applied separately during
# unbundling. It has been hand-edited to apply to 2.28, where
# stbi__unpremultiply_on_load_thread is already renamed to
# stbi_set_unpremultiply_on_load_thread.
Source2: stb_image.patch

Patch0: openusd-alt-tbb-disable-debug-relwithdebinfo.patch
# SONAME patch from Fedora/RH
Patch1: 0001-Downstream-only-add-an-SONAME-version.patch
# Fix blender GL errors when using Hydra
# https://github.com/PixarAnimationStudios/OpenUSD/pull/2550
Patch2: 2550.patch
# usd: Fix build failure with libstdc++15 / C++23
# https://github.com/PixarAnimationStudios/OpenUSD/pull/4085
Patch3: 4085.patch
# should be send to upstream
Patch4: openusd-alt-tbb-2023.patch

BuildRequires(pre): cmake rpm-build-python3 ninja-build /proc
BuildRequires: gcc-c++
# tbb and embree still need boost
BuildRequires: boost-devel boost-python3-devel
BuildRequires: tbb-devel
BuildRequires: pkgconfig(blosc) pkgconfig(dri) opensubdiv-devel
BuildRequires: imath-devel >= 3.0 openexr-devel pkgconfig(Qt%{qt_ver})
BuildRequires: python3-module-OpenGL python3-module-jinja2 python3-dev
BuildRequires: dos2unix help2man libstb-devel
%{?_enable_alembic:BuildRequires: alembic-devel}
%{?_enable_draco:BuildRequires: libdraco-devel}
%{?_enable_embree:BuildRequires: embree-devel}
%{?_enable_jemalloc:BuildRequires: libjemalloc-devel}
%{?_enable_ocio:BuildRequires: libopencolorio2.2-devel}
%{?_enable_oiio:BuildRequires: libopenimageio-devel}
%{?_enable_openshading:BuildRequires: openshadinglanguage-devel}
%{?_enable_openvdb:BuildRequires: openvdb-devel}
%{?_enable_ptex:BuildRequires: libPtex-devel}
%{?_enable_hdf5:BuildRequires: libhdf5-devel}
%{?_enable_usdview:BuildRequires: desktop-file-utils}
%{?_enable_materialx:BuildRequires: MaterialX-devel libXt-devel}
%if_enabled pyside6
BuildRequires: python3-module-pyside6-devel
%else
BuildRequires: python3-module-PySide2
%endif

# This package is only available for x86_64 and aarch64
# Will fail to build on other architectures
# https://bugzilla.redhat.com/show_bug.cgi?id=1960848
#
# Note that pxr/base/arch/assumptions.cpp explicitly tests the machine is not
# big-endian, and pxr/base/arch/defines.h explicitly enforces x86_64 or ARM64.
ExclusiveArch: aarch64 x86_64

%filter_from_requires /\/usr\/share\/fonts\/ttf\/roboto/d;\/usr\/share\/fonts\/ttf\/google\-roboto\-mono.*/d

# should use pyside6 instead
%add_python3_req_skip PySide2.QtCore
%add_python3_req_skip PySide2.QtGui
%add_python3_req_skip PySide2.QtWidgets

%description
Universal Scene Description (USD) is an efficient, scalable system for
authoring, reading, and streaming time-sampled scene description for
interchange between graphics applications.

%package -n lib%name%soname
Summary: Universal Scene Description library
Group: System/Libraries
# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython
Requires: %name-resources = %EVR

%description -n lib%name%soname
Universal Scene Description (USD) is an efficient, scalable system for
authoring, reading, and streaming time-sampled scene description for
interchange between graphics applications.

%package resources
Summary: Universal Scene Description library resources
Group: Development/Other
AutoReq: nopython
AutoProv: nopython

%description resources
Universal Scene Description library resources and plugins.

%package devel
Summary: Universal Scene Description library development headers
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR
# cpp.req only uses pkgconfig for cflags and we have only cmake
# so it's useless to run
AutoReq: yes, nocpp

%description devel
Universal Scene Description library development headers

# For usdview, usdcompress
%package -n python3-module-usd
Summary: %summary
Group: Development/Python3
%if_enabled usdview
Requires: font(roboto)
Requires: font(robotomono)
%endif
Requires: python3-module-OpenGL

%description -n python3-module-usd
Python language bindings for the Universal Scene Description (USD) C++ API

%prep
%setup
%autopatch -p1

# Convert NOTICE.txt from CRNL line encoding
dos2unix NOTICE.txt

# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

# Further drop shebangs line for some py files
sed -r -i '1{/^#!/d}' \
	pxr/usd/sdr/shaderParserTestUtils.py \
	pxr/usd/usdUtils/updateSchemaWithSdrNode.py \
	pxr/usdImaging/usdviewq/usdviewApi.py

# Unbundle Google Roboto fonts
rm -rvf pxr/usdImaging/usdviewq/fonts/*
ln -s %_datadir/fonts/ttf/roboto pxr/usdImaging/usdviewq/fonts/Roboto
ln -s %_datadir/fonts/ttf/google-roboto-mono \
    pxr/usdImaging/usdviewq/fonts/Roboto_Mono

# Unbundle stb_image, stb_image_write, stb_image_resize:
pushd pxr/imaging/hio/stb
cp -p %_includedir/stb/stb_image.h .
patch -p1 < '%SOURCE2'
ln -svf %_includedir/stb/stb_image_resize.h \
    %_includedir/stb/stb_image_write.h ./
popd

# Remove bundled doxygen-awesome-css (CSS and JS files) since we are not
# building Doxygen-generated HTML documentation.
rm -rf docs/doxygen/doxygen-awesome-css/

# Fix libdir installation
sed -i 's|lib/usd|%_libdir/usd|g' cmake/macros/Private.cmake
sed -i 's|"lib"|%_libdir|g' cmake/macros/Private.cmake
sed -i 's|plugin/usd|%_libdir/usd/plugin|g' \
        cmake/macros/Private.cmake
sed -i 's|lib/python|%_lib/python3/site-packages|g' \
        cmake/macros/Private.cmake
sed -i 's|lib/usd|%_libdir/usd|g' cmake/macros/Public.cmake
sed -i 's|"lib"|%_libdir|g' cmake/macros/Public.cmake
sed -i 's|plugin/usd|%_libdir/usd/plugin|g' \
        cmake/macros/Public.cmake

# Fix cmake directory destination
sed -i 's|"${CMAKE_INSTALL_PREFIX}"|%_libdir/cmake/pxr|g' pxr/CMakeLists.txt

# Fix uic-qt6 use
cat > uic-wrapper <<'EOF'
#!/bin/sh
exec %_libdir/qt%{qt_ver}/libexec/uic -g python "$@"
EOF
chmod +x uic-wrapper

%build
%cmake \
	-GNinja \
%if_with jemalloc
	-DPXR_MALLOC_LIBRARY="%_libdir/libjemalloc.so" \
%endif
	-DCMAKE_SKIP_INSTALL_RPATH=ON \
	%_cmake_skip_rpath \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DPYTHON_EXECUTABLE=%_bindir/python3 \
     	-DPXR_BUILD_DOCUMENTATION=FALSE \
     	-DPXR_BUILD_EXAMPLES=OFF \
     	-DPXR_BUILD_IMAGING=ON \
     	-DPXR_BUILD_MONOLITHIC=ON \
     	-DPXR_BUILD_TESTS=OFF \
     	-DPXR_BUILD_TUTORIALS=OFF \
     	-DPXR_BUILD_USD_IMAGING=ON \
     	-DPXR_BUILD_USD_TOOLS=ON \
	%if_enabled usdview
     	-DPXR_BUILD_USDVIEW=ON \
	%else
	-DPXR_BUILD_USDVIEW=OFF \
	%endif
     	\
	%if_enabled alembic
     	-DPXR_BUILD_ALEMBIC_PLUGIN=ON \
	%else
	-DPXR_BUILD_ALEMBIC_PLUGIN=OFF \
	%endif
	%if_enabled draco
     	-DPXR_BUILD_DRACO_PLUGIN=ON \
	%else
	-DPXR_BUILD_DRACO_PLUGIN=OFF \
	%endif
	%if_enabled embree
     	-DPXR_BUILD_EMBREE_PLUGIN=ON \
	%else
	-DPXR_BUILD_EMBREE_PLUGIN=OFF \
	%endif
	%if_enabled ocio
     	-DPXR_BUILD_OPENCOLORIO_PLUGIN=ON \
	%else
	-DPXR_BUILD_OPENCOLORIO_PLUGIN=OFF \
	%endif
	%if_enabled oiio
     	-DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON \
	%else
	-DPXR_BUILD_OPENIMAGEIO_PLUGIN=OFF \
	%endif
     	-DPXR_BUILD_PRMAN_PLUGIN=OFF \
     	\
	%if_enabled openvdb
     	-DPXR_ENABLE_OPENVDB_SUPPORT=ON \
	%else
	-DPXR_ENABLE_OPENVDB_SUPPORT=OFF \
	%endif
	%if_enabled hdf5
     	-DPXR_ENABLE_HDF5_SUPPORT=ON \
	%else
	-DPXR_ENABLE_HDF5_SUPPORT=OFF \
	%endif
	%if_enabled ptex
     	-DPXR_ENABLE_PTEX_SUPPORT=ON \
	%else
	-DPXR_ENABLE_PTEX_SUPPORT=OFF \
	%endif
	%if_enabled openshading
     	-DPXR_ENABLE_OSL_SUPPORT=ON \
	%else
	-DPXR_ENABLE_OSL_SUPPORT=OFF \
	%endif
	%if_enabled materialx
	-DPXR_ENABLE_MATERIALX_SUPPORT=ON \
	-DMaterialX_DIR=%prefix \
	%else
	-DPXR_ENABLE_MATERIALX_SUPPORT=OFF \
	%endif
     	-DPXR_ENABLE_PYTHON_SUPPORT=ON \
     	\
     	-DPXR_INSTALL_LOCATION="%_libdir/usd/plugin" \
     	\
     	-DPXR_VALIDATE_GENERATED_CODE=OFF \
     	\
     	-DPYSIDE_AVAILABLE=ON \
	-DPYSIDEUICBINARY:PATH=${PWD}/uic-wrapper \
	%nil
%cmake_build

%install
%cmake_install

%if_enabled usdview
# Install a desktop icon for usdview
desktop-file-install                                    \
--dir=%buildroot%_desktopdir              \
%SOURCE1
%endif

# Remove examples that were built and installed even though we set
# -DPXR_BUILD_EXAMPLES=OFF.
rm -vrf '%buildroot%_datadir/usd/examples'

# Fix installation path for some files
mv %buildroot%prefix/lib/python/pxr/*.* \
        %buildroot%python3_sitelibdir/pxr/
%if_enabled usdview
mv %buildroot%prefix/lib/python/pxr/Usdviewq/* \
        %buildroot%python3_sitelibdir/pxr/Usdviewq/
%endif

# TODO: Can we figure out how to fix the installation path for
# pxrTargets{,-release}.cmake, instead of moving them after the fact? We choose
# to put them in the same directory as pxrConfig.cmake.
find %buildroot%prefix/cmake -mindepth 1 -maxdepth 1 -type f \
    -exec mv -v '{}' '%buildroot%_libdir/cmake/pxr' ';'

# Generate and install man pages. While generating the man pages might more
# properly go in %%build, it is generally much easier to do this here in a
# single step, using the entry points installed into the buildroot. This is
# especially true for the entry points that are Python scripts.
install -d '%buildroot%_man1dir'
for cmd in %buildroot%_bindir/*
do
  PYTHONPATH='%buildroot%python3_sitelibdir' \
  LD_LIBRARY_PATH='%buildroot%_libdir' \
      help2man \
      --no-info --version-string='%lversion' \
      --no-discard-stderr --output="%buildroot%_man1dir/$(basename "${cmd}").1" \
      "${cmd}"
done

%check
%if_enabled usdview
#desktop-file-validate %%buildroot%%_desktopdir/org.openusd.usdview.desktop
%endif
%{?_enable_test:%ctest}

%files
%doc NOTICE.txt README.md CHANGELOG.md SECURITY.md LICENSE.txt
%_bindir/sdfdump
%_bindir/sdffilter
%_bindir/usdGenSchema
%_bindir/usdcat
%_bindir/usdchecker
%_bindir/hdGenSchema
%if_enabled draco
%_bindir/usdcompress
%endif
%_bindir/usddiff
%_bindir/usddumpcrate
%_bindir/usdedit
%_bindir/usdfixbrokenpixarschemas
%_bindir/usdgenschemafromsdr
%_bindir/usdrecord
%_bindir/usdresolve
%_bindir/usdstitch
%_bindir/usdstitchclips
%_bindir/usdtree
%_bindir/usdzip
%_bindir/usdmeasureperformance
%_bindir/usdInitSchema
%if_enabled usdview
%_desktopdir/org.openusd.usdview.desktop
%_bindir/testusdview
%_bindir/usdview
%endif
%if_enabled materialx
%_bindir/usdBakeMaterialX
%_man1dir/usdBakeMaterialX.1*
%endif

%_man1dir/sdfdump.1*
%_man1dir/sdffilter.1*
%_man1dir/usdGenSchema.1*
%_man1dir/usdcat.1*
%_man1dir/usdchecker.1*
%_man1dir/hdGenSchema.1*
%if_enabled draco
%_man1dir/usdcompress.1*
%endif
%_man1dir/usddiff.1*
%_man1dir/usddumpcrate.1*
%_man1dir/usdedit.1*
%_man1dir/usdfixbrokenpixarschemas.1*
%_man1dir/usdgenschemafromsdr.1*
%_man1dir/usdrecord.1*
%_man1dir/usdresolve.1*
%_man1dir/usdstitch.1*
%_man1dir/usdstitchclips.1*
%_man1dir/usdtree.1*
%_man1dir/usdzip.1*
%_man1dir/usdmeasureperformance.1*
%_man1dir/usdInitSchema.1*
%if_enabled usdview
%_man1dir/testusdview.1*
%_man1dir/usdview.1*
%endif

%files resources
%_libdir/usd

%files -n lib%name%soname
%doc NOTICE.txt README.md LICENSE.txt
%_libdir/libusd_ms.so.%soname.%lversion

%files devel
%_libdir/libusd_ms.so
%_includedir/pxr
%_libdir/cmake/pxr

%files -n python3-module-usd
%python3_sitelibdir/pxr

%changelog
* Thu May 28 2026 L.A. Kostis <lakostis@altlinux.ru> 26.05-alt0.1
- 26.05.
- hydra: rebase blender patch.
- usd: fix build failure with libstdc++15/c++23 (upstream PR#4085).
- usd: fix build with TBB 2023.0.0 (tnx to rider@).
- .spec fixes:
  + usdview: enable .desktop file (closes #51184).
  + split out -resources from library (closes #59343).

* Wed Nov 19 2025 L.A. Kostis <lakostis@altlinux.ru> 25.11-alt0.1
- 25.11.
- embree4: drop patch (merged by upstream).
- rediffed/update patches.

* Wed Sep 03 2025 L.A. Kostis <lakostis@altlinux.ru> 25.08-alt0.1
- 25.08.
- aarch64: disable ExecLibrary (doesn't compile).
- rediffed/update patches.

* Tue Jul 01 2025 L.A. Kostis <lakostis@altlinux.ru> 25.05.01-alt0.1
- 25.05.01.

* Thu Apr 24 2025 L.A. Kostis <lakostis@altlinux.ru> 25.05-alt0.1.rc1
- 25.05-rc1.
- embree4: rebase patch.
- spec: update files.
- spec: skip cpp.req on -devel headers (because we have only cmake
        but cpp.req relies on pkgconfig).

* Tue Apr 22 2025 L.A. Kostis <lakostis@altlinux.ru> 25.02-alt0.4.a
- Enable MaterialX.

* Tue Apr 15 2025 L.A. Kostis <lakostis@altlinux.ru> 25.02-alt0.3.a
- Update to 25.02a.
- usdview: remove .desktop file (as usdview doesn't work without args).

* Mon Mar 03 2025 Anton Farygin <rider@altlinux.ru> 25.02-alt0.2
- NMU: fixed build with TBB 2022.0.0.
- Added VCS tag.

* Wed Jan 22 2025 L.A. Kostis <lakostis@altlinux.ru> 25.02-alt0.1
- 25.02.
- embree4: rebase patch.
- hydra: Fix issues using Hydra and Storm with OpenGL core
  profile (upstream PR #2550).

* Tue Nov 19 2024 L.A. Kostis <lakostis@altlinux.ru> 24.11-alt0.1
- 24.11.

* Sun Aug 18 2024 L.A. Kostis <lakostis@altlinux.ru> 24.08-alt0.2
- Use PySlide6 for usdview (closes #51184, tnx to grenka@).

* Mon Aug 05 2024 L.A. Kostis <lakostis@altlinux.ru> 24.08-alt0.1
- 24.08.
- cleanup merged patches.
- embree4: update patch (upstream PR #2313).

* Tue May 14 2024 L.A. Kostis <lakostis@altlinux.ru> 24.05-alt0.1
- 24.05.
- cleanup merged patches.

* Fri Mar 15 2024 L.A. Kostis <lakostis@altlinux.ru> 24.03-alt0.1
- 24.03.
- cleanup merged patches.

* Tue Jan 02 2024 Grigory Ustinov <grenka@altlinux.org> 23.11-alt0.4
- NMU: dropped dependency on PySide2.

* Wed Dec 20 2023 Anton Vyatkin <toni@altlinux.org> 23.11-alt0.3
- NMU: Drop dependency on distutils (Closes: #48865).

* Wed Nov 22 2023 Nazarov Denis <nenderus@altlinux.org> 23.11-alt0.2
- build with OpenColorIO 2.3

* Wed Nov 15 2023 L.A. Kostis <lakostis@altlinux.ru> 23.11-alt0.1
- Initial build for ALTLinux.
- .spec loosely based on RH Rawhide.
