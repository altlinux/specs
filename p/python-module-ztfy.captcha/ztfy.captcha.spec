%define mname ztfy
%define oname %mname.captcha
Name: python-module-%oname
Version: 0.3.3
Release: alt1
Summary: ZTFY captcha package
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.captcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Pillow python-module-fanstatic
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.template
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.dublincore
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-ztfy.cache
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-ztfy.baseskin
BuildPreReq: python-module-ztfy.myams
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname PIL z3c.form z3c.template zope.annotation ztfy.cache
%py_requires zope.component zope.dublincore zope.i18nmessageid ztfy.skin
%py_requires zope.interface zope.schema ztfy.jqueryui ztfy.utils
%py_requires ztfy.baseskin ztfy.myams fanstatic

%description
ztfy.captcha is a small package used to generate "human" verification
images called 'captchas', which can easily be integrated into public
forms to avoid spam.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.captcha is a small package used to generate "human" verification
images called 'captchas', which can easily be integrated into public
forms to avoid spam.

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
* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

