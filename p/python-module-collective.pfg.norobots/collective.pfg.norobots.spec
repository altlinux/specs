%define mname collective.pfg
%define oname %mname.norobots

Name: python-module-%oname
Version: 1.1
Release: alt2.dev0.git20121108
Summary: PloneFormGen field using collective.z3cform.norobots
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.pfg.norobots/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sylvainb/collective.pfg.norobots.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-collective.z3cform.norobots

%py_provides %oname
%py_requires %mname Products.PloneFormGen Products.Archetypes zope.event
%py_requires Products.CMFCore Products.ATContentTypes zope.i18nmessageid
%py_requires zope.component zope.lifecycleevent
%py_requires collective.z3cform.norobots

%description
collective.pfg.norobots allows to add a collective.z3cform.norobots
captcha field to PloneFormGen forms.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing plone.app.testing Products.validation
%py_requires plone.registry plone.app.dexterity plone.app.collection
%py_requires plone.app.caching z3c.form.testing

%description tests
collective.pfg.norobots allows to add a collective.z3cform.norobots
captcha field to PloneFormGen forms.

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
%python_sitelibdir/collective/pfg/norobots
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/pfg/norobots/test*

%files tests
%python_sitelibdir/collective/pfg/norobots/test*

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.dev0.git20121108
- Added necessary requirements
- Enabled testing

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev0.git20121108
- Initial build for Sisyphus

