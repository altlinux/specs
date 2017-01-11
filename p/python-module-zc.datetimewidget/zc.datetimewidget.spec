%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zc.datetimewidget

%def_with python3

Name: python-module-%oname
Version: 0.8.0
#Release: alt2.1
Summary: Javascript-based widgets for date and datetime fields
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.datetimewidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/a1/32/05acfd667c7670ded21287f4ad327d93c704d2d27b765e178c7c7e7794c0/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc pytz zc.i18n zc.resourcelibrary zope.app.form
%py_requires zope.component zope.datetime zope.interface zope.publisher
%py_requires zope.schema

%description
There are two types of widgets provided by this package, a date widget
and a datetime widget.

%package -n python3-module-%oname
Summary: Javascript-based widgets for date and datetime fields
Group: Development/Python3
%py3_requires zc pytz zc.i18n zc.resourcelibrary zope.app.form
%py3_requires zope.component zope.datetime zope.interface zope.publisher
%py3_requires zope.schema

%description -n python3-module-%oname
There are two types of widgets provided by this package, a date widget
and a datetime widget.

%package -n python3-module-%oname-tests
Summary: Tests for zc.datetimewidget
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.zcmlfiles zope.app.securitypolicy
%py3_requires zope.app.authentication zope.app.server zope.app.testing
%py3_requires zope.securitypolicy zope.testbrowser zope.testing

%description -n python3-module-%oname-tests
There are two types of widgets provided by this package, a date widget
and a datetime widget.

This package contains tests for zc.datetimewidget.

%package tests
Summary: Tests for zc.datetimewidget
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.zcmlfiles zope.app.securitypolicy
%py_requires zope.app.authentication zope.app.server zope.app.testing
%py_requires zope.securitypolicy zope.testbrowser zope.testing

%description tests
There are two types of widgets provided by this package, a date widget
and a datetime widget.

This package contains tests for zc.datetimewidget.

%prep
%setup -q -n %{oname}-%{version}

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
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

