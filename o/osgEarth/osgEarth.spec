%define osg_version %(pkg-config --modversion openscenegraph)

Name: osgEarth
Version: 2.1.1
Release: alt1

Summary: Dynamic map generation toolkit for OpenSceneGraph
License: LGPL
#Group: System/Libraries
Group: Graphics

Url: http://osgearth.org
Source: %name-%version.tar
Packager: Dmitry Derjavin <dd@altlinux.org>

# Automatically added by buildreq on Wed Sep 22 2010
BuildRequires: cmake gcc-c++ libGL-devel libOpenSceneGraph-devel libXrandr-devel libXrender-devel libXt-devel libcurl-devel libexpat-devel libgdal-devel libgeos-devel libsqlite3-devel libzip-devel
BuildRequires: libGLU-devel
BuildRequires: /usr/bin/osgversion

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
#Requires: %_libdir/osgPlugins-%osg_version

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

%build
mkdir BUILD
pushd BUILD
cmake -DCMAKE_BUILD_TYPE="Release" -DCMAKE_INSTALL_PREFIX:PATH=%_usr ..
%make_build VERBOSE=1
popd

%install
pushd BUILD
%makeinstall_std
# Supposed to take data files
mkdir -p %buildroot%_datadir/osgEarth
cp -a ../data ../tests %buildroot%_datadir/osgEarth
popd

%files -n lib%name
%doc README.txt
%_libdir/libosgEarth*.so.*
%_libdir/osgPlugins-%osg_version/*

%files -n lib%name-devel
%_includedir/osg*
%_libdir/libosg*.so

%files examples

%_bindir/osgearth_annotation
%_bindir/osgearth_cache
%_bindir/osgearth_clouds
%_bindir/osgearth_composite
%_bindir/osgearth_controls
%_bindir/osgearth_elevation
%_bindir/osgearth_featureeditor
%_bindir/osgearth_featureinfo
%_bindir/osgearth_features
%_bindir/osgearth_imageoverlay
%_bindir/osgearth_labels
%_bindir/osgearth_manip
%_bindir/osgearth_map
%_bindir/osgearth_measure
%_bindir/osgearth_ocean
%_bindir/osgearth_shadercomp
%_bindir/osgearth_tilesource
%_bindir/osgearth_toc
%_bindir/osgearth_version
%_bindir/osgearth_viewer

%files data
%_datadir/osgEarth

%changelog
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
