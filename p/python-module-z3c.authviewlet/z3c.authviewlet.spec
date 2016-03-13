%define oname z3c.authviewlet

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt3.1
Summary: Authentication viewlet for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.authviewlet
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.layer.pagelet zope.authentication zope.component
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.viewlet

%description
This package provides an authentication viewlet implementation for
Zope3.

%package -n python3-module-%oname
Summary: Authentication viewlet for Zope3
Group: Development/Python3
%py3_requires z3c.layer.pagelet zope.authentication zope.component
%py3_requires zope.i18n zope.i18nmessageid zope.interface zope.viewlet

%description -n python3-module-%oname
This package provides an authentication viewlet implementation for
Zope3.

%package -n python3-module-%oname-tests
Summary: Tests for Authentication viewlet for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.layer.pagelet zope.app.authentication zope.app.testing
%py3_requires zope.testbrowser zope.testing

%description -n python3-module-%oname-tests
This package provides an authentication viewlet implementation for
Zope3.

This package contains tests for Authentication viewlet for Zope3.

%package tests
Summary: Tests for Authentication viewlet for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.layer.pagelet zope.app.authentication zope.app.testing
%py_requires zope.testbrowser zope.testing

%description tests
This package provides an authentication viewlet implementation for
Zope3.

This package contains tests for Authentication viewlet for Zope3.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus

