%define oname Products.mediaPerson
Name: python-module-%oname
Version: 0.4
Release: alt1.svn20130221
Summary: Person type with folderish behaviour to store related media
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.mediaPersons/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.mediaPerson/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PasteScript
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.ATContentTypes Products.Archetypes zope.interface
%py_requires Products.CMFCore zope.i18nmessageid

%description
Person type with folderish behaviour to store related media.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
Person type with folderish behaviour to store related media.

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
rm -fR build
py.test

%files
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.svn20130221
- Initial build for Sisyphus

