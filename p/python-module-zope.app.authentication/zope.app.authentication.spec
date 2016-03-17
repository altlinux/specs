%define oname zope.app.authentication

%def_with python3

Name: python-module-%oname
Version: 3.9
Release: alt3.1
Summary: Principals and groups management for the pluggable authentication utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.authentication/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app ZODB3 zope.authentication zope.component
%py_requires zope.container zope.dublincore zope.event zope.exceptions
%py_requires zope.formlib zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.location zope.password zope.pluggableauth zope.schema
%py_requires zope.security zope.traversing zope.app.container
%py_requires zope.app.component

%description
This package provides a flexible and pluggable authentication utility
for Zope 3, using zope.pluggableauth. Several common plugins are provided.

%package -n python3-module-%oname
Summary: Principals and groups management for the pluggable authentication utility
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.authentication zope.component
%py3_requires zope.container zope.dublincore zope.event zope.exceptions
%py3_requires zope.formlib zope.i18n zope.i18nmessageid zope.interface
%py3_requires zope.location zope.password zope.pluggableauth zope.schema
%py3_requires zope.security zope.traversing zope.app.container
%py3_requires zope.app.component

%description -n python3-module-%oname
This package provides a flexible and pluggable authentication utility
for Zope 3, using zope.pluggableauth. Several common plugins are provided.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.authentication
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.securitypolicy zope.app.zcmlfiles
%py3_requires zope.securitypolicy zope.testbrowser zope.publisher
%py3_requires zope.testing zope.session zope.formlib zope.publisher
%py3_requires zope.site zope.login

%description -n python3-module-%oname-tests
This package provides a flexible and pluggable authentication utility
for Zope 3, using zope.pluggableauth. Several common plugins are provided.

This package contains tests for zope.app.authentication.

%package tests
Summary: Tests for zope.app.authentication
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.securitypolicy zope.app.zcmlfiles
%py_requires zope.securitypolicy zope.testbrowser zope.publisher
%py_requires zope.testing zope.session zope.formlib zope.publisher
%py_requires zope.site zope.login

%description tests
This package provides a flexible and pluggable authentication utility
for Zope 3, using zope.pluggableauth. Several common plugins are provided.

This package contains tests for zope.app.authentication.

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
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/tests

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9-alt1
- Initial build for Sisyphus

