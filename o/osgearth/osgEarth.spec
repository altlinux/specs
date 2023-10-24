%define osg_version %(pkg-config --modversion openscenegraph)

Name: osgearth
Version: 3.5
Release: alt1

Summary: Dynamic map generation toolkit for OpenSceneGraph
License: LGPL-3.0 with exceptions
Group: Graphics

Url: http://osgearth.org
Source: %name-%version.tar
Source1: submodules.tar
Patch1: osgearth-alt-fix-pathes.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: libGL-devel
BuildRequires: libGLEW-devel
BuildRequires: libGLU-devel
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libgdal-devel
BuildRequires: libgeos-devel
BuildRequires: libprotobuf-devel
BuildRequires: libsqlite3-devel
BuildRequires: libwebp-devel
BuildRequires: libzip-devel
BuildRequires: libzip-utils
BuildRequires: protobuf-compiler
BuildRequires: rapidjson-devel

Provides: osgEarth = %EVR
Obsoletes: osgEarth < %EVR

%description
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

%package -n lib%name
Summary: Runtime libraries for osgEarth
Group: System/Libraries
Provides: libosgEarth = %EVR
Obsoletes: libosgEarth < %EVR

%description -n lib%name
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains runtime libraries for osgEarth.

%package -n lib%name-devel
Summary: Development files for osgEarth
Group: Development/C++
Requires: lib%name = %version-%release
Provides: libosgEarth-devel = %EVR
Obsoletes: libosgEarth-devel < %EVR

%description -n lib%name-devel
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains development files for osgEarth.

%package examples
Summary: Sample applications for osgEarth
Group: Development/Documentation
Requires: %name-data
Provides: osgEarth-examples = %EVR
Obsoletes: osgEarth-examples < %EVR

%description examples
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains sample applications for osgEarth.

%package data
Summary: Sample data files for osgEarth
Group: Development/Documentation
BuildArch: noarch
Provides: osgEarth-data = %EVR
Obsoletes: osgEarth-data < %EVR

%description data
osgEarth is a scalable terrain rendering toolkit for
OpenSceneGraph. Just create a simple XML file, point it at your
imagery, elevation, and vector data, load it into your favorite OSG
application, and go! osgEarth supports all kinds of data and comes
with lots of examples to help you get up and running quickly and
easily.

This package contains sample data files for osgEarth.

%prep
%setup
tar xf %SOURCE1
%patch1 -p1
# Remove non-free content
rm -rf data/loopix
 
# Disable fastdxt driver on non x86 arches, requires x86 intrinsics
%ifnarch x86_64
sed -i 's|add_subdirectory(fastdxt)|# add_subdirectory(fastdxt)|' src/osgEarthDrivers/CMakeLists.txt
%endif

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
# OpenSceneGraph debuginfo too large now => unmets
%global __find_debuginfo_files %nil
%endif
%cmake \
       -Wno-dev \
       -DCMAKE_BUILD_TYPE="Release"
%cmake_build

%install
%cmakeinstall_std
# Supposed to take data files
mkdir -p %buildroot%_datadir/osgEarth
cp -a data tests %buildroot%_datadir/osgEarth

%files -n lib%name
%doc README.md
%_libdir/libosgEarth*.so.*
%_libdir/osgPlugins-*/osgdb_*.so

%files -n lib%name-devel
%_includedir/osg*
%_libdir/libosg*.so
%_datadir/cmake/osgEarthConfig*.cmake

%files examples
%_bindir/*

%files data
%_datadir/osgEarth

%changelog
* Tue Oct 24 2023 Andrey Cherepanov <cas@altlinux.org> 3.5-alt1
- New version.

* Wed May 17 2023 Andrey Cherepanov <cas@altlinux.org> 3.4-alt1
- New version.

* Sat Apr 30 2022 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version.
- Renamed to osgearth.

* Wed Jan 19 2022 Andrey Cherepanov <cas@altlinux.org> 3.2-alt3
- Rebuild with geos-3.10.
- Build from upstream git tag.
- Use cmake macros.

* Wed Oct 27 2021 Michael Shigorin <mike@altlinux.org> 3.2-alt2
- E2K: avoid OSG debuginfo unmets

* Tue Aug 10 2021 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.

* Mon Dec 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version.

* Tue Jun 16 2020 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- New version.

* Tue Mar 03 2020 Grigory Ustinov <grenka@altlinux.org> 2.10.2-alt3
- Fix build with gdal 3.0.4.

* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 2.10.2-alt2
- ensure our CXXFLAGS instead of hardwired -O2
- E2K: explicit -std=c++11

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 2.10.2-alt1
- New version.

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 2.10.1-alt1
- New version.

* Fri Nov 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.10-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.9-alt3.gitbc65245
- NMU: Use upstream fix for geos 3.7.0.

* Sat Jun 23 2018 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt2
- NUM: rebuild against OpenSceneGraph 3.4.1

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.9-alt1
- New version.
- Drop obsoleted patch.

* Fri Aug 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.8-alt1
- New version
- Add GEOS >= 3.6.0 compatibility from upsteam commit

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.7-alt2
- Rebuild with geos 3.6.2

* Thu Oct 01 2015 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- 2.7 built against OpenSceneGraph 3.4.0

* Wed Sep 30 2015 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1.5
- rebuilt against current OpenSceneGraph

* Tue Jul 29 2014 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1.4
- rebuilt against OpenSceneGraph 3.2.1

* Thu Jul 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.3
- Rebuilt with updated geos

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.2
- Rebuilt with updated geos

* Thu Sep 26 2013 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1.1.1
- rebuilt against OpenSceneGraph 3.2.0

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.1
- Rebuilt with updated geos

* Wed Apr 18 2012 Dmitry Derjavin <dd@altlinux.org> 2.1.1-alt1
- 2.1.1

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2.1
- Rebuilt with geos 3.4.0

* Wed Nov 30 2011 Dmitry Derjavin <dd@altlinux.org> 2.1-alt2
- /usr/bin/osgversion dependency added (thanks to iv@);
- osgdb_osgearth moved to osgPlugins;
- examples updated.

* Tue Oct 04 2011 Dmitry Derjavin <dd@altlinux.org> 2.1-alt1
- 2.1

* Wed Dec 22 2010 Dmitry Derjavin <dd@altlinux.org> 1.4.1-alt2
- libGLU-devel added to BuildRequires.

* Wed Sep 22 2010 Dmitry Derjavin <dd@altlinux.org> 1.4.1-alt1
- Initial ALTLinux build.
