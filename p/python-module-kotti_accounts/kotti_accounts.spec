%define oname kotti_accounts

Name: python-module-%oname
Version: 0.2.5
Release: alt1.git20140820
Summary: Allows a user principal to be associated to multiple email accounts
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_accounts
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/frgomes/kotti_accounts.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-kotti_velruse python-module-zope.sqlalchemy
BuildPreReq: python-module-waitress python-module-pyramid_zcml
BuildPreReq: python-module-pyramid_tm python-module-pyramid_debugtoolbar
BuildPreReq: python-module-pyramid_chameleon python-module-lingua
BuildPreReq: python-module-kotti_tinymce python-module-pyramid_mako
BuildPreReq: python-module-polib

%py_provides %oname

%description
kotti_accounts is a Kotti plugin which allows a user principal to be
associated to multiple email accounts.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
kotti_accounts is a Kotti plugin which allows a user principal to be
associated to multiple email accounts.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20140820
- Initial build for Sisyphus

