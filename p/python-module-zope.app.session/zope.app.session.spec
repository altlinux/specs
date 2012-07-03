%define oname zope.app.session
Name: python-module-%oname
Version: 3.6.2
Release: alt2.1
Summary: Zope session
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app ZODB3 zope.annotation zope.app.appsetup
%py_requires zope.app.http zope.component zope.i18nmessageid
%py_requires zope.interface zope.location zope.minmax zope.publisher
%py_requires zope.session

%description
This package provides session support.

%package tests
Summary: Tests for Zope session
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.site zope.app.testing zope.app.zptpage
%py_requires zope.app.securitypolicy zope.app.zcmlfiles

%description tests
This package provides session support.

This package contains tests for Zope session.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

