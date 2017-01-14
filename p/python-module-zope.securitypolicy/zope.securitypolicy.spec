%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.securitypolicy

%def_with python3

Name: python-module-%oname
Version: 4.1.0
#Release: alt3.1
Summary: Default security policy for Zope3
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.securitypolicy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/90/e9/8d950f1b265835104e925671f4b57a236218f7e7fc507049043edb875449/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-zope.i18nmessageid
%py_requires ZODB3 zope.annotation zope.authentication zope.component
%py_requires zope.configuration zope.interface zope.location
%py_requires zope.schema zope.security zope.dublincore

%description
This package provides an useful security policy for Zope3. It's the
default security policy used in "zope3 the application" and many other
zope-based projects.

%package -n python3-module-%oname
Summary: Default security policy for Zope3
Group: Development/Python3
Requires: python3-module-zope.i18nmessageid
%py3_requires ZODB3 zope.annotation zope.authentication zope.component
%py3_requires zope.configuration zope.interface zope.location
%py3_requires zope.schema zope.security zope.dublincore

%description -n python3-module-%oname
This package provides an useful security policy for Zope3. It's the
default security policy used in "zope3 the application" and many other
zope-based projects.

%package -n python3-module-%oname-tests
Summary: Tests for Default security policy for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testrunner

%description -n python3-module-%oname-tests
This package provides an useful security policy for Zope3. It's the
default security policy used in "zope3 the application" and many other
zope-based projects.

This package contains tests for Default security policy for Zope3.

%package tests
Summary: Tests for Default security policy for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testrunner

%description tests
This package provides an useful security policy for Zope3. It's the
default security policy used in "zope3 the application" and many other
zope-based projects.

This package contains tests for Default security policy for Zope3.

%prep
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3
- Version 4.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

