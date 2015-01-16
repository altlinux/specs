%define mname collective
%define oname %mname.ckeditortemplates
Name: python-module-%oname
Version: 0.3.1
Release: alt1.dev0.git20150115
Summary: Plone templates for ckeditor
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.ckeditortemplates/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/IMIO/collective.ckeditortemplates.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-BeautifulSoup4
BuildPreReq: python-module-mock python-module-openid
BuildPreReq: python-module-five.grok-tests
BuildPreReq: python-module-Plone python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-collective.ckeditor
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-robotframework-debuglibrary
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.multilingualbehavior

%py_provides %oname
%py_requires %mname Plone plone.app.dexterity plone.app.contenttypes
%py_requires plone.api collective.ckeditor Products.CMFCore
%py_requires Products.CMFPlone plone.app.dexterity plone.app.textfield
%py_requires plone.namedfile plone.dexterity plone.supermodel
%py_requires zope.i18nmessageid plone.multilingualbehavior

%description
This products create plone templates for ckeditor.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework.testing plone.testing
%py_requires plone.app.testing zope.publisher zope.configuration
%py_requires five.grok.testing

%description tests
This products create plone templates for ckeditor.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/tests

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/tests

%changelog
* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.dev0.git20150115
- Version 0.3.1.dev0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.dev0.git20141105
- Initial build for Sisyphus

