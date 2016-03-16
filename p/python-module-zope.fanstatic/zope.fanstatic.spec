%define oname zope.fanstatic

%def_with python3

Name: python-module-%oname
Version: 0.12
Release: alt2.1
Summary: Fanstatic integration for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.fanstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope fanstatic zope.component zope.errorview zope.event
%py_requires zope.interface zope.publisher zope.traversing

%description
This package provides Zope integration for fanstatic. This means it's
taking care of three things:

* provide access to the needed resources throughout the request/response
  cycle.
* provide the base URL for the resources to be rendered.
* clear the needed resources when an exception view is rendered.

This library fulfills these conditions for a Zope Toolkit/Grok setup.

%package -n python3-module-%oname
Summary: Fanstatic integration for Zope
Group: Development/Python3
%py3_requires zope fanstatic zope.component zope.errorview zope.event
%py3_requires zope.interface zope.publisher zope.traversing

%description -n python3-module-%oname
This package provides Zope integration for fanstatic. This means it's
taking care of three things:

* provide access to the needed resources throughout the request/response
  cycle.
* provide the base URL for the resources to be rendered.
* clear the needed resources when an exception view is rendered.

This library fulfills these conditions for a Zope Toolkit/Grok setup.

%package -n python3-module-%oname-tests
Summary: Tests for Fanstatic integration for Zope
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.annotation zope.app.publication zope.app.wsgi
%py3_requires zope.browserpage zope.container zope.principalregistry
%py3_requires zope.securitypolicy zope.security zope.site
%py3_requires zope.app.appsetup

%description -n python3-module-%oname-tests
This package provides Zope integration for fanstatic. This means it's
taking care of three things:

* provide access to the needed resources throughout the request/response
  cycle.
* provide the base URL for the resources to be rendered.
* clear the needed resources when an exception view is rendered.

This library fulfills these conditions for a Zope Toolkit/Grok setup.

This package contains tests for Fanstatic integration for Zope.

%package tests
Summary: Tests for Fanstatic integration for Zope
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.app.publication zope.app.wsgi
%py_requires zope.browserpage zope.container zope.principalregistry
%py_requires zope.securitypolicy zope.security zope.site
%py_requires zope.app.appsetup

%description tests
This package provides Zope integration for fanstatic. This means it's
taking care of three things:

* provide access to the needed resources throughout the request/response
  cycle.
* provide the base URL for the resources to be rendered.
* clear the needed resources when an exception view is rendered.

This library fulfills these conditions for a Zope Toolkit/Grok setup.

This package contains tests for Fanstatic integration for Zope.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Version 0.12

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2
- Enabled tests

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Initial build for Sisyphus

