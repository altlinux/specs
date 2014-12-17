%define mname eea
%define oname %mname.vocab
Name: python-module-%oname
Version: 4.6
Release: alt1
Summary: Provides vocabularies commonly used through the EEA Site
License: GPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.vocab/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ATVocabularyManager zope.schema
%py_requires Products.MimetypesRegistry zope.interface zope.component

%description
eea.vocab provides vocabularies commonly used through the EEA Site. It
was designed to be small and light so that other products using one of
these vocabularies wouldn't have to depend on other heavy weight
products or copy/paste code.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
eea.vocab provides vocabularies commonly used through the EEA Site. It
was designed to be small and light so that other products using one of
these vocabularies wouldn't have to depend on other heavy weight
products or copy/paste code.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1
- Initial build for Sisyphus

