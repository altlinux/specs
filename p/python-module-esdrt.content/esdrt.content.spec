%define mname esdrt
%define oname %mname.content
Name: python-module-%oname
Version: 1.27
Release: alt1.dev0.git20150112
Summary: Content-types for ESD Review Tool
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/esdrt.content/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/esdrt.content.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-openid python-module-argparse
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-collective.z3cform.datagridfield
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-plone.app.versioningbehavior
BuildPreReq: python-module-plone.app.workflowmanager
BuildPreReq: python-module-cs.htmlmailer
BuildPreReq: python-module-collective.deletepermission
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDiffTool
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.directives.dexterity
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.container zope.i18nmessageid z3c.form
%py_requires zope.browsermenu zope.app.container zope.event
%py_requires zope.publisher zope.globalrequest zope.lifecycleevent
%py_requires zope.schema zope.interface zope.annotation zope.viewlet
%py_requires plone.i18n plone.app.content plone.registry zope.component
%py_requires plone.dexterity plone.indexer plone.app.textfield zope.i18n
%py_requires plone.directives.dexterity plone.app.contentlisting
%py_requires plone.app.discussion plone.z3cform plone.directives.form
%py_requires Products.CMFPlone Products.CMFEditions plone.rfc822
%py_requires Products.statusmessages Products.CMFDiffTool plone.memoize
%py_requires five.grok plone.app.dexterity plone.namedfile plone.api
%py_requires collective.z3cform.datagridfield plone.app.workflowmanager
%py_requires Products.ATVocabularyManager plone.app.versioningbehavior
%py_requires cs.htmlmailer collective.deletepermission Products.CMFCore

%description
Product containing content-types and workflow information for Effort
Sharing Decission Review Tool.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Product containing content-types and workflow information for Effort
Sharing Decission Review Tool.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.27-alt1.dev0.git20150112
- New snapshot

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.27-alt1.dev0.git20141223
- New snapshot

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.27-alt1.dev0.git20141222
- Initial build for Sisyphus

