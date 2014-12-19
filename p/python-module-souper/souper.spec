%define oname souper
Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20140306
Summary: Souper - Generic Indexed Storage based on ZODB
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/souper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/souper.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-interlude
BuildPreReq: python-module-node.ext.zodb
BuildPreReq: python-module-repoze.catalog
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface

%py_provides %oname
%py_requires node.ext.zodb repoze.catalog zope.component zope.interface

%description
Souper is a tool for programmers. It offers an integrated storage tied
together with indexes in a catalog. The records in the storage are
generic. It is possible to store any data on a record if it is
persistent pickable in ZODB.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Souper is a tool for programmers. It offers an integrated storage tied
together with indexes in a catalog. The records in the storage are
generic. It is possible to store any data on a record if it is
persistent pickable in ZODB.

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
%doc *.rst docs/*
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%oname/tests.*

%files tests
%python_sitelibdir/%oname/tests.*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140306
- Initial build for Sisyphus

