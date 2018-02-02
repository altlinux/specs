%define oname Flask-WebTest
Name: python-module-%oname
Version: 0.0.7
Release: alt1.git20141009.1
Summary: Utilities for testing Flask applications with WebTest
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-WebTest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aromanovich/flask-webtest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-flask
BuildPreReq: python-module-flask_sqlalchemy python-module-webtest
BuildPreReq: python-module-blinker python-modules-sqlite3

%py_provides flask_webtest

%description
Provides a set of utilities to ease testing Flask applications with
WebTest.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.7-alt1.git20141009.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141009
- Initial build for Sisyphus

