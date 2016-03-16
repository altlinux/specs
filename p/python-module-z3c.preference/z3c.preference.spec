%define oname z3c.preference

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt2.1
Summary: UI for zope.preference using z3c.pagelet and z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.preference/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.form z3c.formui z3c.pagelet zope.preference

%description
This packages provides a user interface for zope.preference using
z3c.pagelet and z3c.form.

%package -n python3-module-%oname
Summary: UI for zope.preference using z3c.pagelet and z3c.form
Group: Development/Python3
%py3_requires z3c.form z3c.formui z3c.pagelet zope.preference

%description -n python3-module-%oname
This packages provides a user interface for zope.preference using
z3c.pagelet and z3c.form.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.preference
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.wsgi zope.browserresource zope.login
%py3_requires zope.principalregistry zope.app.principalannotation
%py3_requires zope.securitypolicy zope.testbrowser zope.testing

%description -n python3-module-%oname-tests
This packages provides a user interface for zope.preference using
z3c.pagelet and z3c.form.

This package contains tests for z3c.preference.

%package tests
Summary: Tests for z3c.preference
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.wsgi zope.browserresource zope.login
%py_requires zope.principalregistry zope.app.principalannotation
%py_requires zope.securitypolicy zope.testbrowser zope.testing

%description tests
This packages provides a user interface for zope.preference using
z3c.pagelet and z3c.form.

This package contains tests for z3c.preference.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

