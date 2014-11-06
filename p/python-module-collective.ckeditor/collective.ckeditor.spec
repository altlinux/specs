%define mname collective
%define oname %mname.ckeditor
Name: python-module-%oname
Version: 4.3.0
Release: alt1.b3.dev0.git20140619
Summary: CKEditor for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.ckeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.ckeditor.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-demjson
BuildPreReq: python-module-zope.i18nmessageid python-module-Zope2-tests
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-collective.plonefinder
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.ResourceRegistries
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-plone.outputfilters
BuildPreReq: python-module-plone.fieldsets
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.i18nmessageid collective.quickupload
%py_requires collective.plonefinder plone.app.uuid Products.CMFCore
%py_requires Products.CMFPlone Products.PortalTransforms zope.schema
%py_requires Products.ATContentTypes Products.Archetypes plone.fieldsets
%py_requires Products.PythonScripts Products.ResourceRegistries
%py_requires Products.CMFDefault plone.outputfilters zope.app.component
%py_requires plone.app.controlpanel zope.component zope.interface
%py_requires zope.publisher zope.app.schema

%description
This addon is a ckeditor integration for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2-tests
%py_requires plone.app.testing Products.PloneTestCase zope.testing
%py_requires zope.security.testing

%description tests
This addon is a ckeditor integration for Plone.

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
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1.b3.dev0.git20140619
- Initial build for Sisyphus

