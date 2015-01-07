%define oname Products.PloneSurvey
Name: python-module-%oname
Version: 1.4.8
Release: alt1.dev.git20150106
Summary: Plone Survey is an addon collecting data from people
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneSurvey/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PloneSurvey.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Reportlab python-module-svg2rlg
BuildPreReq: python-module-PyPDF2
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-z3c.rml
BuildPreReq: python-module-collective.recaptcha
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.CMFFormController
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone z3c.rml reportlab collective.recaptcha
%py_requires Products.CMFCore Products.Archetypes Products.validation
%py_requires Products.ATContentTypes Products.PlonePAS zope.interface
%py_requires Products.PluggableAuthService zope.i18nmessageid zope.i18n
%py_requires zope.app.pagetemplate zope.browserpage zope.publisher
%py_requires Products.MailHost

%description
This package allows users to create a survey or simple form for
collecting user's feedback: on a course, simple data collection etc..
Surveys can be a simple single page, or a multi page survey with complex
branching.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.CMFFormController zope.event
%py_requires zope.lifecycleevent zope.component Products.CMFPlone.tests

%description tests
This package allows users to create a survey or simple form for
collecting user's feedback: on a course, simple data collection etc..
Surveys can be a simple single page, or a multi page survey with complex
branching.

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
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.8-alt1.dev.git20150106
- Initial build for Sisyphus

