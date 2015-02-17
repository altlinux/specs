%define mname collective.edm
%define oname %mname.listing
Name: python-module-%oname
Version: 0.12
Release: alt1
Summary: Integration of a filer explorer like listing in Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.edm.listing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-collective.externaleditor
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ExternalEditor
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires collective.quickupload collective.externaleditor
%py_requires Products.statusmessages Products.CMFCore Products.CMFPlone
%py_requires Products.ExternalEditor Products.CMFPlacefulWorkflow
%py_requires Products.CMFEditions plone.registry plone.memoize
%py_requires plone.app.content plone.app.layout zope.interface
%py_requires zope.component zope.i18nmessageid zope.security
%py_requires zope.publisher zope.browserpage zope.schema

%description
A view for folders that provides file-explorer like document adding and
management tools.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
A view for folders that provides file-explorer like document adding and
management tools.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/edm/__init__.py \
	%buildroot%python_sitelibdir/collective/edm/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/collective/edm/listing
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/edm/listing/tests.*

%files tests
%python_sitelibdir/collective/edm/listing/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/edm
%python_sitelibdir/collective/edm/__init__.py*

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1
- Initial build for Sisyphus

