%define oname Products.XLIFFMarshall
Name: python-module-%oname
Version: 1.1
Release: alt1.svn20091105
Summary: Export and import translations into and from Plone in XLIFF format
License: GPL
Group: Development/Python
Url: http://svn.plone.org/svn/collective/Products.XLIFFMarshall/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/Products.XLIFFMarshall/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-BeautifulSoup
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Marshall
BuildPreReq: python-module-Products.OrderableReferenceField
BuildPreReq: python-module-Products.Archetypes-tests
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-Products.LinguaPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.CMFCore Products.Marshall
%py_requires Products.OrderableReferenceField Products.Archetypes
%py_requires Products.ATContentTypes zope.interface zope.event
%py_requires zope.app.component zope.app.annotation zope.component

%description
Export and import translations into and from Plone in XLIFF format.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.LinguaPlone Products.Archetypes.tests

%description tests
Export and import translations into and from Plone in XLIFF format.

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

pushd Products/XLIFFMarshall
cp -fR *.txt *.zcml docs profiles skins \
	%buildroot%python_sitelibdir/Products/XLIFFMarshall/
cp -fR *.txt *.zcml docs profiles skins \
	%buildroot%python_sitelibdir/Products/XLIFFMarshall/
install -p -m644 browser/*.zcml \
	%buildroot%python_sitelibdir/Products/XLIFFMarshall/browser/
cp -fR tests/Person/*.txt tests/Person/Extensions \
	%buildroot%python_sitelibdir/Products/XLIFFMarshall/tests/Person/
cp -fR tests/xliff \
	%buildroot%python_sitelibdir/Products/XLIFFMarshall/tests/
popd

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
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.svn20091105
- Initial build for Sisyphus

