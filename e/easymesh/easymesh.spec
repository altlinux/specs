Name: easymesh
Version: 1.4
Release: alt2
Summary: A Two-Dimensional Quality Mesh Generator
License: Free for non-commertial using
Group: Sciences/Mathematics
Url: http://www-dinma.univ.trieste.it/nirftc/research/easymesh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www-dinma.univ.trieste.it/nirftc/research/easymesh/easymesh_1_4.c
# http://www-dinma.univ.trieste.it/nirftc/research/easymesh/easymesh_html.tar.gz
# http://www-dinma.univ.trieste.it/nirftc/research/easymesh/examples.tar.gz
Source: %name-%version.tar
Source1: Makefile

%description
* Generates two dimensional, unstructured, Delaunay and constrained
  Delaunay triangulations in general domains.
* Handles holes in the domain.
* Local refining/coarsening can be achieved easily with different
  techniques.
* Handles domains composed of more than one material.
* Performs renumeration of nodes, elements and sides in order to
  decrease the bandwidth of discretized set of equations (wherever you
  place the unknowns). This renumeration is invoked by default, and
  cannot be switched off by the command line option.
* Has a built-in function for relaxation of grid, in order to avoid the
  creation of nodes surrounded with more than 7 and less than 5
  elements. The result of this technique, combined with Laplacian
  smoothing, is a grid of high quality.
* Performs Laplacian smoothing.
* Uses very simple ASCII file as input.
* Creates three different ASCII output files with all the data which a
  numerical analysist might need.
* If specified by a command line switch, creates a drawing with Delaunay
  and Voronoi mesh in DXF or fig format, so the results of triangulation
  can be viewed with any graphical tool which supports these formats.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
%make_build

%install
%makeinstall_std

%files
%doc html examples
%_bindir/*

%changelog
* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2
- Rebuilt for debuginfo

* Mon Jan 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

