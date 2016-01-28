%define oname pyproj

%def_with python3

Name: python-module-%oname
Version: 1.9.4
Release: alt3.git20141229.1
Summary: Pyrex generated python interface to PROJ.4 library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyproj/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jswhit/pyproj.git
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
#BuildPreReq: libproj-devel python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
#BuildPreReq: python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 python3-devel rpm-build-python3 time

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

%package -n python3-module-%oname
Summary: Pyrex generated python interface to PROJ.4 library
Group: Development/Python3

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for pyrex generated python interface to PROJ.4 library
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Pyrex generated python interface to PROJ.4 library

Performs cartographic transformations and geodetic computations.

This package contains tests for pyrex generated python interface to
PROJ.4 library.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
install -d %buildroot%python_sitelibdir/%oname/test
install -p -m644 test/* %buildroot%python_sitelibdir/%oname/test
chmod +x %buildroot%python_sitelibdir/%oname/data/test*

%if_with python3
pushd ../python3
%python3_install
install -d %buildroot%python3_sitelibdir/%oname/test
install -p -m644 test/* %buildroot%python3_sitelibdir/%oname/test
chmod +x %buildroot%python3_sitelibdir/%oname/data/test*
popd
%endif

%files
%doc Changelog LICENSE* *.md docs
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/%oname/data/test*

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/%oname/data/test*

%if_with python3
%files -n python3-module-%oname
%doc Changelog LICENSE* *.md docs
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/%oname/data/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%python3_sitelibdir/%oname/data/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt3.git20141229.1
- NMU: Use buildreq for BR.

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt3.git20141229
- New snapshot

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt2.svn20131105
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.svn20131105
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.svn20130619
- Version 1.9.4

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1.svn20130125
- Version 1.9.3

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

