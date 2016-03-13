%define oname z3locales

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt2.1
Summary: Display localized dates in Zope 2 using Zope 3 components
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3locales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.i18n DateTime

%description
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

%package -n python3-module-%oname
Summary: Display localized dates in Zope 2 using Zope 3 components
Group: Development/Python3
%py3_requires zope.i18n DateTime

%description -n python3-module-%oname
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

%package -n python3-module-%oname-tests
Summary: Tests for z3locales
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Z3locales is a library which translates dates in Zope 2 to the current
user language using Zope 3 technology.

This package contains tests for z3locales.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
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

