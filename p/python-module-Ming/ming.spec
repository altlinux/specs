%define oname Ming
Name: python-module-%oname
Version: 0.3.2
Release: alt1.dev.20121219
Summary: Bringing order to Mongo since 2009
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Ming/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

%package tests
Summary: Tests for Bringing order to Mongo since 2009
Group: Development/Python
Requires: %name = %version-%release

%description tests
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

This package contains tests for Ming.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev.20121219
- Version 0.3.2dev-20121219

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev.20120912
- Initial build for Sisyphus

