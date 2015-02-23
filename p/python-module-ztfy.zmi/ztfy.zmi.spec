%define mname ztfy
%define oname %mname.zmi
Name: python-module-%oname
Version: 0.3.1
Release: alt1
Summary: ZTFY management interface for Zope3/BlueBream
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.zmi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-z3c.language.switch
BuildPreReq: python-module-zope.app.basicskin
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname z3c.language.switch zope.app.basicskin zope.i18n
%py_requires zope.authentication zope.browsermenu zope.browserpage
%py_requires zope.component zope.dublincore zope.i18nmessageid ztfy.skin
%py_requires zope.interface zope.publisher zope.schema zope.security
%py_requires zope.traversing

%description
ztfy.zmi is a small package which just provides a new skin called ZMI.
This skin is done to include standard ZMI views with ZTFY.blog
management skin.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.zmi is a small package which just provides a new skin called ZMI.
This skin is done to include standard ZMI views with ZTFY.blog
management skin.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

