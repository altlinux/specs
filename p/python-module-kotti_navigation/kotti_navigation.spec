%define oname kotti_navigation
Name: python-module-%oname
Version: 0.3.1
Release: alt1
Summary: Add a configurable navigation to your Kotti site
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_navigation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-pyramid-tests python-module-fanstatic
BuildPreReq: python-modules-logging

%py_provides %oname
%py_requires kotti pyramid fanstatic logging

%description
This is an extension to the Kotti CMS that renders a navigation in one
of the available slots for a Kotti website (left, right, abovecontent,
etc.).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.config.testing kotti.tests

%description tests
This is an extension to the Kotti CMS that renders a navigation in one
of the available slots for a Kotti website (left, right, abovecontent,
etc.).

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

