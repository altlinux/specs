%define oname Products.PFGVerkkomaksut
Name: python-module-%oname
Version: 0.11.0
Release: alt1.svn20110403
Summary: Provides verkkomaksut payment adapter to Products.PloneFormGen package
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PFGVerkkomaksut/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.PFGVerkkomaksut/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PasteScript
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PloneFormGen Products.CMFCore Products.CMFPlone
%py_requires Products.statusmessages Products.Archetypes zope.schema
%py_requires Products.ATContentTypes Products.GenericSetup zope.viewlet
%py_requires zope.interface zope.i18nmessageid

%description
Products.PFGVerkkomaksut provides verkkomaksut payment adapter to
Products.PloneFormGen package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase Products.MailHost
%py_requires zope.component.testing zope.security.testing

%description tests
Products.PFGVerkkomaksut provides verkkomaksut payment adapter to
Products.PloneFormGen package.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.svn20110403
- Initial build for Sisyphus

