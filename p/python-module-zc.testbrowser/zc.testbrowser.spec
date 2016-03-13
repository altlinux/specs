%define oname zc.testbrowser

%def_with python3

Name: python-module-%oname
Version: 1.0.0a5
Release: alt3.1
Summary: Programmable web browser for functional black-box testing of web applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.testbrowser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc ClientForm mechanize simplejson zope.interface
%py_requires zope.schema

%description
The zc.testbrowser package provides web user agents (browsers) with
programmatic interfaces designed to be used for testing web
applications, especially in conjunction with doctests.

There are currently two type of testbrowser provided.  One for accessing
web sites via HTTP (zc.testbrowser.browser) and one that controls a
Firefox web browser (zc.testbrowser.real).  All flavors of testbrowser
have the same API.

%package -n python3-module-%oname
Summary: Programmable web browser for functional black-box testing of web applications
Group: Development/Python3
%py3_requires zc ClientForm mechanize simplejson zope.interface
%py3_requires zope.schema

%description -n python3-module-%oname
The zc.testbrowser package provides web user agents (browsers) with
programmatic interfaces designed to be used for testing web
applications, especially in conjunction with doctests.

There are currently two type of testbrowser provided.  One for accessing
web sites via HTTP (zc.testbrowser.browser) and one that controls a
Firefox web browser (zc.testbrowser.real).  All flavors of testbrowser
have the same API.

%package -n python3-module-%oname-tests
Summary: Tests for zc.testbrowser
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The zc.testbrowser package provides web user agents (browsers) with
programmatic interfaces designed to be used for testing web
applications, especially in conjunction with doctests.

There are currently two type of testbrowser provided.  One for accessing
web sites via HTTP (zc.testbrowser.browser) and one that controls a
Firefox web browser (zc.testbrowser.real).  All flavors of testbrowser
have the same API.

This package contains tests for zc.testbrowser.

%package tests
Summary: Tests for zc.testbrowser
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The zc.testbrowser package provides web user agents (browsers) with
programmatic interfaces designed to be used for testing web
applications, especially in conjunction with doctests.

There are currently two type of testbrowser provided.  One for accessing
web sites via HTTP (zc.testbrowser.browser) and one that controls a
Firefox web browser (zc.testbrowser.real).  All flavors of testbrowser
have the same API.

This package contains tests for zc.testbrowser.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0a5-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0a5-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0a5-alt1
- Initial build for Sisyphus

