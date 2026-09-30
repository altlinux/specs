%define _unpackaged_files_terminate_build 1
%define sover 4.3
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%ifarch %ix86
%def_without check
%else
%def_with check
%endif

Name: mapnik
Version: 4.3.2
Release: alt1

Summary: An open source toolkit for developing mapping applications
License: LGPL-2.1-or-later
Group: Engineering
URL: http://mapnik.org/
VCS: https://github.com/mapnik/mapnik

Source: %name-%version.tar
# gitmodules
Source1: test_data.tar
Source2: test_data-visual.tar
Source3: deps_mapbox_variant.tar
Source4: deps_mapbox_geometry.tar
Source5: deps_mapbox_polylabel.tar
Source6: deps_mapbox_mapnik-vector-tile.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: boost-devel-headers
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-context-devel
BuildRequires: boost-interprocess-devel
BuildRequires: boost-geometry-devel
BuildRequires: boost-msm-devel
BuildRequires: boost-beast-devel
BuildRequires: boost-lockfree-devel
BuildRequires: boost-locale-devel
BuildRequires: libicu-devel
BuildRequires: zlib-devel
BuildRequires: libfreetype-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: libproj-devel
BuildRequires: libcairo-devel
BuildRequires: postgresql-devel
BuildRequires: libgdal-devel
BuildRequires: libsqlite3-devel
BuildRequires: libxml2-devel
BuildRequires: libavif-devel
BuildRequires: libssl-devel
BuildRequires: qt6-base-devel
BuildRequires: protozero-devel
BuildRequires: sparsehash-devel
%if_with check
BuildRequires: ctest
BuildRequires: catch2-devel
%endif

%description
Mapnik is an open source toolkit for developing mapping applications.
At the core is a C++ shared library providing algorithms and patterns
for spatial data access and visualization.

Mapnik is basically a collection of geographic objects like maps, layers,
datasources, features, and geometries. The library doesn't rely on any
OS specific "windowing systems" and it can be deployed to any server
environment. It is intended to play fair in a multi-threaded environment
and is aimed primarily, but not exclusively, at web-based development.

%package -n lib%name%sover
Summary: %summary
Group: System/Libraries

%description -n lib%name%sover
%summary.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
%summary.

%package common
Summary: Mapnik common files
Group: Other
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-dejavu-lgc

%description common
%summary.

%package plugins
Summary: Plugins for %name
Group: Other
Requires: lib%name%sover = %EVR
Requires: %name-common = %EVR

%description plugins
%summary.

%package utils
Summary: Mapnik visualization and demo utilities
Group: Engineering
Requires: lib%name%sover = %EVR
Requires: %name-common = %EVR

%description utils
%summary.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
%summary.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6
%autopatch -p1
rm -r deps/mapnik/sparsehash

%build
%cmake \
    -DBUILD_TESTING=%{?_with_check:ON}%{!?_with_check:OFF} \
    -DFONTS_INSTALL_DIR=share/fonts \
    -DUSE_EXTERNAL_MAPBOX_PROTOZERO=ON
%cmake_build

%install
%cmake_install

# trash cleanup
rm -r %buildroot%_bindir/viewer.ini %buildroot%_datadir/fonts

%check
%ctest

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_libdir/lib%{name}json.a
%_libdir/lib%{name}wkt.a
%_libdir/lib%name.so
%_includedir/%name
%_libdir/cmake/%name
%_pkgconfigdir/lib%{name}*.pc

%files common
%dir %_libdir/%name

%files plugins
%_libdir/%name/input

%files utils
%_bindir/geometry_to_wkb
%_bindir/mapnik-index
%_bindir/mapnik-render
%_bindir/mapnik-viewer
%_bindir/pgsql2sqlite
%_bindir/shapeindex
%_bindir/svg2png

%files doc
%doc AUTHORS.md COPYING README.md CHANGELOG.md docs/

%changelog
* Wed Sep 30 2026 Valery Zabrovsky <brow@altlinux.org> 4.3.2-alt1
- Revive the package with version 4.3.2.
- Switch to CMake build.
- Apply Shared Libs Policy to libmapnik.
- Add check section.

* Tue Sep 17 2013 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.1-alt3.3.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Mon Nov 26 2012 Ivan A. Melnikov <iv@altlinux.org> 2.0.1-alt3.3
- Rebuilt with Boost 1.52.0

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt3.2
- Rebuilt with libpng15

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt3.1
- Rebuilt with Boost 1.51.0

* Fri Apr 27 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt3
- really fix plugin path in python bindings

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt2
- fix plugins path in python module
- fix requires to fonts

* Thu Apr 19 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus
