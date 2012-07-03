%define oname zc.freeze
Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: Pattern for freezing objects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.freeze/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc pytz rwproperty zc.copy ZODB3 zope.annotation
%py_requires zope.cachedescriptors zope.component zope.event
%py_requires zope.interface zope.locking

%description
The zc.freeze package provides a pattern for freezing objects. State is
informational--enforcement unspecified. Some enforcement approaches and
helpers are included.

%package tests
Summary: Tests for zc.freeze
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction zope.app.container zope.app.keyreference
%py_requires zope.app.testing zope.testing

%description tests
The zc.freeze package provides a pattern for freezing objects. State is
informational--enforcement unspecified. Some enforcement approaches and
helpers are included.

This package contains tests for zc.freeze.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

