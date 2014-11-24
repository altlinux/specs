%define mname plone.formwidget
%define oname %mname.captcha
Name: python-module-%oname
Version: 1.0.3
Release: alt2.dev0.git20140903
Summary: A z3c.form captcha widget for use with Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.captcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.captcha.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-skimpyGimpy
BuildPreReq: python-module-plone.keyring
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.password-tests
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires %mname plone.keyring plone.z3cform

%description
plone.formwidget.captcha is a z3c.form captcha widget for use with
Plone. It is a z3c.form re-implementation of the collective.captcha
package written by Martijn Pieters.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.app.testing zope.component.testing
%py_requires zope.password.testing

%description tests
plone.formwidget.captcha is a z3c.form captcha widget for use with
Plone. It is a z3c.form re-implementation of the collective.captcha
package written by Martijn Pieters.

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
%doc *.rst docs/*
%python_sitelibdir/plone/formwidget/*
%exclude %python_sitelibdir/plone/formwidget/__init__.py*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/formwidget/*/test*
%exclude %python_sitelibdir/plone/formwidget/*/*/test*

%files tests
%python_sitelibdir/plone/formwidget/*/test*
%python_sitelibdir/plone/formwidget/*/*/test*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.dev0.git20140903
- Avoid conflict with plone.formwidget.captcha and plone.formwidget

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20140903
- Initial build for Sisyphus

