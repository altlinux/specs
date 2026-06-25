#
# Upstream provides static libraries for some of its components, despite
# the fact that static library building is disabled in CMake.
# See https://www.altlinux.org/LTO
#
%define optflags_lto %nil

# aarch64: error: cpio archive too big - 4518M
%ifarch aarch64
%global __find_debuginfo_files %nil
%endif

%global descr IfcOpenShell is an open source (LGPL) software library for working with\
Industry Foundation Classes (IFC). Complete parsing support is provided\
for IFC2x3 TC1, IFC4 Add2 TC1, IFC4x1, IFC4x2, and IFC4x3 Add2.\
Extensive geometric support is implemented for the IFC releases IFC2x3 TC1\
and IFC4 Add2 TC1. Extending with support for arbitrary IFC schemas is\
possible at compile-time when using C++ and at run-time when using Python.

# Upstream prioritizes static libraries. Shared libraries are not packaged
# according to the Shared Libs Policy. Also, not all libraries have a shared
# version; some are still built statically.
%def_without shared

%def_with documentation
%def_with examples

# Required for FreeCAD
%def_with convert
%def_with cgal
%def_with gltf

# i586: E: Couldn't find package OpenUSD-devel
%ifarch %ix86
%def_without hdf5
%else
%def_with hdf5
%endif

%def_with opencascasde
%def_with ifcpython
%def_with ifcgeom

%def_with optimizations
%def_with geomserver

# FTBFS
%def_without wasm
%def_without mmap
%def_without qtviewer
%def_without ifcxml
%def_without relationship_validation

# Not compatible with our version of libproj
%def_without proj
# Requires the rocksdb static library. We only build the shared library
%def_without rocksdb
# libopencollada has been deprecated and is no longer supported in ALT
%def_without collada

Name: ifcopenshell
Version: 0.8.4
Release: alt1

Summary: Open source IFC library and geometry engine
License: LGPL-3.0-or-later AND GPL-3.0-or-later
Group: Engineering
Url: https://ifcopenshell.org/
Vcs: https://github.com/IfcOpenShell/IfcOpenShell.git

Source0: %name-%version.tar
Source1: submodules.tar

BuildRequires: rpm-build-cmake
BuildRequires: boost-devel
BuildRequires: boost-devel-headers
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-program_options-devel
BuildRequires: eigen3-devel
BuildRequires: gcc-c++
BuildRequires: libhdf5-devel
BuildRequires: libsvgpp-devel
BuildRequires: libxml2-devel
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: opencascade-devel
BuildRequires: swig
%{?_with_cgal:BuildRequires: cgal-devel}
%{?_with_ifcpython:BuildRequires: python3-dev}
%{?_with_proj:BuildRequires: libproj-devel}
%{?_with_hdf5:BuildRequires: OpenUSD-devel}
%{?_with_documentation:BuildRequires: doxygen graphviz}
%if_with qtviewer
BuildRequires: qt6-base-devel
BuildRequires: OpenSceneGraph
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libOpenThreads-devel
%endif
%if_with rocksdb
BuildRequires: librocksdb-devel
BuildRequires: rocksdb-tools
BuildRequires: libsnappy-devel
BuildRequires: libgflags-devel
BuildRequires: bzlib-devel
BuildRequires: liblz4-devel
%endif

ExclusiveArch: x86_64 aarch64

%description
%descr

%package -n lib%name-devel
Summary: C++ API for the %name
Group: Development/C++

%description -n lib%name-devel
%summary.
%descr

%package -n python3-module-%name
Summary: Python API for the %name
Group: Development/Python3
# Optional blender addons
%filter_from_requires /python3(OCC)/d
%filter_from_requires /python3(bmesh)/d
%filter_from_requires /python3(bootstrap)/d
%filter_from_requires /python3(bpy.types)/d
%filter_from_requires /python3(codegen)/d
%filter_from_requires /python3(documentation)/d
%filter_from_requires /python3(header)/d
%filter_from_requires /python3(mapping)/d
%filter_from_requires /python3(mathutils)/d
%filter_from_requires /python3(mvdxml_expression)/d
%filter_from_requires /python3(nodes)/d

%description -n python3-module-%name
%summary.
%descr

%prep
%setup -a1

%build
pushd cmake
%cmake -G Ninja \
	-DCMAKE_CXX_STANDARD=17 -DCMAKE_CXX_EXTENSIONS=ON \
	-DCMAKE_CXX_FLAGS="-Wno-error=return-type" \
%ifnarch aarch64
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%else
	-DCMAKE_BUILD_TYPE=Release \
%endif
	-DWASM_BUILD=%{with wasm} \
	-DBUILD_SHARED_LIBS=%{with shared} \
	-DUSE_MMAP=%{with mmap} \
	-DBUILD_IFCGEOM=%{with ifcgeom} \
	-DBUILD_IFCPYTHON=%{with ifcpython} \
	-DBUILD_CONVERT=%{with convert} \
	-DBUILD_EXAMPLES=%{with examples} \
	-DBUILD_GEOMSERVER=%{with geomserver} \
	-DBUILD_QTVIEWER=%{with qtviewer} \
	-DWITH_OPENCASCASE=%{with opencascade} \
	-DWITH_CGAL=%{with cgal} \
	-DCOLLADA_SUPPORT=%{with collada} \
	-DGLTF_SUPPORT=%{with gltf} \
	-DHDF5_SUPPORT=%{with hdf5} \
	-DWITH_PROJ=%{with proj} \
	-DIFCXML_SUPPORT=%{with ifcxml} \
	-DWITH_RELATIONSHIP_VALIDATION=%{with relationship_validation} \
	-DWITH_ROCKSDB=%{with rocksdb} \
%nil
%cmake_build
popd

%if_with documentation
# Read the docs/cpp-api/README.md
pushd docs/cpp-api
doxygen
# Documentation too large
cd output && tar cJfv %name-%version.tar.xz html
popd
%endif

%install
pushd cmake
%cmake_install
popd

%files
%_bindir/IfcConvert
%_bindir/svgfill
%_bindir/IfcGeomServer

%files -n lib%name-devel
%_includedir/ifcparse
%_includedir/ifcgeom
%_includedir/serializers
%_includedir/graph_2d.h
%_includedir/progress.h
%_includedir/svgfill.h
%_libdir/libIfcGeom.a
%_libdir/libIfcParse.a
%_libdir/libSerializers*.a
%_libdir/libgeometry*.a
%_libdir/libsvgfill.a
%if_with documentation
%doc docs/cpp-api/output/%name-%version.tar.xz
%endif

%files -n python3-module-%name
%python3_sitelibdir/%name

%changelog
* Mon Jun 08 2026 Ulysses Apokin <ulysses@altlinux.org> 0.8.4-alt1
- Initial build for Sisyphus.
