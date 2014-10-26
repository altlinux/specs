%define mname collective.ptg
%define oname %mname.flickr
Name: python-module-%oname
Version: 1.0
Release: alt1.git20130901
Summary: Adds flickr support to truegallery
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.ptg.flickr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.ptg.flickr.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-flickrapi
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-collective.plonetruegallery-tests
BuildPreReq: python-module-initgroups
BuildPreReq: python-module-unittest2

%py_provides %oname
%py_requires %mname plone.app.z3cform collective.plonetruegallery

%description
Add on collective.plonetruegallery to aggregate from flickr.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.plonetruegallery.tests

%description tests
Add on collective.plonetruegallery to aggregate from flickr.

This package contains tests for %oname

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/collective/ptg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/ptg/*/tests

%files tests
%python_sitelibdir/collective/ptg/*/tests

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20130901
- Initial build for Sisyphus

