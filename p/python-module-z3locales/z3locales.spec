%define oname z3locales
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Display localized dates in Zope 2 using Zope 3 components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3locales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires zope.i18n DateTime

%description
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

%package tests
Summary: Tests for z3locales
Group: Development/Python
Requires: %name = %version-%release

%description tests
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

This package contains tests for z3locales.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

