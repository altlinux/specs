%define oname zope.app.rotterdam

%def_with python3

Name: python-module-%oname
Version: 3.5.3
Release: alt2.1
Summary: Rotterdam -- A Zope 3 ZMI Skin
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.rotterdam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.app.basicskin zope.app.form
%py_requires zope.app.pagetemplate zope.component zope.container
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.proxy
%py_requires zope.publisher zope.security zope.traversing

%description
This package provides an advanced skin for the Zope 3 ZMI.

%package -n python3-module-%oname
Summary: Rotterdam -- A Zope 3 ZMI Skin
Group: Development/Python3
%py3_requires zope.app zope.app.basicskin zope.app.form
%py3_requires zope.app.pagetemplate zope.component zope.container
%py3_requires zope.i18n zope.i18nmessageid zope.interface zope.proxy
%py3_requires zope.publisher zope.security zope.traversing

%description -n python3-module-%oname
This package provides an advanced skin for the Zope 3 ZMI.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.rotterdam
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.login
%py3_requires zope.securitypolicy

%description -n python3-module-%oname-tests
This package provides an advanced skin for the Zope 3 ZMI.

This package contains tests for zope.app.rotterdam.

%package tests
Summary: Tests for zope.app.rotterdam
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.securitypolicy

%description tests
This package provides an advanced skin for the Zope 3 ZMI.

This package contains tests for zope.app.rotterdam.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
sed -i 's|rfc822|rfc822py3|' $(find ./ -name '*.py')
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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Version 3.5.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

