%define oname plone.openid
Name: python-module-%oname
Version: 2.0.4
Release: alt1.dev0.git20150211
Summary: OpenID authentication support for PAS
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.openid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.openid.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils
BuildPreReq: python-module-openid
BuildPreReq: python-module-transaction
BuildPreReq: python-module-Products.PluggableAuthService

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone ZODB3 Products.PluggableAuthService openid
%py_requires transaction docutils

%description
This product implements OpenID authentication support for Zope via a
Pluggable Authentication Service plugin.

Using this package everyone with an OpenID authentity will be able to
login on your Zope site. OpenID accounts are not given any extra roles
beyond the standard Authenticated role. This allows you to make a
distinction between people that have explicitly signed up to your site
and people who are unknown but have succesfully verified their identity.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This product implements OpenID authentication support for Zope via a
Pluggable Authentication Service plugin.

Using this package everyone with an OpenID authentity will be able to
login on your Zope site. OpenID accounts are not given any extra roles
beyond the standard Authenticated role. This allows you to make a
distinction between people that have explicitly signed up to your site
and people who are unknown but have succesfully verified their identity.

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

%files
%doc *.txt docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.dev0.git20150211
- Version 2.0.4.dev0

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt2.dev0.git20140826
- Fixed requirements

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.dev0.git20140826
- Initial build for Sisyphus

