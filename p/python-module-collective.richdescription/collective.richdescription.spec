%define mname collective
%define oname %mname.richdescription
Name: python-module-%oname
Version: 2.0
Release: alt1.gi20141111
Summary: Turns Plone 'Description' field into Richtext/HTML
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.richdescription/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.richdescription.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.component zope.interface Products.Archetypes
%py_requires archetypes.schemaextender plone.app.dexterity
%py_requires plone.app.textfield plone.behavior plone.autoform
%py_requires plone.dexterity plone.supermodel Products.LinguaPlone
%py_requires Products.CMFPlone

%description
Adds the new html-formatable textfield "richdescription" to Archetypes
based content types and hides the description field from
ExtensibleMetadata. When the field is saved, the contents are also
stored in the "description" field, but without html-formating. A
Metadata index is provided, so that "richdescription" can be used with
catalog brains.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Adds the new html-formatable textfield "richdescription" to Archetypes
based content types and hides the description field from
ExtensibleMetadata. When the field is saved, the contents are also
stored in the "description" field, but without html-formating. A
Metadata index is provided, so that "richdescription" can be used with
catalog brains.

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
export PYTHONPATH=$PWD/src
python src/collective/richdescription/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.gi20141111
- Initial build for Sisyphus

