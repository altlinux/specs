%define oname proteus
Name: python-module-%oname
Version: 3.4.0
Release: alt1
Summary: Library to access Tryton server as a client
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/proteus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-dateutil
BuildPreReq: python-module-trytond-tests python-module-simplejson
BuildPreReq: python-module-cdecimal python-modules-sqlite3
BuildPreReq: python-module-pydot graphviz python-module-pygraphviz

%py_provides %oname

%description
A library to access Tryton's models like a client.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library to access Tryton's models like a client.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=$PWD
python setup.py test

%files
%doc CHANGELOG README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

