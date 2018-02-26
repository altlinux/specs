%define oname zope.app.appsetup
Name: python-module-%oname
Version: 3.16.0
Release: alt3.1
Summary: Zope app setup helper
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.appsetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.publication zope.component zope.configuration
%py_requires zope.container zope.error zope.event zope.interface
%py_requires zope.processlifetime zope.security zope.session zope.site
%py_requires zope.traversing ZODB3

%description
This package provides application setup helpers for the Zope3 appserver.

%package tests
Summary: Tests for Zope app setup helper
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.componentvocabulary zope.principalregistry
%py_requires zope.testing zope.testrunner

%description tests
This package provides application setup helpers for the Zope3 appserver.

This package contains tests for Zope app setup helper.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.16.0-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt3
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt2
- Excluded .pth file

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16.0-alt1
- Initial build for Sisyphus

