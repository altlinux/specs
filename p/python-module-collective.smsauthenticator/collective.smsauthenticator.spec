%define mname collective
%define oname %mname.smsauthenticator
Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20150212
Summary: Two-step verification in Plone 4 using login codes sent by SMS
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.smsauthenticator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.smsauthenticator.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ska python-module-rebus
BuildPreReq: python-module-twilio python-module-robotsuite
BuildPreReq: python-module-mockup python-module-openid
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.users
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-grokcore.component-tests
BuildPreReq: python-module-grokcore.annotation-tests
BuildPreReq: python-module-grokcore.security-tests
BuildPreReq: python-module-grokcore.site-tests
BuildPreReq: python-module-grokcore.view-tests
BuildPreReq: python-module-grokcore.viewlet-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.api plone.directives.form ska rebus twilio
%py_requires Products.PluggableAuthService Products.statusmessages
%py_requires Products.CMFCore Products.CMFPlone Products.PlonePAS
%py_requires plone.registry plone.app.users plone.autoform plone.z3cform
%py_requires plone.app.registry zope.interface zope.i18nmessageid
%py_requires zope.globalrequest zope.component zope.schema z3c.form

%description
Two-step verification for Plone 4 with use login codes sent by SMS. This
app allows users to enable the two-step verification for their Plone
accounts. A mobile phone capable to receive SMS messages is obviously
required. Usage of two-step verification is optonal, unless site admins
have forced it (configurable in app control panel). Admins can
white-list the IPs, for which the two-step verification would be
skipped.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing robotsuite zope.configuration

%description tests
Two-step verification for Plone 4 with use login codes sent by SMS. This
app allows users to enable the two-step verification for their Plone
accounts. A mobile phone capable to receive SMS messages is obviously
required. Usage of two-step verification is optonal, unless site admins
have forced it (configurable in app control panel). Admins can
white-list the IPs, for which the two-step verification would be
skipped.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Two-step verification for Plone 4 with use login codes sent by SMS. This
app allows users to enable the two-step verification for their Plone
accounts. A mobile phone capable to receive SMS messages is obviously
required. Usage of two-step verification is optonal, unless site admins
have forced it (configurable in app control panel). Admins can
white-list the IPs, for which the two-step verification would be
skipped.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Two-step verification for Plone 4 with use login codes sent by SMS. This
app allows users to enable the two-step verification for their Plone
accounts. A mobile phone capable to receive SMS messages is obviously
required. Usage of two-step verification is optonal, unless site admins
have forced it (configurable in app control panel). Admins can
white-list the IPs, for which the two-step verification would be
skipped.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.txt *.rst examples
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/%mname/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150212
- Initial build for Sisyphus

