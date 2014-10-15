%define oname plone.stringinterp
Name: python-module-%oname
Version: 1.1.1
Release: alt1.dev0.git20140826
Summary: Adaptable string interpolation
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.stringinterp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.stringinterp.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.i18n

%py_provides %oname
%py_requires plone Products.CMFCore zope.i18n

%description
Provides ${id} style string interpolation using named adapters to look
up variables. This is meant to provide a trivially simple template
system for clients like plone.app.contentrules.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides ${id} style string interpolation using named adapters to look
up variables. This is meant to provide a trivially simple template
system for clients like plone.app.contentrules.

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
%exclude %python_sitelibdir/plone/*/tests

%files tests
%python_sitelibdir/plone/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20140826
- Initial build for Sisyphus

