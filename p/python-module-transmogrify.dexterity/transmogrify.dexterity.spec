%define mname transmogrify
%define oname %mname.dexterity
Name: python-module-%oname
Version: 1.5
Release: alt1.dev0.git20141106
Summary: A transmogrifier blueprint for updating dexterity objects
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/transmogrify.dexterity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/transmogrify.dexterity.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.transmogrifier-tests
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.app.transmogrifier
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname collective.transmogrifier plone.app.textfield
%py_requires plone.app.transmogrifier plone.dexterity plone.namedfile
%py_requires plone.supermodel plone.uuid z3c.form zope.interface
%py_requires zope.component zope.schema zope.lifecycleevent zope.event
%py_requires zope.dottedname

%description
The transmogrify.dexterity package provides a transmogrifier pipeline
section for updating field values of dexterity content objects. The
blueprint name is transmogrify.dexterity.schemaupdater.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.dexterity plone.directives.form
%py_requires zope.testing zope.configuration
%py_requires collective.transmogrifier.sections.tests

%description tests
The transmogrify.dexterity package provides a transmogrifier pipeline
section for updating field values of dexterity content objects. The
blueprint name is transmogrify.dexterity.schemaupdater.

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
%doc *.rst examples
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.dev0.git20141106
- Initial build for Sisyphus

