%define oname zope.principalregistry

%def_with python3

Name: python-module-%oname
Version: 4.0.0
Release: alt3.1
Summary: Global principal registry component for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.principalregistry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.authentication zope.component zope.interface
%py_requires zope.password zope.security

%description
This package provides an authentication utility for zope.authentication
that uses simple non-persistent principal registry.

%package -n python3-module-%oname
Summary: Global principal registry component for Zope3
Group: Development/Python3
%py3_requires zope zope.authentication zope.component zope.interface
%py3_requires zope.password zope.security

%description -n python3-module-%oname
This package provides an authentication utility for zope.authentication
that uses simple non-persistent principal registry.

%package -n python3-module-%oname-tests
Summary: Tests for zope.principalregistry
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component

%description -n python3-module-%oname-tests
This package provides an authentication utility for zope.authentication
that uses simple non-persistent principal registry.

This package contains tests for zope.principalregistry

%package tests
Summary: Tests for zope.principalregistry
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component

%description tests
This package provides an authentication utility for zope.authentication
that uses simple non-persistent principal registry.

This package contains tests for zope.principalregistry

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Initial build for Sisyphus

