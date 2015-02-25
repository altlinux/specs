%define mname hl.pas
%define oname %mname.samlplugin

%def_disable check

Name: python-module-%oname
Version: 1.3
Release: alt1.dev.git20150224
Summary: SAML2 authentication for Zope
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/hl.pas.samlplugin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Haufe-Lexware/hl.pas.samlplugin.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-requests python-module-m2crypto
BuildPreReq: python-module-mehcode-xmlsec
BuildPreReq: python-modules-json python-modules-logging
BuildPreReq: python-modules-xml
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.GenericSetup-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.app.container Products.PluggableAuthService requests
%py_requires M2Crypto Products.CMFCore zope.site zope.component json
%py_requires zope.interface zope.publisher logging xml xmlsec

%description
hl.pas.samlplugin provides a SAML2 plugin for Zope's
PluggableAuthService. It provides the IExtractionPlugin,
IAuthenticationPlugin, IChallengePlugin, ICredentialsResetPlugin
interfaces.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.GenericSetup.testing

%description tests
hl.pas.samlplugin provides a SAML2 plugin for Zope's
PluggableAuthService. It provides the IExtractionPlugin,
IAuthenticationPlugin, IChallengePlugin, ICredentialsResetPlugin
interfaces.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-hl = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-hl
Summary: Core files of hl
Group: Development/Python
%py_provides hl

%description -n python-module-hl
Core files of hl.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 hl/pas/__init__.py \
	%buildroot%python_sitelibdir/hl/pas/
install -p -m644 hl/__init__.py \
	%buildroot%python_sitelibdir/hl/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/hl/pas/samlplugin
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/hl/pas/samlplugin/tests

%files tests
%python_sitelibdir/hl/pas/samlplugin/tests

%files -n python-module-%mname
%dir %python_sitelibdir/hl/pas
%python_sitelibdir/hl/pas/__init__.py*

%files -n python-module-hl
%dir %python_sitelibdir/hl
%python_sitelibdir/hl/__init__.py*

%changelog
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev.git20150224
- Initial build for Sisyphus

