%define oname zope.introspector

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt3
Summary: Introspection helpers for Zope and Python objects
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.introspector/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope grokcore.component zope.interface zope.component
%py_requires zope.publisher martian

%description
Introspection helpers for Zope and Python objects.

%package -n python3-module-%oname
Summary: Introspection helpers for Zope and Python objects
Group: Development/Python3
%py3_requires zope grokcore.component zope.interface zope.component
%py3_requires zope.publisher martian

%description -n python3-module-%oname
Introspection helpers for Zope and Python objects.

%package -n python3-module-%oname-tests
Summary: Tests for zope.introspector
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing z3c.testsetup
%py3_requires zope.securitypolicy

%description -n python3-module-%oname-tests
Introspection helpers for Zope and Python objects.

This package contains tests for zope.introspector.

%package tests
Summary: Tests for zope.introspector
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing z3c.testsetup
%py_requires zope.securitypolicy

%description tests
Introspection helpers for Zope and Python objects.

This package contains tests for zope.introspector.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

