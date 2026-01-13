%define somver 8
%define sover %somver.0.2
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: qhull
Version: 2020.2
Release: alt3

Summary: General dimension convex hull programs
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
License: BSD-style
Group: Sciences/Mathematics
Source: %name-%version.tar.gz
URL: http://www.qhull.org/
Requires: lib%name = %version-%release

# Automatically added by buildreq on Sat Nov 01 2008
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

%package -n lib%name
Summary: General dimension convex hull program library
Group: Sciences/Mathematics
Obsoletes: %name-lib < %version-%release
Provides: %name-lib = %version-%release

%description -n lib%name
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

This package contains the dynamic library files.

%package -n lib%name-devel
Summary: General dimension convex hull program development files.
Group: Sciences/Mathematics
Requires: lib%name = %version-%release
Obsoletes: %name-devel < %version-%release
Provides: %name-devel = %version-%release

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

%package -n lib%{name}cpp-devel-static
Summary:        Development and documentation files for qhull - C++ interface
Group:          Sciences/Mathematics
Requires:       %name = %version

%description -n lib%{name}cpp-devel-static
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files and static lib for Qhull's C++ interface.


%package -n lib%name-devel-static
Summary:        Development and documentation files for qhull
Group:          Sciences/Mathematics
Requires:       %name = %version

%description -n lib%name-devel-static
Qhull computes the convex hull, Delaunay triangulation, Voronoi diagram,
halfspace intersection about a point, furthest-site Delaunay triangulation,
and furthest-site Voronoi diagram.

This package contains the header files and static lib for Qhull's.

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

%build
export CFLAGS="%optflags_shared"
export CXXFLAGS="%optflags_shared"
%cmake \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    %if %_lib == lib64
    -DLIB_SUFFIX:STRING=64 \
    %endif
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%prefix \
    -DINCLUDE_INSTALL_DIR="%_includedir" \
    -DLIB_INSTALL_DIR="%_libdir" \
    -DBIN_INSTALL_DIR="%_bindir" \
    -DMAN_INSTALL_DIR="%_mandir/man1/" \
    .
%cmake_build

%install
%cmake_install

# Fixup wrong location
%if "%_lib" != "lib"
    mv %buildroot%_prefix/lib/cmake %buildroot%_libdir/
    mv %buildroot%_prefix/lib/pkgconfig %buildroot%_libdir/
%endif

%files
%doc Announce.txt COPYING.txt File_id.diz README.txt REGISTER.txt
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/cmake/Qhull/QhullTargets.cmake
%_libdir/cmake/Qhull/QhullConfig.cmake
%_libdir/cmake/Qhull/QhullConfigVersion.cmake
%_libdir/cmake/Qhull/QhullTargets-noconfig.cmake
%_pkgconfigdir/qhull_r.pc
%_includedir/libqhull
%_includedir/libqhull_r

%files -n lib%name-devel-static
%_libdir/libqhullstatic.a
%_libdir/libqhullstatic_r.a
%_libdir/pkgconfig/qhullstatic.pc
%_libdir/pkgconfig/qhullstatic_r.pc

%files -n lib%{name}cpp-devel-static
%_includedir/libqhullcpp/
%_libdir/libqhullcpp.a
%_libdir/pkgconfig/qhullcpp.pc

%files doc
%doc %_docdir/%name

%changelog
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
