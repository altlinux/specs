%define oname z3c.testing

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt2.a3.1
Summary: High-level Testing Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.app.appsetup zope.app.publication
%py_requires zope.app.testing zope.container zope.site zope.component
%py_requires zope.configuration zope.interface zope.testing
%py_requires zope.app.rotterdam zope.browserpage zope.browserresource
%py_requires zope.principalregistry zope.publisher zope.securitypolicy
%py_requires zope.testbrowser

%description
This package provides a collection of high-level test setups for unit
and functional testing. In particular, it provides a testing layer that
can use an existing, pre-populated database as a starting point, which
speeds up the test setup phase for large testing data sets.

%package -n python3-module-%oname
Summary: High-level Testing Support
Group: Development/Python3
%py3_requires ZODB3 zope.app.appsetup zope.app.publication
%py3_requires zope.app.testing zope.container zope.site zope.component
%py3_requires zope.configuration zope.interface zope.testing
%py3_requires zope.app.rotterdam zope.browserpage zope.browserresource
%py3_requires zope.principalregistry zope.publisher zope.securitypolicy
%py3_requires zope.testbrowser

%description -n python3-module-%oname
This package provides a collection of high-level test setups for unit
and functional testing. In particular, it provides a testing layer that
can use an existing, pre-populated database as a starting point, which
speeds up the test setup phase for large testing data sets.

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
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.a3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.a3
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.a3
- Version 1.0.0a3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

