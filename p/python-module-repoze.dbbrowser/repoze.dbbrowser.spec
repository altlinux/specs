%define oname repoze.dbbrowser

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt3
Summary: Admin UI for relational db based apps
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.dbbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.bfg repoze.tm2 sqlalchemy zope.sqlalchemy

%description
This package provides a simple WSGI application to browse and edit
database tables. The application was developed using the repoze.bfg web
framework and uses the excellent JqueryUI library.

After installing and configuring the application, you will be able to
browse and edit your application's tables by visiting the configured URL
path. All the configuration that is needed is an sqlalchemy database
connection string for your database.

%package -n python3-module-%oname
Summary: Admin UI for relational db based apps
Group: Development/Python3
%py3_requires repoze.bfg repoze.tm2 sqlalchemy zope.sqlalchemy

%description -n python3-module-%oname
This package provides a simple WSGI application to browse and edit
database tables. The application was developed using the repoze.bfg web
framework and uses the excellent JqueryUI library.

After installing and configuring the application, you will be able to
browse and edit your application's tables by visiting the configured URL
path. All the configuration that is needed is an sqlalchemy database
connection string for your database.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.dbbrowser
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a simple WSGI application to browse and edit
database tables. The application was developed using the repoze.bfg web
framework and uses the excellent JqueryUI library.

This package contains tests for repoze.dbbrowser.

%package tests
Summary: Tests for repoze.dbbrowser
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a simple WSGI application to browse and edit
database tables. The application was developed using the repoze.bfg web
framework and uses the excellent JqueryUI library.

This package contains tests for repoze.dbbrowser.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

