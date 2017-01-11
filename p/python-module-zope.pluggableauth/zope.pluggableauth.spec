%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.pluggableauth

%def_with python3

Name: python-module-%oname
Version: 2.1.0
#Release: alt3.1
Summary: Pluggable Authentication Utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.pluggableauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/21/26/f1b506941ee29a2fd842e318bf4e56423bdd1c587dfdd64ed63f8bc40922/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope ZODB3 zope.authentication zope.component
%py_requires zope.container zope.event zope.i18nmessageid zope.interface
%py_requires zope.password zope.publisher zope.schema zope.security
%py_requires zope.session zope.site zope.traversing

%description
Based on zope.authentication, this package provides a flexible and
pluggable authentication utility. Several common plugins are provided.

%package -n python3-module-%oname
Summary: Pluggable Authentication Utility
Group: Development/Python3
%py3_requires zope ZODB3 zope.authentication zope.component
%py3_requires zope.container zope.event zope.i18nmessageid zope.interface
%py3_requires zope.password zope.publisher zope.schema zope.security
%py3_requires zope.session zope.site zope.traversing

%description -n python3-module-%oname
Based on zope.authentication, this package provides a flexible and
pluggable authentication utility. Several common plugins are provided.

%package -n python3-module-%oname-tests
Summary: Tests for Pluggable Authentication Utility
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component

%description -n python3-module-%oname-tests
Based on zope.authentication, this package provides a flexible and
pluggable authentication utility. Several common plugins are provided.

This package contains tests for Pluggable Authentication Utility.

%package tests
Summary: Tests for Pluggable Authentication Utility
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component

%description tests
Based on zope.authentication, this package provides a flexible and
pluggable authentication utility. Several common plugins are provided.

This package contains tests for Pluggable Authentication Utility.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Version 2.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

