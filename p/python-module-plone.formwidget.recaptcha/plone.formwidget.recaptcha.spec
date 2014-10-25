%define mname plone.formwidget
%define oname %mname.recaptcha
Name: python-module-%oname
Version: 1.0
Release: alt1.b4.git20101118
Summary: ReCaptcha widget for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.recaptcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.recaptcha.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-recaptcha-client
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires %mname plone.z3cform plone.registry plone.app.registry
%py_requires recaptcha.client

%description
plone.formwidget.recaptcha is a z3c.form ReCaptcha widget for use with
Plone. It is a z3c.form re-implementation of the collective.recaptcha
package written by David Glick.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
plone.formwidget.recaptcha is a z3c.form ReCaptcha widget for use with
Plone. It is a z3c.form re-implementation of the collective.recaptcha
package written by David Glick.

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
nosetests

%files
%doc *.txt docs/*
%python_sitelibdir/plone/formwidget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/formwidget/*/tests.*
%exclude %python_sitelibdir/plone/formwidget/__init__.py*

%files tests
%python_sitelibdir/plone/formwidget/*/tests.*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b4.git20101118
- Initial build for Sisyphus

