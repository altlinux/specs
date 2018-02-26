%define oname zope.fanstatic
Name: python-module-%oname
Version: 0.12
Release: alt1
Summary: Fanstatic integration for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.fanstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
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

