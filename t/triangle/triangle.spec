Name: triangle
Version: 1.6
Release: alt7
Summary: A Two-Dimensional Quality Mesh Generator and Delaunay Triangulator
 
License: MIT
Group: Sciences/Mathematics
Url: http://www.netlib.org/voronoi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.netlib.org/voronoi/triangle.zip

BuildPreReq: libX11-devel glibc-devel /usr/bin/unzip

%description
Triangle generates exact Delaunay triangulations, constrained Delaunay
triangulations, conforming Delaunay triangulations, Voronoi diagrams, and
high-quality triangular meshes.  The latter can be generated with no small
or large angles, and are thus suitable for finite element analysis.
Show Me graphically displays the contents of the geometric files used by
Triangle.  Show Me can also write images in PostScript form.

Information on the algorithms used by Triangle, including complete
references, can be found in the comments at the beginning of the triangle.c
source file.  Another listing of these references, with PostScript copies
of some of the papers, is available from the Web page

    http://www.cs.cmu.edu/~quake/triangle.research.html

%package -n lib%name
Summary: Triangle shared library
Group: System/Libraries

%description -n lib%name
Triangle generates exact Delaunay triangulations, constrained Delaunay
triangulations, conforming Delaunay triangulations, Voronoi diagrams, and
high-quality triangular meshes.  The latter can be generated with no small
or large angles, and are thus suitable for finite element analysis.
Show Me graphically displays the contents of the geometric files used by
Triangle.  Show Me can also write images in PostScript form.

This package contains Triangle shared library.

%package -n lib%name-devel
Summary: Development files for Triangle library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Triangle generates exact Delaunay triangulations, constrained Delaunay
triangulations, conforming Delaunay triangulations, Voronoi diagrams, and
high-quality triangular meshes.  The latter can be generated with no small
or large angles, and are thus suitable for finite element analysis.
Show Me graphically displays the contents of the geometric files used by
Triangle.  Show Me can also write images in PostScript form.

This package contains development files for Triangle library.

%package -n lib%name-devel-static
Summary: Static Triangle library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Triangle generates exact Delaunay triangulations, constrained Delaunay
triangulations, conforming Delaunay triangulations, Voronoi diagrams, and
high-quality triangular meshes.  The latter can be generated with no small
or large angles, and are thus suitable for finite element analysis.
Show Me graphically displays the contents of the geometric files used by
Triangle.  Show Me can also write images in PostScript form.

This package contains static Triangle library.

%prep
%setup

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -m755 %name showme tricall %buildroot%_bindir
install -m644 *.so* *.a %buildroot%_libdir
install -m644 %name.h %buildroot%_includedir/%name
ln -s lib%name.so.0.0.0 %buildroot%_libdir/lib%name.so.0
ln -s lib%name.so.0 %buildroot%_libdir/lib%name.so

%files
%doc README triangle.c A.poly
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%changelog
* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt7
- Added necessary definitions in %_includedir/triangle/triangle.h
- Disabled devel-static subpackage

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt6
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt5
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt4
- Rebuilt for soname set-versions

* Sat Jun 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt3
- Rebuild with optimization and PIC

* Thu Apr 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2
- Move header into %_includedir/%name

* Thu Apr 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

