%define mname eea
%define oname %mname.translations
Name: python-module-%oname
Version: 6.4
Release: alt1
Summary: Translations for EEA website
License: GPLv2+ / MPL
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.translations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires %mname zope.publisher zope.i18nmessageid

%description
Translations for EEA website. Most translations come from old
local.eea.europa.eu website. We also have translated logos here.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2
%py_requires Products.PloneTestCase

%description tests
Translations for EEA website. Most translations come from old
local.eea.europa.eu website. We also have translated logos here.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests*

%files tests
%python_sitelibdir/%mname/*/tests*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.4-alt1
- Initial build for Sisyphus

