%define mname archetypes
%define oname %mname.multilingual
Name: python-module-%oname
Version: 1.3
Release: alt1.dev.git20130924
Summary: Multilingual support for archetypes
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/archetypes.multilingual/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/archetypes.multilingual.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.multilingual
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-Products.PloneLanguageTool
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-archetypes.testcase
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname Products.ATContentTypes plone.multilingual
%py_requires collective.monkeypatcher Products.PloneLanguageTool
%py_requires Products.CMFPlone Products.CMFCore zope.interface
%py_requires zope.lifecycleevent zope.event zope.component

%description
This egg adds the glue between plone.app.multilingual and
plone.multilingual for Archetype-based Content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing archetypes.testcase Products.Archetypes
%py_requires plone.testing zope.configuration

%description tests
This egg adds the glue between plone.app.multilingual and
plone.multilingual for Archetype-based Content.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev.git20130924
- Initial build for Sisyphus

