%define oname mockup
Name: python-module-%oname
Version: 2.0.0
Release: alt1.git20150213
Summary: A collection of client side patterns for faster and easier web development
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mockup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/mockup.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-modules-json

%py_provides %oname

%description
Plone Mockup is an ongoing effort to modernize Plone's javascript
story.

The Goals of Mockup:

1. Standardize configuration of patterns implemented in js to use HTML
   data attributes, so they can be developed without running a backend
   server.
2. Use modern AMD approach to declaring dependencies on other js libs.
3. Full unit testing of js

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Plone Mockup is an ongoing effort to modernize Plone's javascript
story.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150213
- Initial build for Sisyphus

