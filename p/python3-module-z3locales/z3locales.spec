%define oname z3locales

Name: python3-module-%oname
Version: 0.4.1
Release: alt3

Summary: Display localized dates in Zope 2 using Zope 3 components
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/z3locales/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires zope.i18n DateTime


%description
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

%package tests
Summary: Tests for z3locales
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

This package contains tests for z3locales.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

