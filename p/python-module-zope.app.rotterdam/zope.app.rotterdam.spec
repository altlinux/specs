%define oname zope.app.rotterdam
Name: python-module-%oname
Version: 3.5.2
Release: alt2.1
Summary: Rotterdam -- A Zope 3 ZMI Skin
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.rotterdam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.app.basicskin zope.app.form
%py_requires zope.app.pagetemplate zope.component zope.container
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.proxy
%py_requires zope.publisher zope.security zope.traversing

%description
This package provides an advanced skin for the Zope 3 ZMI.

%package tests
Summary: Tests for zope.app.rotterdam
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.securitypolicy

%description tests
This package provides an advanced skin for the Zope 3 ZMI.

This package contains tests for zope.app.rotterdam.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

