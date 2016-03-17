%define oname zc.ajaxform

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt4.1
Summary: Ajax Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.ajaxform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires ClientForm rwproperty simplejson zc.form
%py_requires zope.html zope.testbrowser

%description
The zc.ajaxform package provides framework to support:

- A single-class application model

- Nested-application support

- Integration with zope.formlib

%package -n python3-module-%oname
Summary: Ajax Support
Group: Development/Python3
%py3_requires ClientForm rwproperty simplejson zc.form
%py3_requires zope.html zope.testbrowser

%description -n python3-module-%oname
The zc.ajaxform package provides framework to support:

- A single-class application model

- Nested-application support

- Integration with zope.formlib

%package -n python3-module-%oname-tests
Summary: Tests for zc.ajaxform
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.zcmlfiles zope.testbrowser

%description -n python3-module-%oname-tests
The zc.ajaxform package provides framework to support:

- A single-class application model

- Nested-application support

- Integration with zope.formlib

This package contains tests for zc.ajaxform.

%package tests
Summary: Tests for zc.ajaxform
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
The zc.ajaxform package provides framework to support:

- A single-class application model

- Nested-application support

- Integration with zope.formlib

This package contains tests for zc.ajaxform.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3
- Removed setuptools from requirements

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

