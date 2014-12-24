%define mname ftw
%define oname %mname.lawgiver
Name: python-module-%oname
Version: 1.5.1
Release: alt1.dev0.git20141208
Summary: Generate your Plone workflows by describing it in plain text with a DSL
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.lawgiver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.lawgiver.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-argparse python-module-i18ndude
BuildPreReq: python-module-lxml python-module-ordereddict
BuildPreReq: python-module-transaction python-module-unittest2
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-collective.deletepermission
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.workflow
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.dottedname

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.CMFPlone ZODB3 i18ndude
%py_requires Products.GenericSetup Products.statusmessages argparse
%py_requires collective.deletepermission ftw.upgrade lxml plone.i18n
%py_requires plone.app.workflow zope.component zope.configuration
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.schema Products.CMFCore

%description
ftw.lawgiver generates Plone workflows based on a human readable
specification written in a custom DSL.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing ftw.testbrowser ftw.testing
%py_requires plone.app.testing plone.browserlayer plone.mocktestcase
%py_requires plone.testing zope.dottedname

%description tests
ftw.lawgiver generates Plone workflows based on a human readable
specification written in a custom DSL.

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
%doc *.md *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.dev0.git20141208
- Initial build for Sisyphus

