%define oname zope.app.interface
Name: python-module-%oname
Version: 3.6.0
Release: alt2.1
Summary: Zope Interface Extensions
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.interface/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zodbcode zope.app.content zope.componentvocabulary
%py_requires zope.security

%description
This package provides several extensions to Zope interfaces, such as a
persistent implementation, interface type queries, and a vocabulary of
all registered interfaces of the system (or of a particular type).

%package tests
Summary: Tests for Zope Interface Extensions
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides several extensions to Zope interfaces, such as a
persistent implementation, interface type queries, and a vocabulary of
all registered interfaces of the system (or of a particular type).

This package contains tests for Zope Interface Extensions.

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

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

