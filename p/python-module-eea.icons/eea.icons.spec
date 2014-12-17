%define mname eea
%define oname %mname.icons
Name: python-module-%oname
Version: 1.4
Release: alt1
Summary: EEA Icons used throughout the EEA sites
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.icons/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires %mname Products.CMFCore zope.interface zope.i18nmessageid

%description
Font Awesome icons for Plone and EEA packages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
Font Awesome icons for Plone and EEA packages.

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
%doc *.md *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

