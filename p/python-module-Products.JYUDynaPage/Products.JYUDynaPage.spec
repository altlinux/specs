%define oname Products.JYUDynaPage
Name: python-module-%oname
Version: 2.0
Release: alt1.svn20120418
Summary: Plone page with configurable dynamic lists in top and bottom of the content
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.JYUDynaPage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.JYUDynaPage/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.contentmigration

%description
Products.JYUDynaPage is a replacement to old mxmDynamicPage product for
Plone 3. DynaPage content type is like normal page content type, but it
has easily configurable lists (well at least easier than collections
are) which can be placed below or above the normal page content. List
items can consist any Plone content found from catalog.

Products.JYUDynaPage contains also migration script to migrate data from
old mxmDynamicPage- product to Products.JYUDynaPage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.Archetypes zope.component.testing
%py_requires zope.security.testing Products.PloneTestCase

%description tests
Products.JYUDynaPage is a replacement to old mxmDynamicPage product for
Plone 3. DynaPage content type is like normal page content type, but it
has easily configurable lists (well at least easier than collections
are) which can be placed below or above the normal page content. List
items can consist any Plone content found from catalog.

Products.JYUDynaPage contains also migration script to migrate data from
old mxmDynamicPage- product to Products.JYUDynaPage.

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
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20120418
- Initial build for Sisyphus

