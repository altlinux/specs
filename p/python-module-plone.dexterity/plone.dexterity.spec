%define oname plone.dexterity
Name: python-module-%oname
Version: 2.2.4
Release: alt1.dev0.git20140923
Summary: Base framework for building content types
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.dexterity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.dexterity.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.alterego
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.synchronize
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.browser
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.filerepresentation
BuildPreReq: python-module-zope.size
BuildPreReq: python-module-plone.mocktestcase
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.filerepresentation zope.size ZODB3
%py_requires zope.location zope.publisher zope.schema zope.security
%py_requires zope.dottedname zope.interface zope.lifecycleevent
%py_requires zope.annotation zope.browser zope.component zope.container
%py_requires Products.CMFDynamicViewFTI Products.statusmessages
%py_requires plone.synchronize plone.uuid plone.z3cform Products.CMFCore
%py_requires plone.folder plone.memoize plone.rfc822 plone.supermodel
%py_requires plone plone.alterego plone.autoform plone.behavior

%description
Dexterity is a system for building content types, both through-the-web
and as filesystem code. It is aimed at Plone, although this package
should work with plain Zope + CMF systems.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.mocktestcase plone.testing

%description tests
Dexterity is a system for building content types, both through-the-web
and as filesystem code. It is aimed at Plone, although this package
should work with plain Zope + CMF systems.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4-alt1.dev0.git20140923
- Initial build for Sisyphus

