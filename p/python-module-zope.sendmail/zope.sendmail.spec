%define oname zope.sendmail
Name: python-module-%oname
Version: 3.7.4
Release: alt2.1
Summary: Zope sendmail
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.sendmail/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope transaction zope.i18nmessageid zope.interface
%py_requires zope.schema zope.component zope.configuration

%description
zope.sendmail is a package for email sending from Zope 3 applications.

%package tests
Summary: Tests for Zope sendmail
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.security zope.component

%description tests
zope.sendmail is a package for email sending from Zope 3 applications.

This package contains tests for Zope sendmail.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.4-alt1
- Initial build for Sisyphus

