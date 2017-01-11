%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname z3c.etestbrowser

%def_with python3

Name: python-module-%oname
Version: 2.0.1
#Release: alt2.1
Summary: Extensions for zope.testbrowser
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.etestbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/2c/42/5ead3d40c40f45b9b9d31f661a7ffdd194d5e981ad8d586cfede4947bd52/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires lxml zope.testbrowser zope.app.wsgi

%description
This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to
more external products, like lxml.

%package -n python3-module-%oname
Summary: Extensions for zope.testbrowser
Group: Development/Python3
%py3_requires lxml zope.testbrowser zope.app.wsgi

%description -n python3-module-%oname
This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to
more external products, like lxml.

%package -n python3-module-%oname-tests
Summary: Tests for Extensions for zope.testbrowser
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles
%py3_requires zope.app.securitypolicy zope.app.server zope.testbrowser

%description -n python3-module-%oname-tests
This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to
more external products, like lxml.

This package contains tests for Extensions for zope.testbrowser.

%package tests
Summary: Tests for Extensions for zope.testbrowser
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles
%py_requires zope.app.securitypolicy zope.app.server zope.testbrowser

%description tests
This package is intended to provide extended versions of the Zope 3
testbrowser. Especially those extensions that introduce dependencies to
more external products, like lxml.

This package contains tests for Extensions for zope.testbrowser.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|htmllib|html.parser|g' $(find ./ -name '*.py')
%python3_build
popd
%endif

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Added necessary requirements
- Excludes *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

