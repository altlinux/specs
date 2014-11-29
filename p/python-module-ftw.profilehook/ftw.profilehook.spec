%define mname ftw
%define oname %mname.profilehook
Name: python-module-%oname
Version: 1.0.1
Release: alt1.dev0.git20141107
Summary: Hook for executing code when a generic setup profile is installed
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.profilehook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.profilehook.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname Products.CMFCore zope.schema zope.component
%py_requires zope.interface zope.configuration

%description
ftw.profilehook provides a hook for executing custom code after a
generic setup profile is installed.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
ftw.profilehook provides a hook for executing custom code after a
generic setup profile is installed.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20141107
- Initial build for Sisyphus

