%define mname eea
%define oname %mname.relations
Name: python-module-%oname
Version: 7.2
Release: alt1.dev.git20141120
Summary: Redefines relations in Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.relations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.relations.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-pydot
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-eea.facetednavigation
BuildPreReq: python-module-Products.TALESField
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.jquery eea.facetednavigation Products.TALESField
%py_requires Products.CMFCore Products.ATContentTypes zope.interface
%py_requires Products.Archetypes Products.GenericSetup zope.component
%py_requires Products.statusmessages Products.validation zope.schema
%py_requires zope.lifecycleevent zope.event

%description
EEA Relations package redefines relations in Plone. Right now in Plone
any object can be in relation with any other object. EEA Relations lets
you to define possible relations between objects. EEA Relations also
comes with a nice, customizable faceted navigable popup for relations
widget.

Once installed from "Add-ons", the package will add an utility called
"Possible relations" under "Control Panel".

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing Products.PloneTestCase

%description tests
EEA Relations package redefines relations in Plone. Right now in Plone
any object can be in relation with any other object. EEA Relations lets
you to define possible relations between objects. EEA Relations also
comes with a nice, customizable faceted navigable popup for relations
widget.

Once installed from "Add-ons", the package will add an utility called
"Possible relations" under "Control Panel".

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR %mname/relations %buildroot%python_sitelibdir/%mname/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.md *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.dev.git20141120
- Initial build for Sisyphus

