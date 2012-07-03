%define oname zope.app.boston
Name: python-module-%oname
Version: 3.5.1
Release: alt2.1
Summary: Boston -- A Zope 3 ZMI Skin
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.boston/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.basicskin zope.app.skins zope.app.testing
%py_requires zope.browsermenu zope.component zope.container
%py_requires zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.viewlet

%description
The Boston skin is a new UI for the Zope Management Interface called
ZMI.

%package tests
Summary: Tests for zope.app.boston
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.dtmlpage zope.app.onlinehelp
%py_requires zope.app.securitypolicy zope.app.zcmlfiles zope.testbrowser
%py_requires zope.testing zope.login

%description tests
The Boston skin is a new UI for the Zope Management Interface called
ZMI.

This package contains tests for zope.app.boston.

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
%exclude %python_sitelibdir/*/*/*/*test*
%exclude %python_sitelibdir/*/*/*/*/*test*

%files tests
%python_sitelibdir/*/*/*/*test*
%python_sitelibdir/*/*/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

