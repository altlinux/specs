%define mname eea.faceted
%define oname %mname.vocabularies
Name: python-module-%oname
Version: 5.1
Release: alt1.dev.git20141014
Summary: EEA Faceted Vocabularies for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.faceted.vocabularies/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.faceted.vocabularies.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.app.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires Products.CMFCore zope.schema zope.interface zope.app.schema
%py_requires zope.i18nmessageid zope.component

%description
Zope 3 vocabularies to be used within eea.facetednavigation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.browserresource zope.configuration
%py_requires zope.component.testing

%description tests
Zope 3 vocabularies to be used within eea.facetednavigation.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires eea

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

install -p -m644 eea/faceted/__init__.py \
	%buildroot%python_sitelibdir/eea/faceted/
pushd eea/faceted/vocabularies
cp -fR *.txt *.zcml documentation locales \
	%buildroot%python_sitelibdir/eea/faceted/vocabularies/
popd

%check
python setup.py test

%files
%doc *.md *.txt docs/*
%python_sitelibdir/eea/faceted/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/eea/faceted/*/tests.*
%exclude %python_sitelibdir/eea/faceted/__init__.py*

%files tests
%python_sitelibdir/eea/faceted/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/eea/faceted
%python_sitelibdir/eea/faceted/__init__.py*

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.dev.git20141014
- Initial build for Sisyphus

