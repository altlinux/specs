%define oname zope.componentvocabulary
Name: python-module-%oname
Version: 1.0.1
Release: alt2.1
Summary: Component vocabularies
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.componentvocabulary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.component zope.i18nmessageid zope.interface
%py_requires zope.schema zope.security

%description
This package contains various vocabularies.

%package tests
Summary: Tests for zope.componentvocabulary
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component

%description tests
This package contains tests for zope.componentvocabulary.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

