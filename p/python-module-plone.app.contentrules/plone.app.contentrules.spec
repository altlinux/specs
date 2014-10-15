%define oname plone.app.contentrules

%def_disable check

Name: python-module-%oname
Version: 3.0.8
Release: alt1.dev0.git20141009
Summary: Plone integration for plone.contentrules
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.contentrules/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.contentrules.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.stringinterp
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app five.formlib plone.contentrules plone.memoize
%py_requires plone.stringinterp plone.uuid plone.app.form zope.browser
%py_requires plone.app.vocabularies zope.annotation zope.component
%py_requires zope.container zope.event zope.formlib zope.i18nmessageid
%py_requires zope.interface zope.lifecycleevent zope.publisher zope.site
%py_requires zope.schema zope.traversing Products.CMFCore ZODB3
%py_requires Products.CMFDefault Products.GenericSetup
%py_requires Products.statusmessages
#py_requires Products.CMFPlone

%description
plone.app.contentrules provides Plone-specific conditions and actions,
as well as a user interface for plone.contentrules.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.contentrules provides Plone-specific conditions and actions,
as well as a user interface for plone.contentrules.

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
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.dev0.git20141009
- Initial build for Sisyphus

