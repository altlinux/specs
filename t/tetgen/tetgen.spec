Name: tetgen
Version: 1.4.3
Release: alt5
Summary: Tetrahedral Mesh Generator and Three-Dimensional Delaunay Triangulator
License: BSD-like
Group: Sciences/Mathematics
Url: http://tetgen.berlios.de/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.wias-berlin.de/people/si/tetgen1.4.3.tar.gz
Source1: http://tetgen.berlios.de/files/tetgen-manual.pdf

BuildPreReq: gcc-c++

%description
TetGen generates the Delaunay tetrahedralization, Voronoi diagram, constrained
Delaunay tetrahedralizations and quality tetrahedral meshes. The main goal of
TetGen is to generate suitable meshes for solving partial differential equations
by finite element or finite volume methods. The following pictures respectively
illustrate an input - a piecewise linear complex (left), a boundary conforming
Delaunay tetrahedral mesh (middle) and its dual - a Voronoi diagram (right).

There is also executable file - TetView - for view diagrams of TetGen, but it's
without public sources. You may get it from
http://www.wias-berlin.de/people/si/files/tetview-linux.gz

%package -n lib%name
Summary: Tetgen shared library
Group: System/Libraries

%description -n lib%name
TetGen generates the Delaunay tetrahedralization, Voronoi diagram, constrained
Delaunay tetrahedralizations and quality tetrahedral meshes. The main goal of
TetGen is to generate suitable meshes for solving partial differential equations
by finite element or finite volume methods. The following pictures respectively
illustrate an input - a piecewise linear complex (left), a boundary conforming
Delaunay tetrahedral mesh (middle) and its dual - a Voronoi diagram (right).

This package contains Tetgen shared library for another projects.

%package -n lib%name-devel
Summary: Development files for TetGen library
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
TetGen generates the Delaunay tetrahedralization, Voronoi diagram, constrained
Delaunay tetrahedralizations and quality tetrahedral meshes. The main goal of
TetGen is to generate suitable meshes for solving partial differential equations
by finite element or finite volume methods. The following pictures respectively
illustrate an input - a piecewise linear complex (left), a boundary conforming
Delaunay tetrahedral mesh (middle) and its dual - a Voronoi diagram (right).

This package contains development files for TetGen library.

%package -n lib%name-devel-static
Summary: Static library of TetGen
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
TetGen generates the Delaunay tetrahedralization, Voronoi diagram, constrained
Delaunay tetrahedralizations and quality tetrahedral meshes. The main goal of
TetGen is to generate suitable meshes for solving partial differential equations
by finite element or finite volume methods. The following pictures respectively
illustrate an input - a piecewise linear complex (left), a boundary conforming
Delaunay tetrahedral mesh (middle) and its dual - a Voronoi diagram (right).

This package contains static library of TetGen.

%package -n lib%name-doc
Summary: Documentation for TetGen
Group: Documentation
BuildArch: noarch

%description -n lib%name-doc
TetGen generates the Delaunay tetrahedralization, Voronoi diagram, constrained
Delaunay tetrahedralizations and quality tetrahedral meshes. The main goal of
TetGen is to generate suitable meshes for solving partial differential equations
by finite element or finite volume methods. The following pictures respectively
illustrate an input - a piecewise linear complex (left), a boundary conforming
Delaunay tetrahedral mesh (middle) and its dual - a Voronoi diagram (right).

This package contains manual of TetGen.

%prep
%setup

%build
%make_build tetgen tetlib
%make_build spredicates.o
%make_build libtetgen.so

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -d %buildroot%_docdir/%name
install -m755 %name %buildroot%_bindir
install -m644 *.so* *.a %buildroot%_libdir
ln -s lib%name.so.0 %buildroot%_libdir/lib%name.so
install -m644 %name.h %buildroot%_includedir
install -m644 %SOURCE1 %buildroot%_docdir/%name

%files
%doc LICENSE example.poly
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-doc
%_docdir/%name

%changelog
* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt5
- Upstream update on 2011/01/19

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt4
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt3
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt2
- Rebuilt for soname set-versions

* Sat Dec 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Sat Jun 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt2
- Rebuild with PIC

* Thu Apr 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

