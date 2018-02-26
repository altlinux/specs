%define oname zope.app.server
Name: python-module-%oname
Version: 3.6.0
Release: alt2.1
Summary: ZServer integration for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.server/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.app.applicationcontrol zope.app.appsetup
%py_requires zope.app.publication zope.app.wsgi zope.configuration
%py_requires zope.deprecation zope.event zope.interface zope.publisher
%py_requires zope.server zope.password zope.processlifetime zdaemon
%py_requires ZConfig ZODB3

%description
This package integrates ZServer -- Zope's HTTP and FTP server -- into a
Zope 3 application setup. It also defines the script skeleton for a
classic Zope 3 application.

%package tests
Summary: Tests for zope.app.server
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package integrates ZServer -- Zope's HTTP and FTP server -- into a
Zope 3 application setup. It also defines the script skeleton for a
classic Zope 3 application.

This package contains tests for zope.app.server.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

