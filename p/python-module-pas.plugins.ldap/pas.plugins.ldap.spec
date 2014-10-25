%define mname pas.plugins
%define oname %mname.ldap
Name: python-module-%oname
Version: 1.4.1
Release: alt1.dev0.git20141024
Summary: LDAP Plugin for Zope2 PluggableAuthService (users and groups)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pas.plugins.ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/pas.plugins.ldap.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-bda.cache
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-node
BuildPreReq: python-module-node.ext.ldap-tests
BuildPreReq: python-module-odict
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-ldap
BuildPreReq: python-module-yafowil
BuildPreReq: python-module-yafowil.plone
BuildPreReq: python-module-yafowil.widget.array
BuildPreReq: python-module-yafowil.widget.dict
BuildPreReq: python-module-yafowil.yaml
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Plone
BuildPreReq: python-module-interlude
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-yaml
BuildPreReq: python-module-node.ext.ugm
BuildPreReq: python-module-argparse
BuildPreReq: python-module-openid
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname bda.cache five.globalrequest node.ext.ldap Plone
%py_requires plone.registry Products.CMFCore Products.GenericSetup
%py_requires Products.CMFQuickInstallerTool Products.PlonePAS
%py_requires Products.PluggableAuthService Products.statusmessages
%py_requires yafowil.plone yafowil.widget.array yafowil.widget.dict
%py_requires yafowil.yaml zope.component zope.globalrequest
%py_requires zope.i18nmessageid zope.interface zope.traversing

%description
This is a LDAP Plugin for the Zope2 Pluggable Authentication Service
(PAS).

It provides users and/or groups from an LDAP Directory. It works in a
plain Zope2 even if it depends on PlonePAS. If Plone is installed an
integration layer with a setup-profile and a plone-controlpanel page is
available.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing zope.configuration node.ext.ldap.testing

%description tests
This is a LDAP Plugin for the Zope2 Pluggable Authentication Service
(PAS).

It provides users and/or groups from an LDAP Directory. It works in a
plain Zope2 even if it depends on PlonePAS. If Plone is installed an
integration layer with a setup-profile and a plone-controlpanel page is
available.

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
nosetests

%files
%doc *.rst
%python_sitelibdir/pas/plugins/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/pas/plugins/*/test*

%files tests
%python_sitelibdir/pas/plugins/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.dev0.git20141024
- Initial build for Sisyphus

