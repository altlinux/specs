%define oname Products.plonehrm
Name: python-module-%oname
Version: 2.15
Release: alt1.dev.svn20100115
Summary: Plone HRM is a simple Open Source personnel solution for SMEs
License: GPLv2+
Group: Development/Python
Url: https://plone.org/products/plonehrm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.plonehrm/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plonehrm.absence
BuildPreReq: python-module-plonehrm.checklist
BuildPreReq: python-module-plonehrm.contracts
BuildPreReq: python-module-plonehrm.jobperformance
BuildPreReq: python-module-plonehrm.notes
BuildPreReq: python-module-plonehrm.notifications
BuildPreReq: python-module-plonehrm.personaldata
BuildPreReq: python-module-collective.autopermission
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plonehrm.absence plonehrm.checklist plonehrm.contracts
%py_requires plonehrm.jobperformance plonehrm.notes Products.CMFPlone
%py_requires plonehrm.notifications plonehrm.personaldata plone.memoize
%py_requires collective.autopermission Products.CMFCore zope.interface
%py_requires Products.Archetypes Products.ATContentTypes plone.portlets
%py_requires Products.validation Products.CMFDefault plone.app.portlets
%py_requires Products.CMFQuickInstallerTool plone.app.contentmenu
%py_requires plone.app.controlpanel plone.app.workflow zope.i18n
%py_requires zope.formlib zope.component zope.viewlet zope.event
%py_requires zope.annotation zope.schema zope.i18nmessageid
%py_requires zope.app.container

%description
This product helps maintain personnel files for your organisation, even
across multiple locations. The main features include: Unlimited number
of branches and employees, register statutory personal data of your
staff, a checklist for new staff, e.g. collecting copies of personal
documents, manage contracts and merge templates to create new contracts,
a variety of web and e-mail notifications, including birthdays,
probation and contract expiry and reports on progress discussions and
agendas.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
This product helps maintain personnel files for your organisation, even
across multiple locations. The main features include: Unlimited number
of branches and employees, register statutory personal data of your
staff, a checklist for new staff, e.g. collecting copies of personal
documents, manage contracts and merge templates to create new contracts,
a variety of web and e-mail notifications, including birthdays,
probation and contract expiry and reports on progress discussions and
agendas.

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

pushd Products/plonehrm
cp -fR *.txt *.zcml *.gif i18n locales profiles skins \
	%buildroot%python_sitelibdir/Products/plonehrm/
install -p -m644 doc/*.txt \
	%buildroot%python_sitelibdir/Products/plonehrm/doc/
popd

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.15-alt1.dev.svn20100115
- Initial build for Sisyphus

