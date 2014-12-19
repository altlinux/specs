%define mname collective
%define oname %mname.captchacontactinfo
Name: python-module-%oname
Version: 1.2.2
Release: alt1.dev0.git20141217
Summary: A simple customization for Plone contact-info that add recaptcha for anonymous users
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.captchacontactinfo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.captchacontactinfo.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.recaptcha python-module-openid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.recaptcha Products.CMFCore zope.interface
%py_requires Products.CMFPlone plone.app.controlpanel zope.formlib
%py_requires zope.schema zope.i18nmessageid

%description
A simple Plone customization for the "Contact form" form that add a
captcha regognition for anonymous users.

When anonymous try to use contact-info form, they must provide also a
captcha protection value.

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
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20141217
- Initial build for Sisyphus

