%define mname collective
%define oname %mname.dancing
Name: python-module-%oname
Version: 1.0
Release: alt1.dev.git20141020
Summary: The all-singing all-dancing newsletter add-on for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dancing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dancing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-StoneageHTML python-module-BeautifulSoup
BuildPreReq: python-module-collective.singing
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-five.intid
BuildPreReq: python-module-zc.lockfile
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-zope.testbrowser
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zc.queue
BuildPreReq: python-module-z3c.formwidget.query
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.singing plone.z3cform plone.app.z3cform
%py_requires five.intid zc.lockfile collective.monkeypatcher plone.uuid
%py_requires Products.CMFPlone Products.CMFCore Products.ATContentTypes
%py_requires Products.statusmessages plone.app.portlets plone.portlets
%py_requires plone.memoize zope.i18nmessageid zope.annotation zope.event
%py_requires zope.app.component zope.component zope.sendmail zope.schema
%py_requires zope.publisher zope.app.container zope.lifecycleevent
%py_requires zope.interface zope.i18n zope.browserpage zc.queue
%py_requires zope.app.pagetemplate z3c.formwidget.query z3c.form

%description
Singing & Dancing is the next generation newsletter Product for Plone.
It's an out of the box solution that works without modification for most
of your use cases. And should you find something that Singing & Dancing
can't do, it's built to be easily extended via plug-ins using the Zope 3
Component Architecture.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testbrowser Products.PloneTestCase zope.testing

%description tests
Singing & Dancing is the next generation newsletter Product for Plone.
It's an out of the box solution that works without modification for most
of your use cases. And should you find something that Singing & Dancing
can't do, it's built to be easily extended via plug-ins using the Zope 3
Component Architecture.

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

pushd %mname/dancing
cp -fR *.txt *.zcml Extensions locales profiles resources \
	%buildroot%python_sitelibdir/%mname/dancing/
install -p -m644 browser/*.pt browser/*.zcml \
	%buildroot%python_sitelibdir/%mname/dancing/browser/
install -p -m644 browser/portlets/*.pt browser/portlets/*.zcml \
	%buildroot%python_sitelibdir/%mname/dancing/browser/portlets/
popd

%check
python setup.py test
py.test collective/dancing/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.dev.git20141020
- Initial build for Sisyphus

