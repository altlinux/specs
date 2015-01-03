%define oname BlazeUtils
Name: python-module-%oname
Version: 0.4.4
Release: alt1
Summary: A collection of python utility functions and classes
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/BlazeUtils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-wrapt
BuildPreReq: python-module-mock python-module-nose
BuildPreReq: python-module-xlwt python-module-xlrd
BuildPreReq: python-module-docutils python-module-SQLAlchemy

%py_provides blazeutils
%py_requires xlwt wrapt xlrd docutils sqlalchemy

%description
BlazeUtils is a library to hold common tools for the Blaze library
family:

* BlazeWeb
* BaseBWA
* BlazeForm

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
BlazeUtils is a library to hold common tools for the Blaze library
family:

* BlazeWeb
* BaseBWA
* BlazeForm

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
nosetests

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing.*

%files tests
%python_sitelibdir/*/testing.*

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus

