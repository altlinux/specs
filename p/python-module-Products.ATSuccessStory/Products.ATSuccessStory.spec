%define oname Products.ATSuccessStory
Name: python-module-%oname
Version: 4.1.2
Release: alt1.git20120907
Summary: Success stories Product
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ATSuccessStory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.ATSuccessStory.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.CMFPlone Products.Archetypes
%py_requires Products.CMFDynamicViewFTI Products.ATContentTypes
%py_requires zope.formlib zope.schema zope.component zope.interface
%py_requires zope.app.component zope.i18nmessageid plone.memoize
%py_requires plone.app.vocabularies plone.i18n plone.app.portlets
%py_requires plone.portlets

%description
ATSuccessStory is a very simple product that provides you with two new
content types:

a. Success Story Folder
b. Success Story

Success Stories can only be created inside Success Story Folders, so you
first need one of those.

By default the folder will display success stories with a nice summary
view, showing the description and the image.

This product also provides a portlet, that you can add anywhere.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.component.testing
%py_requires zope.security.testing

%description tests
ATSuccessStory is a very simple product that provides you with two new
content types:

a. Success Story Folder
b. Success Story

Success Stories can only be created inside Success Story Folders, so you
first need one of those.

By default the folder will display success stories with a nice summary
view, showing the description and the image.

This product also provides a portlet, that you can add anywhere.

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

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.git20120907
- Initial build for Sisyphus

