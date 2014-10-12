%define oname plone.i18n
Name: python-module-%oname
Version: 2.0.10
Release: alt1.dev0.git20140823
Summary: Advanced i18n/l10n features
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.i18n/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.i18n.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-unidecode
BuildPreReq: python-module-zope.component python-module-plone
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires plone zope.component zope.i18n zope.interface
%py_requires zope.publisher

%description
Advanced i18n/l10n features useful in a CMS environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.browserresource zope.component zope.configuration
%py_requires zope.testing

%description tests
Advanced i18n/l10n features useful in a CMS environment.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/*/tests

%files tests
%python_sitelibdir/plone/*/*/tests

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.10-alt1.dev0.git20140823
- Initial build for Sisyphus

