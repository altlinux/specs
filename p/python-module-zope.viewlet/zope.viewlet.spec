%define oname zope.viewlet
Name: python-module-%oname
Version: 3.7.2
Release: alt2.1
Summary: Zope Viewlets
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.viewlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.browserpage zope.component zope.configuration
%py_requires zope.contentprovider zope.event zope.i18nmessageid
%py_requires zope.interface zope.location zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
Viewlets provide a generic framework for building pluggable user
interfaces.

%package tests
Summary: Tests for Zope Viewlets
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.size

%description tests
Viewlets provide a generic framework for building pluggable user
interfaces.

This package contains tests for Zope Viewlets.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

