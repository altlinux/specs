%define sover 8.0

Name: qhull
Version: 2020.2
Release: alt4

Summary: General dimension convex hull programs
License: BSD-style
Group: Sciences/Mathematics
Source: %name-%version.tar
Patch0: build-qhullcpp-as-shared-library.patch
Patch1: fix-CMake-target-export.patch
URL: https://github.com/qhull/qhull/wiki
VCS: https://github.com/qhull/qhull

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ gcc-fortran cmake

Conflicts: labplot1.6

%description
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

Rbox is a useful tool in generating input for Qhull; it generates
hypercubes, diamonds, cones, circles, simplices, spirals,
lattices, and random points.

Qhull produces graphical output for Geomview.  This helps with
understanding the output. <http://www.geomview.org>

%package -n libqhull_r%sover
Summary: General dimension convex hull program library
Group: System/Libraries
Obsoletes: libqhull < %EVR

%description -n libqhull_r%sover
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

Rbox is a useful tool in generating input for Qhull; it generates
hypercubes, diamonds, cones, circles, simplices, spirals,
lattices, and random points.

Qhull produces graphical output for Geomview.  This helps with
understanding the output. <http://www.geomview.org>

This package contains the C shared library.

%package -n libqhullcpp%sover
Summary: General dimension convex hull program library
Group: System/Libraries

%description -n libqhullcpp%sover
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

Rbox is a useful tool in generating input for Qhull; it generates
hypercubes, diamonds, cones, circles, simplices, spirals,
lattices, and random points.

Qhull produces graphical output for Geomview.  This helps with
understanding the output. <http://www.geomview.org>

This package contains the the shared C++ library.

%package -n lib%name-devel
Summary: General dimension convex hull program development files.
Group: Development/Other
Requires: libqhull_r%sover = %EVR
Requires: libqhullcpp%sover = %EVR
Obsoletes: %name-devel < %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

Rbox is a useful tool in generating input for Qhull; it generates
hypercubes, diamonds, cones, circles, simplices, spirals,
lattices, and random points.

Qhull produces graphical output for Geomview.  This helps with
understanding the output. <http://www.geomview.org>

This package contains the files for development.

%package doc
Summary: General dimension convex hull program documentation
Group: Sciences/Mathematics
BuildArch: noarch

%description doc
Qhull is a general dimension convex hull program that reads a set
of points from stdin, and outputs the smallest convex set that contains
the points to stdout.  It also generates Delaunay triangulations, Voronoi
diagrams, furthest-site Voronoi diagrams, and halfspace intersections
about a point.

Rbox is a useful tool in generating input for Qhull; it generates
hypercubes, diamonds, cones, circles, simplices, spirals,
lattices, and random points.

Qhull produces graphical output for Geomview.  This helps with
understanding the output. <http://www.geomview.org>

This package contains the HTML documentation.

%prep
%setup
%autopatch -p1

%build
%cmake	-DBUILD_SHARED_LIBS=ON \
	-DBUILD_STATIC_LIBS=OFF \
	-DLINK_APPS_SHARED=ON \
	%nill
%cmake_build

%install
%cmake_install

%files
%doc Announce.txt COPYING.txt File_id.diz README.txt REGISTER.txt
%_bindir/*
%_man1dir/*

%files -n libqhull_r%sover
%_libdir/libqhull_r.so.%sover
%_libdir/libqhull_r.so.%sover.*

%files -n libqhullcpp%sover
%_libdir/libqhullcpp.so.%sover
%_libdir/libqhullcpp.so.%sover.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/cmake/Qhull/QhullTargets.cmake
%_libdir/cmake/Qhull/QhullConfig.cmake
%_libdir/cmake/Qhull/QhullConfigVersion.cmake
%_libdir/cmake/Qhull/QhullTargets-noconfig.cmake
%_pkgconfigdir/*.pc
%_includedir/libqhull
%_includedir/libqhull_r
%_includedir/libqhullcpp

%files doc
%doc %_docdir/%name

%changelog
* Sun Jan 18 2026 Anton Midyukov <antohami@altlinux.org> 2020.2-alt4
- Build libqhullcpp as shared library.
- Disable build static libraries.
- Split libqhull by libqhull_r%%sover and libqhullcpp%%sover subpackages.
- Cleanup spec, update URL, add VCS tag.

* Fri Dec 05 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 2020.2-alt3
- Add libqhullcpp-devel-static and libqhull-devel-static.
- Remove DBUILD_STATIC_LIBS=OFF.

* Thu May 15 2025 Grigory Ustinov <grenka@altlinux.org> 2020.2-alt2
- Fixed FTBFS.

* Tue May 11 2021 Grigory Ustinov <grenka@altlinux.org> 2020.2-alt1
- Build new version.

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 2012.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt1
- Version 2012.1

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.2-alt2
- Disabled RPATH

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.2-alt1
- Version 2011.2

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1
- Version 2011.1

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.1-alt4
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.1-alt3
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.1-alt2
- Added explicit conflict with labplot1.6

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010.1-alt1
- Version 2010.1

* Sat Nov 01 2008 Paul Wolneykien <manowar@altlinux.ru> 2003.1-alt3
- BuildRequires: gcc-c++ gcc-fortran

* Sat Nov 01 2008 Paul Wolneykien <manowar@altlinux.ru> 2003.1-alt2
- Fix of the missing dependence: development to library package.

* Wed Sep 24 2008 Paul Wolneykien <manowar@altlinux.ru> 2003.1-alt1
- Initial release for ALTLinux.
