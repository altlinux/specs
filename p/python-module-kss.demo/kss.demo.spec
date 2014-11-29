%define mname kss
%define oname %mname.demo
Name: python-module-%oname
Version: 1.4.6
Release: alt1
Summary: KSS (Kinetic Style Sheets) demo
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/kss.demo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-elementtree
BuildPreReq: python-module-kss.core-tests
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.publisher
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component zope.app.component zope.interface
%py_requires zope.publisher zope.schema zope.app.publisher
%py_requires zope.configuration kss.core

%description
KSS (Kinetic Style Sheets) demo.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires kss.core.tests zope.testing

%description tests
KSS (Kinetic Style Sheets) demo.

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

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/tests

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/tests

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.6-alt1
- Initial build for Sisyphus

