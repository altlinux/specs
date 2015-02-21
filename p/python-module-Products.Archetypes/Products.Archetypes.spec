%define oname Products.Archetypes

Name: python-module-%oname
Version: 1.10.4
Release: alt1.dev0.git20150126
Summary: Default Content Type Framework for Plone 2.1-4.x
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Archetypes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.Archetypes.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mock python-modules-json
BuildPreReq: python-module-Products.CMFFormController
BuildPreReq: python-module-Products.CMFQuickInstallerTool
BuildPreReq: python-module-Products.DCWorkflow
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-Products.PlacelessTranslationService
BuildPreReq: python-module-Products.PortalTransforms
BuildPReReq: python-module-Products.ZSQLMethods
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-plone.folder python-module-plone.uuid
BuildPreReq: python-module-plone.app.folder
BuildPreReq: python-module-zope.annotation python-module-zope.publisher
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFTestCase
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.widgets
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.globalrequest

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component zope.contenttype zope.datetime zope.schema
%py_requires zope.deferredimport zope.event zope.i18n zope.i18nmessageid
%py_requires zope.interface zope.lifecycleevent zope.publisher zope.site
%py_requires zope.tal zope.viewlet Products.CMFCore Products.CMFDefault
%py_requires Products.CMFFormController Products.CMFQuickInstallerTool
%py_requires Products.DCWorkflow Products.GenericSetup plone.folder
%py_requires Products.MimetypesRegistry Products.PortalTransforms json
%py_requires Products.PlacelessTranslationService Products.ZSQLMethods
%py_requires Products.statusmessages Products.validation plone.uuid
%py_requires plone.app.folder ZODB3 zope.annotation zope.publisher
%py_requires Products.CMFPlone plone.app.widgets plone.registry
%add_python_req_skip apelib

%description
Archetypes is a developers framework for rapidly developing and
deploying rich, full featured content types within the context of
Zope/CMF and Plone.

Archetypes is based around the idea of an Active Schema. Rather than
provide a simple description of a new data type, Archetype schemas do
the actual work and heavy lifting involved in using the new type.
Archetype Schemas serve as easy extension points for other developers as
project specific components can be created and bound or you can choose
among the rich existing set of features.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.CMFTestCase mock plone.app.testing
%py_requires zope.configuration zope.globalrequest

%description tests
Archetypes is a developers framework for rapidly developing and
deploying rich, full featured content types within the context of
Zope/CMF and Plone.

Archetypes is based around the idea of an Active Schema. Rather than
provide a simple description of a new data type, Archetype schemas do
the actual work and heavy lifting involved in using the new type.
Archetype Schemas serve as easy extension points for other developers as
project specific components can be created and bound or you can choose
among the rich existing set of features.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/Products/*/*/*/*/tests
%exclude %python_sitelibdir/Products/*/examples

%files tests
%python_sitelibdir/Products/*/tests
%python_sitelibdir/Products/*/*/*/*/tests
%python_sitelibdir/Products/*/examples

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.4-alt1.dev0.git20150126
- Version 1.10.4.dev0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.3-alt1.dev0.git20141023
- Version 1.10.3.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt2.dev0.git20140817
- Added necessary requirements
- Enabled testing

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.dev0.git20140817
- Initial build for Sisyphus

