%define mname collective.js
%define oname %mname.galleria
Name: python-module-%oname
Version: 1.2.6
Release: alt1.dev0.git20140424
Summary: Register Galleria JQuery plugin in Plone's resource registries
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.galleria/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.galleria.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires %mname Products.CMFCore

%description
This addon register Galleria JQuery plugin in Plone's resource
registries.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This addon register Galleria JQuery plugin in Plone's resource
registries.

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
%doc *.rst docs/*
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/js/*/test*

%files tests
%python_sitelibdir/collective/js/*/test*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev0.git20140424
- Initial build for Sisyphus

