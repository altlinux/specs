%define mname node.ext
%define oname %mname.zodb

%def_disable check

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20140513
Summary: Node Implementation with ZODB persistence
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/node.ext.zodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/node.ext.zodb.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-node python-module-ZODB3
BuildPreReq: python-module-interlude
BuildPreReq: python-module-zope.interface

%py_provides %oname
%py_requires %mname node ZODB3 zope.interface

%description
node.ext.zodb is a persistent node implementation for the ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
node.ext.zodb is a persistent node implementation for the ZODB.

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
%doc *.rst
%python_sitelibdir/node/ext/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/node/ext/*/tests.*

%files tests
%python_sitelibdir/node/ext/*/tests.*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140513
- Initial build for Sisyphus

