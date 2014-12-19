%define mname collective
%define oname %mname.recaptcha
Name: python-module-%oname
Version: 1.1.6
Release: alt1.dev0.git20140507
Summary: Wraps the recaptcha-client library to provide a drop-in replacement for collective.captcha
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.recaptcha/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.recaptcha.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-recaptcha-client python-module-openid
BuildPreReq: python-module-Plone
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.formwidget.recaptcha
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname recaptcha.client Plone plone.formwidget.recaptcha
%py_requires plone.registry zope.app.component zope.component
%py_requires zope.app.container zope.browser zope.app.pagetemplate
%py_requires zope.browserpage zope.formlib zope.annotation zope.schema
%py_requires zope.interface zope.publisher zope.i18nmessageid

%description
This package provides an integration of the Recaptcha service into Zope.
Recaptcha is a third-party CAPTCHA service provided by Carnegie Mellon
University. One of its most interesting features is that the act of
users answering CAPTCHAs contributes to efforts to digitize books.

The API is based on collective.captcha and is provided via a "@@captcha"
browser view, so these two packages can be swapped for each other
relatively simply. Use collective.captcha if you need to not be
dependent on an external service; use collective.recaptcha for a
slightly better user experience.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package provides an integration of the Recaptcha service into Zope.
Recaptcha is a third-party CAPTCHA service provided by Carnegie Mellon
University. One of its most interesting features is that the act of
users answering CAPTCHAs contributes to efforts to digitize books.

The API is based on collective.captcha and is provided via a "@@captcha"
browser view, so these two packages can be swapped for each other
relatively simply. Use collective.captcha if you need to not be
dependent on an external service; use collective.recaptcha for a
slightly better user experience.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1.dev0.git20140507
- Initial build for Sisyphus

