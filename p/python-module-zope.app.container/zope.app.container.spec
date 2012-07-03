%define oname zope.app.container
Name: python-module-%oname
Version: 3.9.1
Release: alt2.1
Summary: Zope Container
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.container/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.browser zope.component zope.container
%py_requires zope.copypastemove zope.dublincore zope.event
%py_requires zope.exceptions zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.location zope.publisher
%py_requires zope.schema zope.security zope.size zope.traversing
%py_requires zope.app.publisher

%description
This package define interfaces of container components, and provides
sample container implementations such as a BTreeContainer and
OrderedContainer.

%package tests
Summary: Tests for Zope Container
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.securitypolicy

%description tests
This package define interfaces of container components, and provides
sample container implementations such as a BTreeContainer and
OrderedContainer.

This package contains tests for Zope Container.

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
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Initial build for Sisyphus

