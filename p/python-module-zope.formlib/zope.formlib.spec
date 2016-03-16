%define oname zope.formlib

%def_with python3

Name: python-module-%oname
Version: 4.3.0
Release: alt3.1
Summary: Form generation and validation library for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.formlib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope pytz zope.browser zope.browserpage zope.component
%py_requires zope.event zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.publisher zope.schema
%py_requires zope.security zope.traversing zope.datetime

%description
Forms are web components that use widgets to display and input data.
Typically a template displays the widgets by accessing an attribute or
method on an underlying class.

%package -n python3-module-%oname
Summary: Form generation and validation library for Zope
Group: Development/Python3
%py3_requires zope pytz zope.browser zope.browserpage zope.component
%py3_requires zope.event zope.i18n zope.i18nmessageid zope.interface
%py3_requires zope.lifecycleevent zope.publisher zope.schema
%py3_requires zope.security zope.traversing zope.datetime

%description -n python3-module-%oname
Forms are web components that use widgets to display and input data.
Typically a template displays the widgets by accessing an attribute or
method on an underlying class.

%package -n python3-module-%oname-tests
Summary: Tests for zope.formlib
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.configuration zope.testing

%description -n python3-module-%oname-tests
Forms are web components that use widgets to display and input data.
Typically a template displays the widgets by accessing an attribute or
method on an underlying class.

This package contains sests for zope.formlib.

%package tests
Summary: Tests for zope.formlib
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration zope.testing

%description tests
Forms are web components that use widgets to display and input data.
Typically a template displays the widgets by accessing an attribute or
method on an underlying class.

This package contains sests for zope.formlib.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3
- Version 4.3.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2.a2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.a2
- Version 4.3.0a2

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.a1
- Version 4.3.0a1

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1
- Version 4.0.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.5-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.5-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.5-alt1
- Initial build for Sisyphus

