%define mname archetypes
%define oname %mname.testcase

%def_disable check

Name: python-module-%oname
Version: 1.0
Release: alt1.git20120906
Summary: Test Archetypes-based Plone content type for Multilingual
License: GPLv2+
Group: Development/Python
Url: https://github.com/sneridagh/archetypes.testcase
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sneridagh/archetypes.testcase.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PasteScript
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.PloneTestCase Products.CMFCore
%py_requires zope.testing Products.Archetypes Products.ATContentTypes
%py_requires plone.app.testing zope.configuration zope.interface
%py_requires zope.i18nmessageid

%description
Test Archetypes-based Plone content type for Multilingual.

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
%doc *.txt *.md docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20120906
- Initial build for Sisyphus

