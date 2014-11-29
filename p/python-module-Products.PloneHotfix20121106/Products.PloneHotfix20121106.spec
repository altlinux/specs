%define oname Products.PloneHotfix20121106
Name: python-module-%oname
Version: 1.2
Release: alt1
Summary: Various Plone hotfixes, 2012-11-06
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneHotfix20121106/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-wicked
BuildPreReq: python-module-Pillow python-module-Plone
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-archetypes.kss
BuildPreReq: python-module-borg.localrole
BuildPreReq: python-module-kss.core
BuildPreReq: python-module-kss.demo
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.customerize
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.i18n
BuildPreReq: python-module-plone.app.iterate
BuildPreReq: python-module-plone.app.kss
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.linkintegrity
BuildPreReq: python-module-plone.app.openid
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.redirector
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.fieldsets
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.intelligenttext
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.openid
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.session
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.portlet.collection
BuildPreReq: python-module-plone.portlet.static
BuildPreReq: python-module-five.customerize
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-Products.kupu

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone Products.PloneTestCase archetypes.kss borg.localrole
%py_requires kss.core kss.demo plone.app.content plone.app.contentmenu
%py_requires plone.app.contentrules plone.app.controlpanel plone.app.kss
%py_requires plone.app.customerize plone.app.form plone.app.i18n
%py_requires plone.app.iterate plone.app.layout plone.app.linkintegrity
%py_requires plone.app.openid plone.app.portlets plone.app.redirector
%py_requires plone.app.viewletmanager plone.app.vocabularies plone.i18n
%py_requires plone.app.workflow plone.browserlayer plone.contentrules
%py_requires plone.fieldsets plone.intelligenttext plone.keyring
%py_requires plone.locking plone.memoize plone.openid plone.portlets
%py_requires plone.protect plone.session plone.theme five.customerize
%py_requires plone.portlet.collection plone.portlet.static
%py_requires five.localsitemanager Products.kupu

%description
This hotfix fixes multiple vulnerabilities in Plone, including arbitrary
code execution and privilege escalation.

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
%doc docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

