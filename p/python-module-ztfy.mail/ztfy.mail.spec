%define mname ztfy
%define oname %mname.mail
Name: python-module-%oname
Version: 0.1.6
Release: alt1
Summary: ZTFY interfaces and utilities for mail handling
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.mail/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-chardet
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.componentvocabulary
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname ztfy.utils chardet zope.componentvocabulary
%py_requires zope.i18nmessageid zope.interface zope.schema zope.sendmail

%description
ztfy.mail is a small package which provides a few interfaces and
utilities to help handling email messages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
ztfy.mail is a small package which provides a few interfaces and
utilities to help handling email messages.

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
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus

