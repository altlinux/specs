%define mname unimr
%define oname %mname.memcachedlock
Name: python-module-%oname
Version: 0.1
Release: alt1.rc2.r144828
Summary: Memcached based locking factory functions to provide shared locking
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/unimr.memcachedlock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-ZODB
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-lovely.memcached python-module-pytz
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.size
BuildPreReq: python-module-zope.filerepresentation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-zope.browser

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires lovely.memcached collective.monkeypatcher ZODB

%description
unimr.memcachedlock implements a distributed "soft" locking mechanism
using memcached. It provides factory functions and decorators for a
primitive locking, a reentrant locking and a special locking for
zeo-clients.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.testing Testing

%description tests
unimr.memcachedlock implements a distributed "soft" locking mechanism
using memcached. It provides factory functions and decorators for a
primitive locking, a reentrant locking and a special locking for
zeo-clients.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test
py.test %mname/memcachedlock/tests.py

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.rc2.r144828
- Initial build for Sisyphus

