%define mname ftw
%define oname %mname.dictstorage
Name: python-module-%oname
Version: 1.3
Release: alt1.dev0.git20141107
Summary: Provides a layer for storing key / value paires
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.dictstorage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.dictstorage.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-SQLAlchemy
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-plone.testing

%py_provides %oname
%py_requires %mname zope.component zope.configuration zope.security
%py_requires sqlalchemy

%description
This package provides a layer for storing key / value paires. The
storage can be configured dinamically by providing a IConfig adapter of
the context on which the dict storage is used.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing

%description tests
This package provides a layer for storing key / value paires. The
storage can be configured dinamically by providing a IConfig adapter of
the context on which the dict storage is used.

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
py.test ftw/dictstorage/*.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0.git20141107
- Initial build for Sisyphus

