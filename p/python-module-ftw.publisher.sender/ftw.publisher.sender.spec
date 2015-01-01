%define mname ftw.publisher
%define oname %mname.sender
Name: python-module-%oname
Version: 2.2.2
Release: alt1.dev0.git20141231
Summary: Staging and publishing addon for Plone contents
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.publisher.sender/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.publisher.sender.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zExceptions python-module-transaction
BuildPreReq: python-module-argparse python-module-cssselect
BuildPreReq: python-module-openid
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-ftw.publisher.core
BuildPreReq: python-module-ftw.table
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-ftw.lawgiver
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.contentpage

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zExceptions zope.annotation zope.component ZODB3
%py_requires zope.event zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.schema zope.viewlet plone.memoize Products.ZCatalog
%py_requires Products.statusmessages Products.CMFCore Products.CMFPlone
%py_requires ftw.publisher.core ftw.table ftw.upgrade z3c.form
%py_requires plone.z3cform Products.PloneFormGen ftw.lawgiver

%description
The sender package provides a configuration panel and is responsible for
sending contents to the target instance. It's usually installed on a
editorial site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.testcaselayer plone.app.testing ftw.testing
%py_requires Products.PloneTestCase ftw.builder.testing ftw.contentpage

%description tests
The sender package provides a configuration panel and is responsible for
sending contents to the target instance. It's usually installed on a
editorial site.

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
%python_sitelibdir/ftw/publisher/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/publisher/*/test*
%exclude %python_sitelibdir/ftw/publisher/*/*/example*

%files tests
%python_sitelibdir/ftw/publisher/*/test*
%python_sitelibdir/ftw/publisher/*/*/example*

%changelog
* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1.dev0.git20141231
- Version 2.2.2.dev0

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.dev0.git20141107
- Initial build for Sisyphus

