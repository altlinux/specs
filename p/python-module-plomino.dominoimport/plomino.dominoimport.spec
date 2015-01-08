%define mname plomino
%define oname %mname.dominoimport
Name: python-module-%oname
Version: 0.2
Release: alt1.git20120326
Summary: Import domino database from DXL files
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plomino.dominoimport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plomino/plomino.dominoimport.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2
BuildPreReq: python-module-Products.CMFPlomino
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.untrustedpython

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlomino zope.interface

%description
Allows to import Lotus Notes Domino database (design + documents) into
Plomino.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Allows to import Lotus Notes Domino database (design + documents) into
Plomino.

This package contains tests for %oname.

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
py.test %mname/dominoimport/tests/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20120326
- Initial build for Sisyphus

