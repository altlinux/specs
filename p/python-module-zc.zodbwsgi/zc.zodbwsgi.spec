%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zc.zodbwsgi

%def_with python3

Name: python-module-%oname
Version: 1.2.0
#Release: alt1.1
Summary: WSGI Middleware for Managing ZODB Database Conections
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.zodbwsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/8b/1d/c4d29143e557dc51efc39660ed21708603c73d122c303ea18d9e9fba1a62/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc repoze.retry ZConfig ZODB3 zope.exceptions

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

%package -n python3-module-%oname
Summary: WSGI Middleware for Managing ZODB Database Conections
Group: Development/Python3
%py3_requires zc repoze.retry ZConfig ZODB3 zope.exceptions

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for zc.zodbwsgi
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing webtest paste.deploy manuel

%description -n python3-module-%oname-tests
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
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

