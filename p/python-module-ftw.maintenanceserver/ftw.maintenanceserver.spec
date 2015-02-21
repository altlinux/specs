%define mname ftw
%define oname %mname.maintenanceserver
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev0.git20150121
Summary: Maintenance HTTP server, serving a static directory
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.maintenanceserver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.maintenanceserver.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-plone.testing

%py_provides %oname
%py_requires %mname

%description
Provides a simple server serving a static directory, which can be
configured as haproxy backup server, kicking in when all normal servers
are offline.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testbrowser plone.testing unittest2

%description tests
Provides a simple server serving a static directory, which can be
configured as haproxy backup server, kicking in when all normal servers
are offline.

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
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20150121
- Initial build for Sisyphus

