%define mname ftw
%define oname %mname.zipexport
Name: python-module-%oname
Version: 1.2.2
Release: alt1.dev0.git20141107
Summary: Zip export for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.zipexport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.zipexport.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-z3c.blobfile
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore ftw.upgrade plone.app.dexterity
%py_requires plone.namedfile Products.ATContentTypes plone.registry
%py_requires Products.statusmessages plone.rfc822 zope.i18nmessageid
%py_requires zope.component zope.interface zope.publisher zope.schema
%py_requires zope.dottedname

%description
ftw.zipexport provides a generic solution to export data from plone in a
zip archive.

A user can export data with the "Export as Zip" action in document
listings.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing plone.app.testing plone.directives.form
%py_requires z3c.blobfile Products.CMFPlone zope.configuration

%description tests
ftw.zipexport provides a generic solution to export data from plone in a
zip archive.

A user can export data with the "Export as Zip" action in document
listings.

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
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20141107
- Initial build for Sisyphus

