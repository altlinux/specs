# SONAME version of libAvogadro* libraries
%define sover 2

%define _unpackaged_files_terminate_build 1

# Static libraries are packaged in -devel-static, so they need fat LTO objects
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

#Python3 Avogadro's module
%def_with python3

#OpenGL backend
%def_with opengl

#Optional file format backends
%def_with openbabel
%def_with hdf5
%def_with libarchive

#Symmetry and crystallography
%def_with spglib
%def_with libmsym

#Printing support
%def_with cups

#Documentation
%def_with docs

#Unit tests
%def_with tests

# Disable MMTF support (upstream notes that MMTF is no longer maintained)
%def_without mmtf

Name: avogadro2-libs
Version: 2.1.0
Release: alt1

Summary: Avogadro2 libraries
Group: Sciences/Chemistry
License: BSD-3-Clause AND GPL-3.0-or-later AND MIT AND Apache-2.0 AND Unlicense AND CC0-1.0
URL: https://avogadro.cc/
VCS: https://github.com/OpenChemistry/avogadrolibs

Source: %name-%version.tar

Patch0: avogadro2-libs-spglib.cmake.patch
Patch1: avogadro2-libs-fragments-1.102.1.patch
Patch2: avogadro2-insert_modules.patch
Patch3: avogadro2-libs-insertpeptide-1.103.0.patch
Patch4: avogadro2-libs-system-python-plugins.patch
Patch5: avogadro2-libs-openbabel-libdir.patch
Patch6: avogadro2-libs-system-fragments.patch
Patch7: avogadro2-libs-layer-column-fix.patch
Patch8: avogadro2-libs-layer-flags-fix.patch
Patch9: avogadro2-libs-qtgui-test-main.patch
Patch10: avogadro2-libs-sourcedata-dir.patch
Patch11: avogadro2-libs-hdf5-test-tmpfile.patch
Patch12: avogadro2-libs-cjson-empty-molecule.patch
Patch13: avogadro2-libs-cmake-eigen-dependency.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  eigen3-devel
BuildRequires:  libGLEW-devel
BuildRequires:  libGLU-devel

BuildRequires:  jsoncpp-devel
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-tools-devel
BuildRequires:  qt6-svg-devel
# Require the corrected SONAME and Qt development dependencies.
BuildRequires:  libJKQtPlotter-devel >= 5.0.0-alt3.beta2


%{?_with_python3:BuildRequires: pybind11-devel}

%{?_with_openbabel:BuildRequires:  libopenbabel-devel}
%{?_with_hdf5:BuildRequires:  libhdf5-devel}
%{?_with_libarchive:BuildRequires:  libarchive-devel zlib-devel}

%{?_with_spglib:BuildRequires:  libspglib-devel}
%{?_with_libmsym:BuildRequires:  libmsym-devel}

%{?_with_cups:BuildRequires:  libcups-devel}

%{?_with_mmtf:BuildRequires:  libmmtf-devel}

%{?_with_docs:BuildRequires:  make doxygen graphviz}

%{?_with_tests:BuildRequires: ctest libgtest-devel avogadro2-avogadrodata}

%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular modeling,
bioinformatics, materials science, and related areas.

%package -n libavogadro2
Summary: Avogadro2 shared libraries
Group: System/Libraries
Provides: avogadro2-libs = %EVR
Obsoletes: avogadro2-libs < %EVR

%description -n libavogadro2
This package contains the shared libraries for Avogadro2.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: libavogadro2 = %EVR
Requires: eigen3-devel
Requires: qt6-base-devel
Requires: libJKQtPlotter-devel >= 5.0.0-alt3.beta2
# The common CMake export checks the static plugin and libgwavi archives too.
Requires: %name-devel-static = %EVR

%description devel
This package contains libraries and header files for developing
applications that use %name.

%package devel-static
Summary: Static libraries and static plugins for %name
Group: Development/C++

%description devel-static
This package contains static libraries (libgwavi) and static Qt plugins
for developing applications that use %name.


%if_with python3
%package -n python3-module-avogadro
Summary: Python3 bindings for Avogadro2
Group: Development/Python3

%description -n python3-module-avogadro
This package contains Python3 bindings for Avogadro2.
%endif

%if_with docs
%package doc
Summary: HTML documentation of %name
Group: Development/Documentation
BuildArch: noarch

%description doc
HTML documentation of %name.
%endif


%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1


mv thirdparty/libgwavi/README.md thirdparty/libgwavi/README-libgwavi.md

%build

