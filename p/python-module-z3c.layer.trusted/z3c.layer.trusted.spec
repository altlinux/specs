%define oname z3c.layer.trusted

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt3.1
Summary: Trusted layer setup for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.layer.trusted/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.publisher zope.app.publication zope.container
%py_requires z3c.layer.minimal

%description
This package provides a trused layer setup for Zope3. Truted means you
can travers over objects which you don't have permission for. This is
needed if you have a setup with more then one IAuthentication utility.
Otherwise you don't hav a chance to traverse to the IAthentication
utility in the subsite without to authenticate at the parent
IAuthentication.

%package -n python3-module-%oname
Summary: Trusted layer setup for Zope3
Group: Development/Python3
%py3_requires zope.publisher zope.app.publication zope.container
%py3_requires z3c.layer.minimal

%description -n python3-module-%oname
This package provides a trused layer setup for Zope3. Truted means you
can travers over objects which you don't have permission for. This is
needed if you have a setup with more then one IAuthentication utility.
Otherwise you don't hav a chance to traverse to the IAthentication
utility in the subsite without to authenticate at the parent
IAuthentication.

%package -n python3-module-%oname-tests
Summary: Tests for Trusted layer setup for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testbrowser zope.app.testing zope.app.zcmlfiles
%py3_requires z3c.layer.minimal

%description -n python3-module-%oname-tests
This package provides a trused layer setup for Zope3. Truted means you
can travers over objects which you don't have permission for. This is
needed if you have a setup with more then one IAuthentication utility.
Otherwise you don't hav a chance to traverse to the IAthentication
utility in the subsite without to authenticate at the parent
IAuthentication.

This package contains tests for Trusted layer setup for Zope3.

%package tests
Summary: Tests for Trusted layer setup for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testbrowser zope.app.testing zope.app.zcmlfiles
%py_requires z3c.layer.minimal

%description tests
This package provides a trused layer setup for Zope3. Truted means you
can travers over objects which you don't have permission for. This is
needed if you have a setup with more then one IAuthentication utility.
Otherwise you don't hav a chance to traverse to the IAthentication
utility in the subsite without to authenticate at the parent
IAuthentication.

This package contains tests for Trusted layer setup for Zope3.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

