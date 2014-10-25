%define oname plumber
Name: python-module-%oname
Version: 1.4
Release: alt1.dev0.git20140806
Summary: An alternative to mixin-based extension of classes
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/plumber/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/plumber.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-interlude
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.deprecation

%py_provides %oname
%py_requires zope.interface

%description
Plumbing is an alternative to mixin-based extension of classes. In
motivation an incomplete list of limitations and/or design choices of
python's subclassing are given along with plumber's solutions for them.
The plumbing system is described in detail with code examples. Some
design choices and ongoing discussions are explained. Finally, in
miscellanea you find nomenclature, coverage report, list of
contributors, changes and some todos. All non-experimental features are
fully test covered.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing zope.deprecation

%description tests
Plumbing is an alternative to mixin-based extension of classes. In
motivation an incomplete list of limitations and/or design choices of
python's subclassing are given along with plumber's solutions for them.
The plumbing system is described in detail with code examples. Some
design choices and ongoing discussions are explained. Finally, in
miscellanea you find nomenclature, coverage report, list of
contributors, changes and some todos. All non-experimental features are
fully test covered.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
rm -fR build
py.test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev0.git20140806
- Initial build for Sisyphus

