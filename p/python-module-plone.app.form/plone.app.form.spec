%define oname plone.app.form

%def_disable check

Name: python-module-%oname
Version: 2.3.1
Release: alt1.dev0.git20140925
Summary: zope.formlib integration for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.form/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.form.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.formlib
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.contentlisting
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app five.formlib plone.app.vocabularies plone.locking
%py_requires Products.CMFCore Products.CMFDefault zope.browser zope.i18n
%py_requires zope.component zope.event zope.formlib zope.i18nmessageid
%py_requires zope.interface zope.lifecycleevent zope.schema zope.site

%description
The plone.app.form package gives Plone the ability to better adapt
common zope.formlib UI style functionality to a more appropriate Plone
style.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.content plone.app.testing plone.memoize
%py_requires zope.annotation zope.publisher zope.testing

%description tests
The plone.app.form package gives Plone the ability to better adapt
common zope.formlib UI style functionality to a more appropriate Plone
style.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.dev0.git20140925
- Initial build for Sisyphus

