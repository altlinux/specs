%define oname zc.sourcefactory

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2.a1.1
Summary: An easy way to create custom Zope 3 sources
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.sourcefactory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc ZODB3 zope.intid zope.browser zope.component
%py_requires zope.dublincore zope.interface zope.proxy zope.publisher
%py_requires zope.schema

%description
Source factories are used to simplify the creation of sources for
certain standard cases.

Sources split up the process of providing input fields with choices for
users into several components: a context binder, a source class, a terms
class, and a term class.

This is the correct abstraction and will fit many complex cases very
well. To reduce the amount of work to do for some standard cases, the
source factories allow users to define only the business relevant code
for getting a list of values, getting a token and a title to display.

%package -n python3-module-%oname
Summary: An easy way to create custom Zope 3 sources
Group: Development/Python3
%py3_requires zc ZODB3 zope.intid zope.browser zope.component
%py3_requires zope.dublincore zope.interface zope.proxy zope.publisher
%py3_requires zope.schema

%description -n python3-module-%oname
Source factories are used to simplify the creation of sources for
certain standard cases.

Sources split up the process of providing input fields with choices for
users into several components: a context binder, a source class, a terms
class, and a term class.

This is the correct abstraction and will fit many complex cases very
well. To reduce the amount of work to do for some standard cases, the
source factories allow users to define only the business relevant code
for getting a list of values, getting a token and a title to display.

%package -n python3-module-%oname-tests
Summary: Tests for zc.sourcefactory
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.app.testing zope.keyreference
%py3_requires zope.app.zcmlfiles

%description -n python3-module-%oname-tests
Source factories are used to simplify the creation of sources for
certain standard cases.

Sources split up the process of providing input fields with choices for
users into several components: a context binder, a source class, a terms
class, and a term class.

This is the correct abstraction and will fit many complex cases very
well. To reduce the amount of work to do for some standard cases, the
source factories allow users to define only the business relevant code
for getting a list of values, getting a token and a title to display.

This package contains tests for zc.sourcefactory.

%package tests
Summary: Tests for zc.sourcefactory
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing zope.keyreference
%py_requires zope.app.zcmlfiles

%description tests
Source factories are used to simplify the creation of sources for
certain standard cases.

Sources split up the process of providing input fields with choices for
users into several components: a context binder, a source class, a terms
class, and a term class.

This is the correct abstraction and will fit many complex cases very
well. To reduce the amount of work to do for some standard cases, the
source factories allow users to define only the business relevant code
for getting a list of values, getting a token and a title to display.

This package contains tests for zc.sourcefactory.

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

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.a1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.a1
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.a1
- Version 1.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

