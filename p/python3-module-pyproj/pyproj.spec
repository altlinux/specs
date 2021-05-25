%define oname pyproj

Name: python3-module-%oname
Version: 1.9.6
Release: alt2
Summary: Pyrex generated python interface to PROJ.4 library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyproj/

# https://github.com/jswhit/pyproj.git
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: time
BuildRequires: python3-module-Cython
BuildRequires: /usr/bin/2to3

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
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Pyrex generated python interface to PROJ.4 library

Performs cartographic transformations and geodetic computations.

This package contains tests for pyrex generated python interface to
PROJ.4 library.

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install
install -d %buildroot%python3_sitelibdir/%oname/test
install -p -m644 test/* %buildroot%python3_sitelibdir/%oname/test
chmod +x %buildroot%python3_sitelibdir/%oname/data/test*

%files
%doc Changelog LICENSE* *.md docs
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/%oname/data/test*

%files tests
%python3_sitelibdir/*/test
%python3_sitelibdir/%oname/data/test*

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.6-alt2
- Drop python2 support.

* Fri Apr 12 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.6-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.4-alt3.git20141229.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.4-alt3.git20141229.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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

