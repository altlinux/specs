%define oname plone.behavior
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev0.git20140823
Summary: Infrastructure for maintaining a registry of available behaviors
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.behavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.behavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires plone zope.component zope.interface zope.schema
%py_requires zope.annotation zope.configuration

%description
This package provides optional support for "behaviors". A behavior is a
re-usable aspect of an object that can be enabled or disabled without
changing the component registry.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides optional support for "behaviors". A behavior is a
re-usable aspect of an object that can be enabled or disabled without
changing the component registry.

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
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20140823
- Initial build for Sisyphus

