%define oname zc.zodbwsgi
Name: python-module-%oname
Version: 0.1.0
Release: alt1.1
Summary: WSGI Middleware for Managing ZODB Database Conections
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zodbwsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc repoze.retry ZConfig ZODB3

%description
The zc.zodbwsgi provides middleware for managing connections to a ZODB
database. It combines several features into a single middleware
component:

* database configuration
* database initialization
* connection management
* optional transaction management
* optional request retry on conflict errors (using repoze.retry)

It is designed to work with paste deployment and provides a
"filter_app_factory" entry point, named "main".

%package tests
Summary: Tests for zc.zodbwsgi
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing webtest paste.deploy manuel

%description tests
The zc.zodbwsgi provides middleware for managing connections to a ZODB
database. It combines several features into a single middleware
component:

* database configuration
* database initialization
* connection management
* optional transaction management
* optional request retry on conflict errors (using repoze.retry)

It is designed to work with paste deployment and provides a
"filter_app_factory" entry point, named "main".

This package contains tests for zc.zodbwsgi.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

