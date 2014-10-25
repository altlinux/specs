%define mname node.ext
%define oname %mname.ugm
Name: python-module-%oname
Version: 0.9.6
Release: alt1.git20140910
Summary: Node-based user and group management
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/node.ext.ugm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/node.ext.ugm.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-node-tests
BuildPreReq: python-module-plumber python-module-interlude
BuildPreReq: python-module-unittest2 python-module-zope.testing
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
node.ext.ugm provides an API for node based managing of users and
groups.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
node.ext.ugm provides an API for node based managing of users and
groups.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires node

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/node/ext/__init__.py \
	%buildroot%python_sitelibdir/node/ext/

%check
python setup.py test
nosetests

%files
%doc *.rst
%python_sitelibdir/node/ext/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/node/ext/*/tests.*
%exclude %python_sitelibdir/node/ext/__init__.py*

%files tests
%python_sitelibdir/node/ext/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/node/ext
%python_sitelibdir/node/ext/__init__.py*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1.git20140910
- Initial build for Sisyphus

