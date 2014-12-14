%define mname collective
%define oname %mname.loremipsum
Name: python-module-%oname
Version: 0.11
Release: alt1.dev0.git20141211
Summary: Creates dummy content with populated Lorem Ipsum
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.loremipsum/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.loremipsum.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-loremipsum python-module-openid
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.UserAndGroupSelectionWidget
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.formwidget.recurrence
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname loremipsum Products.CMFPlone plone.dexterity
%py_requires plone.namedfile plone.api Products.CMFCore plone.z3cform
%py_requires Products.Archetypes Products.UserAndGroupSelectionWidget
%py_requires Products.ATContentTypes plone.app.textfield plone.uuid
%py_requires plone.formwidget.recurrence plone.autoform zope.interface
%py_requires plone.app.z3cform zope.component zope.schema zope.container
%py_requires zope.globalrequest zope.i18nmessageid zope.app.schema
%py_requires z3c.form

%description
collective.loremipsum is a developer tool to create dummy content and
dummy members inside your Plone site.

Plain text fields are populated with text from the loremipsum Python
library, while rich text is retrieved from loripsum.net.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
collective.loremipsum is a developer tool to create dummy content and
dummy members inside your Plone site.

Plain text fields are populated with text from the loremipsum Python
library, while rich text is retrieved from loripsum.net.

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

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Dec 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev0.git20141211
- Initial build for Sisyphus

