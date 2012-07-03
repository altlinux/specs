%define oname repoze.dbbrowser
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Admin UI for relational db based apps
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.dbbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg repoze.tm2 sqlalchemy zope.sqlalchemy

%description
This package provides a simple WSGI application to browse and edit
database tables. The application was developed using the repoze.bfg web
framework and uses the excellent JqueryUI library.

After installing and configuring the application, you will be able to
browse and edit your application's tables by visiting the configured URL
path. All the configuration that is needed is an sqlalchemy database
connection string for your database.

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
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

