Name: admesh
Summary: A program for processing triangulated solid meshes
Version: 0.95
Release: alt2
Group: Graphics
License: GPL v2
URL: http://www.varlog.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.varlog.com/admesh-0.95.tar.gz

%description
ADMesh is a program for processing triangulated solid meshes. Currently,
ADMesh only reads the STL file format that is used for rapid prototyping
applications, although it can write STL, VRML, OFF, and DXF files.

Features:
---------

 * Read and write binary and ASCII STL files
 * Check STL files for flaws (i.e. unconnected facets, bad normals)
 * Repair facets by connecting nearby facets that are within a given tolerance
 * Fill holes in the mesh by adding facets.
 * Repair normal directions (i.e. facets should be CCW)
 * Repair normal values (i.e. should be perpendicular to facet with length=1)
 * Remove degenerate facets (i.e. facets with 2 or more vertices equal)
 * Translate in x, y, and z directions
 * Rotate about the x, y, and z axes
 * Mirror about the xy, yz, and xz planes
 * Scale the part by a factor
 * Merge 2 STL files into one
 * Write an OFF file 
 * Write a VRML file 
 * Write a DXF file 
 * Calculate the volume of a part

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
install -d %buildroot%_bindir
install -m755 %name %buildroot%_bindir

%files
%doc ADMESH.DOC COPYING ChangeLog README *.stl
%_bindir/*

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt2
- Rebuilt for debuginfo

* Fri Jun 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt1
- Initial build for Sisyphus

