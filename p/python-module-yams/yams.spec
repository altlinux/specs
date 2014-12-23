%define oname yams
Name: python-module-%oname
Version: 0.40.2
Release: alt1
Summary: Entity / relation schema
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/yams/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-logilab-common
BuildPreReq: python-module-logilab-database python-module-six

%py_provides %oname

%description
Yet Another Magic Schema ! A simple/generic but powerful entities /
relations schema, suitable to represent RDF like data. The schema is
readable/writable from/to various formats.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Yet Another Magic Schema ! A simple/generic but powerful entities /
relations schema, suitable to represent RDF like data. The schema is
readable/writable from/to various formats.

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
%doc ChangeLog README
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.2-alt1
- Version 0.40.2

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.0-alt1
- Version 0.40.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.39.1-alt1
- Initial build for Sisyphus

