Name: xd3d
Version: 8.3.1
Release: alt5
Summary: Scientific Visualization Tool
License: GPLv2
Group: Graphics
Url: http://www.cmap.polytechnique.fr/~jouve/xd3d/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: csh gcc-fortran libX11-devel zlib-devel libXpm-devel

%description
xd3d is a simple scientific visualization tool designed to be easy to
learn. It can plot 2d and 3d meshes, with shadowing, contour plots,
vector fields, iso-contour (3d), as well as 3d surfaces z=f(x,y) defined
by an algebraic expression or a cloud of points. It generates high
quality vector PostScript files for scientific publications and still or
animated bitmap images. It includes the graph plotter xgraphic.

%package examples
Summary: Examples for xd3d
Group: Documentation
BuildArch: noarch

%description examples
xd3d is a simple scientific visualization tool designed to be easy to
learn. It can plot 2d and 3d meshes, with shadowing, contour plots,
vector fields, iso-contour (3d), as well as 3d surfaces z=f(x,y) defined
by an algebraic expression or a cloud of points. It generates high
quality vector PostScript files for scientific publications and still or
animated bitmap images. It includes the graph plotter xgraphic.

This package contains examples for xd3d.

%package docs
Summary: Documentation for xd3d
Group: Documentation
BuildArch: noarch

%description docs
xd3d is a simple scientific visualization tool designed to be easy to
learn. It can plot 2d and 3d meshes, with shadowing, contour plots,
vector fields, iso-contour (3d), as well as 3d surfaces z=f(x,y) defined
by an algebraic expression or a cloud of points. It generates high
quality vector PostScript files for scientific publications and still or
animated bitmap images. It includes the graph plotter xgraphic.

This package contains documentation for xd3d.

%prep
%setup
cp -f RULES.linux_gfortran RULES
sed -i "s|@TOPDIR@|$PWD|" RULES
sed -i "s|@BUILDROOT@|%buildroot|" RULES
mkdir lib

%build
./makedeps
%make_build

%install
%makeinstall_std

sed -i 's|%buildroot||g' RULES

%files
%doc BUGS CHANGELOG FAQ FORMATS LICENSE README RULES*
%_bindir/*

%files examples
%doc Examples

%files docs
%doc Manuals

%changelog
* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.1-alt5
- Rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.1-alt4
- Rebuilt for soname set-versions

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.1-alt3
- Removed paths to buildroot

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.1-alt2
- Fixed unsafe-tmp-usage-in-scripts

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.3.1-alt1
- Initial build for Sisyphus

