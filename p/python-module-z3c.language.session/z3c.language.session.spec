%define oname z3c.language.session

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt4.1
Summary: Zope3 i18n language session
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.language.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app.generations zope.component zope.interface
%py_requires zope.publisher zope.session
Requires: python-module-z3c.language = %EVR

%description
This package provides a session which can be used to store a language.
See z3c.language.negotiator for a sample usage.

%package -n python3-module-%oname
Summary: Zope3 i18n language session
Group: Development/Python3
%py3_requires zope.app.generations zope.component zope.interface
%py3_requires zope.publisher zope.session
Requires: python3-module-z3c.language = %EVR

%description -n python3-module-%oname
This package provides a session which can be used to store a language.
See z3c.language.negotiator for a sample usage.

%package -n python3-module-%oname-tests
Summary: Tests for Zope3 i18n language session
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing z3c.coverage

%description -n python3-module-%oname-tests
This package provides a session which can be used to store a language.
See z3c.language.negotiator for a sample usage.

This package contains tests for Zope3 i18n language session.

%package tests
Summary: Tests for Zope3 i18n language session
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
This package provides a session which can be used to store a language.
See z3c.language.negotiator for a sample usage.

This package contains tests for Zope3 i18n language session.

%package -n python-module-z3c.language
Summary: Core package of z3c.language
Group: Development/Python

%description -n python-module-z3c.language
This package contains core package of z3c.language.

%package -n python3-module-z3c.language
Summary: Core package of z3c.language
Group: Development/Python3

%description -n python3-module-z3c.language
This package contains core package of z3c.language.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif
touch %buildroot%python_sitelibdir/z3c/language/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/z3c/language/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/z3c/language/__init__.py*

%files tests
%python_sitelibdir/*/*/*/tests.*

%files -n python-module-z3c.language
%python_sitelibdir/z3c/language/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/z3c/language/__init__.py
%exclude %python3_sitelibdir/z3c/language/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-z3c.language
%python3_sitelibdir/z3c/language/__init__.py
%python3_sitelibdir/z3c/language/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt4
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3
- Added python-module-z3c.language

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

