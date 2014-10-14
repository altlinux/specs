%define oname Products.validation
Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20120103
Summary: Data validation package for Archetypes
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.validation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.validation.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.i18n python-module-docutils
BuildPreReq: python-module-zope.i18nmessageid
#BuildPreReq: python-module-Products.Archetypes

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.i18n zope.i18nmessageid zope.interface

%description
Data validation package for Archetypes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#py_requires Products.Archetypes

%description tests
Data validation package for Archetypes.

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
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20120103
- Initial build for Sisyphus

