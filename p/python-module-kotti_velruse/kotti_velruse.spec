%define oname kotti_velruse
Name: python-module-%oname
Version: 0.3.4
Release: alt1.git20131126
Summary: Kotti authentication with Velruse: OpenID, OAuth2, Google, Yahoo, Live, Facebook, Twitter...
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_velruse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git.alt:/gears/p/python-module-kotti_velruse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-openid-selector
BuildPreReq: python-module-rgomes_velruse python-module-kotti-tests
BuildPreReq: python-module-openid python-module-anykeystore
BuildPreReq: python-module-requests-oauthlib python-module-pyramid_zcml
BuildPreReq: python-module-zope.sqlalchemy python-module-pyramid_tm
BuildPreReq: python-module-pyramid_debugtoolbar python-module-lingua
BuildPreReq: python-module-pyramid_chameleon python-module-kotti_tinymce
BuildPreReq: python-module-pyramid_mako python-module-polib

%py_provides %oname
Requires: python-module-rgomes_velruse
%py_requires openid_selector pyramid

%description
kotti_velruse is a Kotti plugin which provides authentication via
Velruse, using methods such as: OpenID, OAuth2, Google, Yahoo, Live,
Facebook, Twitter and others.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
kotti_velruse is a Kotti plugin which provides authentication via
Velruse, using methods such as: OpenID, OAuth2, Google, Yahoo, Live,
Facebook, Twitter and others.

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
%doc AUTHORS CHANGES README docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20131126
- Initial build for Sisyphus

