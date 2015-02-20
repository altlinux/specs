%define mname collective
%define oname %mname.registrationcaptcha
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20150218
Summary: Add a captcha field to the registration form
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.registrationcaptcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.registrationcaptcha.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.app.users
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-plone.formwidget.captcha
BuildPreReq: python-module-plone.formwidget.recaptcha
BuildPreReq: python-module-collective.z3cform.norobots

%py_provides %oname
%py_requires %mname Products.CMFCore plone.app.discussion plone.protect
%py_requires plone.app.users plone.registry plone.z3cform z3c.form
%py_requires zope.component zope.interface zope.publisher
%py_requires plone.formwidget.captcha plone.formwidget.recaptcha
%py_requires collective.z3cform.norobots

%description
Add a captcha field to the @@register form for anonymous users form to
secure it from spam bots.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20150218
- Initial build for Sisyphus

