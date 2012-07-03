%define somver 6
%define sover %somver.2.1.1446

Name: qhull
Version: 2012.1
Release: alt1

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
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	.
%make_build

%install
%makeinstall_std

install -m755 user_eg* %buildroot%_bindir

ln -s %_includedir/lib%name %buildroot%_includedir/%name

%pre -n lib%name-devel
rm -fR %_includedir/%name

%files
%doc Announce.txt COPYING.txt File_id.diz README.txt REGISTER.txt
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files doc
%doc %_docdir/%name

%changelog
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
