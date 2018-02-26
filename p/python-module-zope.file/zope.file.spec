%define oname zope.file
Name: python-module-%oname
Version: 0.6.0
Release: alt2.1
Summary: Efficient File Implementation for Zope Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3 zope.browser zope.container zope.contenttype
%py_requires zope.event zope.interface zope.publisher zope.security
%py_requires zope.mimetype

%description
The zope.file package provides a content object used to store a file.
The interface supports efficient upload and download.

%package tests
Summary: Tests for zope.file
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.server zope.app.testing zope.app.zcmlfiles
%py_requires zope.login zope.password zope.securitypolicy
%py_requires zope.testbrowser

%description tests
The zope.file package provides a content object used to store a file.
The interface supports efficient upload and download.

This package contains tests for zope.file.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

