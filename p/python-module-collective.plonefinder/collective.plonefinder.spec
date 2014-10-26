%define mname collective
%define oname %mname.plonefinder
Name: python-module-%oname
Version: 1.0.8
Release: alt1.dev0.git20140915
Summary: A finder to search/select portal objects for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.plonefinder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.plonefinder.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.quickupload

%py_provides %oname
%py_requires %mname collective.quickupload

%description
Ajax popup to browse and select plone contents, suitable to any
plone.formilb form (portlets, control panels, ...)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Ajax popup to browse and select plone contents, suitable to any
plone.formilb form (portlets, control panels, ...)

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
%doc *.txt *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.dev0.git20140915
- Initial build for Sisyphus

