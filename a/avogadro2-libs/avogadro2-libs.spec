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

# Disable MMTF support (upstream notes that MMTF is no longer maintained)
%def_without mmtf

Name: avogadro2-libs
Version: 2.0.0
Release: alt1

Summary: Avogadro2 libraries
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: http://avogadro.openmolecules.net/
VCS: https://github.com/OpenChemistry/avogadrolibs

Source: %name-%version.tar

Patch0: avogadro2-libs-spglib.cmake.patch
Patch1: avogadro2-libs-fragments-1.102.1.patch
Patch2: avogadro2-insert_modules.patch
Patch3: avogadro2-libs-insertpeptide-1.103.0.patch

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
BuildRequires:  libJKQtPlotter-devel


%{?_with_python3:BuildRequires: pybind11-devel}

%{?_with_openbabel:BuildRequires:  libopenbabel-devel}
%{?_with_hdf5:BuildRequires:  libhdf5-devel}
%{?_with_libarchive:BuildRequires:  libarchive-devel}

%{?_with_spglib:BuildRequires:  libspglib-devel}
%{?_with_libmsym:BuildRequires:  libmsym-devel}

%{?_with_cups:BuildRequires:  libcups-devel}

%{?_with_mmtf:BuildRequires:  libmmtf-devel}

%{?_with_docs:BuildRequires:  make doxygen graphviz}

Requires: avogadro2-avogenerators = %version
Requires: avogadro2-crystals = %version
Requires: avogadro2-molecules = %version


%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular modeling,
bioinformatics, materials science, and related areas.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

Provides: libwavi-static

%description devel
This package contains libraries and header files for developing
applications that use %name.


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


sed -e 's|${AvogadroLibs_SOURCEDATA_DIR}/|${AvogadroLibs_SOURCE_DIR}/|g' -i avogadro/qtplugins/insertfragment/CMakeLists.txt
sed -e 's|${AvogadroLibs_SOURCEDATA_DIR}/|${AvogadroLibs_SOURCE_DIR}/|g' -i avogadro/qtplugins/quantuminput/CMakeLists.txt
sed -e 's|${AvogadroLibs_SOURCEDATA_DIR}/|${AvogadroLibs_SOURCE_DIR}/|g' -i avogadro/qtplugins/templatetool/CMakeLists.txt

mv thirdparty/libgwavi/README.md thirdparty/libgwavi/README-libgwavi.md


%build

%cmake \
     -DCMAKE_BUILD_TYPE:STRING=Release \
     -DINSTALL_INCLUDE_DIR:PATH=include/avogadro2 \
     -DINSTALL_LIBRARY_DIR:PATH=%_lib \
     -DCMAKE_MODULE_PATH:PATH=cmake \
     -Wno-dev \
     -DUSE_PYTHON:BOOL=%{with python3} \
     -DCMAKE_C_FLAGS:STRING='-pipe -frecord-gcc-switches -Wall -g -O2 -flto=auto -ffat-lto-objects' \
     -DCMAKE_CXX_FLAGS:STRING='-pipe -frecord-gcc-switches -Wall -g -O2 -flto=auto -ffat-lto-objects' \
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


%files
%doc README.md LICENSE
%doc thirdparty/libgwavi/README-libgwavi.md
%dir %_libdir/avogadro2
%_libdir/libAvogadro*.so.2
%_libdir/libAvogadro*.so.%version
%_libdir/avogadro2/libgwavi.a
%_libdir/avogadro2/staticplugins/

%files devel
%_includedir/avogadro2/
%_libdir/libAvogadro*.so
%_libdir/cmake/avogadrolibs/

%if_with python3
%files -n python3-module-avogadro
%python3_sitelibdir/avogadro
%endif

%if_with docs
%files doc
%doc %_target_platform/docs/html
%endif

%changelog
* Mon Apr 20 2026 Valentin Sokolov <sova@altlinux.org> 2.0.0-alt1
- Update to version 2.0.0

* Fri Feb 06 2026 Valentin Sokolov <sova@altlinux.org> 1.103.0-alt1
- Update to version 1.103.0.

* Wed Jan 28 2026 Valentin Sokolov <sova@altlinux.org> 1.102.1-alt1
- Update to version 1.102.1.

* Mon Nov 10 2025 Valentin Sokolov <sova@altlinux.org> 1.100.0-alt1
- Initial build for Sisyphus.
