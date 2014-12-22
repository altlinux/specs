%define mname dm.zope
%define oname %mname.saml2
Name: python-module-%oname
Version: 3.1
Release: alt1.b2
Summary: Zope 2/Plone extension for SAML2 based Single Sign On
License: GPL/ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.zope.saml2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dm.saml2
BuildPreReq: python-module-dm.zope.schema
BuildPreReq: python-module-dm.xmlsec.binding
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname dm.saml2 dm.zope.schema dm.xmlsec.binding zope.event
%py_requires Products.CMFCore Products.statusmessages Products.PlonePAS
%py_requires Products.PluggableAuthService zope.schema zope.formlib
%py_requires zope.interface zope.app.component zope.component
%py_requires zope.app.container zope.lifecycleevent zope.i18nmessageid

%description
This package supports SAML2 based SSO (Single Sign-On) for Zope2/Plone
installations.

While it currently supports only a small subset of the SAML2 standard
(simple identity provider, simple service provider integration and
attribute support), its current functionality is comparable to Plone's
OpenId support.

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
%doc PKG-INFO
%python_sitelibdir/dm/zope/*
%python_sitelibdir/*.egg-info

%changelog
* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1.b2
- Initial build for Sisyphus

