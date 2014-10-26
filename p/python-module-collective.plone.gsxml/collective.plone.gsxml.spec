%define mname collective.plone
%define oname %mname.gsxml

%def_disable check

Name: python-module-%oname
Version: 0.4.7
Release: alt1.svn20090507
Summary: An XML import/export add-on for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.plone.gsxml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://svn.plone.org/svn/collective/gsxml/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Marshall
BuildPreReq: python-module-Products.PloneArticle
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.i18nmessageid zope.event zope.component zope.interface
%py_requires zope.schema zope.lifecycleevent zope.formlib
%py_requires Products.CMFCore Products.Marshall
%py_requires Products.PloneArticle Products.Archetypes Products.CMFPlone

%description
A package for importing and exporting content from Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2
%py_requires zope.app.testing Products.PloneTestCase
%py_requires zope.component.testing zope.security.testing

%description tests
A package for importing and exporting content from Plone.

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

install -p -m644 src/collective/plone/__init__.py \
	%buildroot%python_sitelibdir/collective/plone/

%check
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/collective/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/plone/*/tests
%exclude %python_sitelibdir/collective/plone/__init__.py*

%files tests
%python_sitelibdir/collective/plone/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/collective/plone
%python_sitelibdir/collective/plone/__init__.py*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.svn20090507
- Initial build for Sisyphus