%cmake \
     -DCMAKE_BUILD_TYPE:STRING=Release \
     -DAVOGADRO_RELEASE_BUILD:BOOL=ON \
     -DINSTALL_INCLUDE_DIR:PATH=include/avogadro2 \
     -DINSTALL_LIBRARY_DIR:PATH=%_lib \
     -DCMAKE_MODULE_PATH:PATH=cmake \
     -Wno-dev \
     -DUSE_PYTHON:BOOL=%{with python3} \
     -DENABLE_TESTING:BOOL=%{with tests} \
%if_with tests
     -DAVOGADRO_DATA_ROOT:PATH=%_datadir/avogadro2/avogadrodata \
%endif
     -DENABLE_RPATH:BOOL=OFF \
     -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
     -DQT_VERSION=6 \
     -DBUILD_STATIC_PLUGINS:BOOL=ON \
     -DUSE_MMTF:BOOL=%{with mmtf} \
     -DUSE_HDF5:BOOL=%{with hdf5} \
     -DUSE_SPGLIB:BOOL=%{with spglib} \
     -DUSE_LIBARCHIVE:BOOL=%{with libarchive} \
     -DBUILD_GPL_PLUGINS:BOOL=ON \
%if_with docs
     -DBUILD_DOCUMENTATION:BOOL=%{with docs} \
%endif
     -DUSE_LIBMSYM:BOOL=%{with libmsym} \
     -DUSE_OPENGL:BOOL=%{with opengl} \
%if_with openbabel
     -DOpenBabel3_INCLUDE_DIR:PATH=%_includedir/openbabel3
%endif

%cmake_build

%if_with docs
%cmake_build -t documentation
%endif

%install
%cmake_install
rm -rf %buildroot%_datadir/doc

%if_with tests
%check
QT_QPA_PLATFORM=offscreen %ctest
%endif


%files -n libavogadro2
%doc README.md LICENSE
%_libdir/libAvogadro*.so.%{sover}*

%files devel
%_includedir/avogadro2/
%_libdir/libAvogadro*.so
%_libdir/cmake/avogadrolibs/

%files devel-static
%doc LICENSE thirdparty/libgwavi/README-libgwavi.md
%dir %_libdir/avogadro2
%_libdir/avogadro2/libgwavi.a
%_libdir/avogadro2/staticplugins/

%if_with python3
%files -n python3-module-avogadro
%python3_sitelibdir/avogadro
%endif

%if_with docs
%files doc
%doc %_target_platform/docs/html
%endif

%changelog
* Tue Nov 10 2026 Valentin Sokolov <sova@altlinux.org> 2.1.0-alt1
- Update to version 2.1.0.
- Require public development dependencies and discover Eigen3 in CMake exports.
- Fix empty-molecule CJSON round trips and legacy autosave recovery
  (closes: #59530).
- Preserve empty-document metadata and reject malformed atom arrays.
- Drop upstreamed layer safety and worker cleanup patches.
- Rebase system Python command and OpenBabel library path fixes.
- Fix layer model notification bounds and add regression tests.
- Use test data from the separate avogadro2-avogadrodata package.
- Use separately packaged polymer fragment data.
- Fix QApplication lifetime in the Qt GUI test runner.
- Run the HDF5 append test on a temporary copy of the reference file.
- Add the zlib build dependency for compressed file formats.

* Tue Sep 15 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt2
- Repackage according to Shared Libs Policy:
  + runtime libraries moved to libavogadro2 package;
  + static archives (libgwavi, static plugins) moved to -devel-static;
  + data packages are now required by avogadro2 instead of the library.
- Add venv-fallback patch for Python plugins without pixi.
- Fix OpenBabel plugin discovery: use arch-aware library path (lib64)
  (closes: #59550, #59557).
- Fix SIGSEGV in RWLayerManager when adding layer to empty molecule
  (closes: #59548).
- Remove phantom column 4 from layer panel (closes: #59547).
- Fix dataChanged signal and bounds check in LayerModel.
- Fix worker thread and subprocess leak in geometry optimization.
- Use %%opt_flags instead of hardcoded CFLAGS/CXXFLAGS.
- Add -ffat-lto-objects to LTO flags for packaged static libraries.
- Replace %%prep seds with a patch.
- Update project URL.
- Provide/obsolete avogadro2-libs runtime package in libavogadro2.
- Drop bogus Provides: libwavi-static from devel.
- Enable unit tests.

* Mon Apr 20 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Wed Jan 28 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Update to version 1.102.1.

* Mon Nov 10 2025 Valentin Sokolov <sova@altlinux.org> 1.100.0-alt1
- Initial build for Sisyphus.
