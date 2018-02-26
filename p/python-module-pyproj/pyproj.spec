%define oname pyproj
Name: python-module-%oname
Version: 1.9.0
Release: alt1.svn20111223.1
Summary: Pyrex generated python interface to PROJ.4 library
License: MIT
Group: Graphics
Url: http://code.google.com/p/pyproj/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pyproj.googlecode.com/svn/trunk
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: libproj-devel python-devel
%setup_python_module %oname

%description
Pyrex generated python interface to PROJ.4 library

Performs cartographic transformations and geodetic computations.

The Proj class can convert from geographic (longitude,latitude) to
native map projection (x,y) coordinates and vice versa, or from one map
projection coordinate system directly to another.

The Geod class can perform forward and inverse geodetic, or Great
Circle, computations. The forward computation involves determining
latitude, longitude and back azimuth of a terminus point given the
latitude and longitude of an initial point, plus azimuth and distance.
The inverse computation involves determining the forward and back
azimuths and distance given the latitudes and longitudes of an initial
and terminus point.

Input coordinates can be given as python arrays, lists/tuples, scalars
or numpy/Numeric/numarray arrays. Optimized for objects that support the
Python buffer protocol (regular python and numpy array objects).

%package tests
Summary: Tests for pyrex generated python interface to PROJ.4 library
Group: Development/Python
Requires: %name = %version-%release

%description tests
Pyrex generated python interface to PROJ.4 library

Performs cartographic transformations and geodetic computations.

This package contains tests for pyrex generated python interface to
PROJ.4 library.

%prep
%setup

%build
%python_build_debug

%install
%python_install

install -d %buildroot%python_sitelibdir/%oname/test
install -p -m644 test/* %buildroot%python_sitelibdir/%oname/test

chmod +x %buildroot%python_sitelibdir/%oname/data/test*

%files
%doc Changelog LICENSE_proj4 README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/%oname/data/test*

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/%oname/data/test*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.0-alt1.svn20111223.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.svn20111223
- Version 1.9.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.9-alt1.svn20110504.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1.svn20110504
- Version 1.8.9

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1.svn20100914.1
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1.svn20100914
- Version 1.8.8

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1.svn20100715
- Version 1.8.7

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1.20091103
- Version 1.8.6
- Extracted tests into separate package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.20090914.1
- Rebuilt with python 2.6

* Fri Sep 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.20090914
- Initial build for Sisyphus

