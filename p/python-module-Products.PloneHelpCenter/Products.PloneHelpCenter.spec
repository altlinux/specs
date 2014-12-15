%define oname Products.PloneHelpCenter
Name: python-module-%oname
Version: 4.0.1
Release: alt1.dev0.git20141016
Summary: A simple help-desk style documentation product for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneHelpCenter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PloneHelpCenter.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml python-module-Plone python-module-openid
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone-tests
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.AddRemoveWidget
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-plone.registry

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone plone.i18n Products.contentmigration Products.CMFCore
%py_requires Products.Archetypes Products.PythonScripts plone.memoize
%py_requires Products.ATContentTypes Products.CMFPlone plone.app.layout
%py_requires Products.LinguaPlone Products.AddRemoveWidget plone.folder
%py_requires Products.CMFDynamicViewFTI plone.app.controlpanel
%py_requires zope.component zope.interface zope.publisher

%description
Plone Help Center is an application designed to aid the documentation of
Plone, and is used on plone.org to categorize and keep documentation up
to date. It should be usable for documenting other open source products
(such as Plone Product add-ons) or even for other documentation
projects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.CMFPlone.tests

%description tests
Plone Help Center is an application designed to aid the documentation of
Plone, and is used on plone.org to categorize and keep documentation up
to date. It should be usable for documenting other open source products
(such as Plone Product add-ons) or even for other documentation
projects.

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
rm -fR build
py.test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20141016
- Initial build for Sisyphus

