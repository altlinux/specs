%define oname plone.keyring
Name: python-module-%oname
Version: 3.0.1
Release: alt1.dev0.git20140826
Summary: Zope utility that facilitates handling of secrets in an application
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.keyring/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.keyring.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPReReq: python-module-zope.container
BuildPReReq: python-module-zope.location

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone ZODB3 zope.container zope.interface zope.location

%description
plone.keyring contains a Zope utility that facilitates handling of
secrets in an application. Secrets are very important in modern
applications, which is why a shared tool to manage them is useful.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
plone.keyring contains a Zope utility that facilitates handling of
secrets in an application. Secrets are very important in modern
applications, which is why a shared tool to manage them is useful.

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
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.dev0.git20140826
- Initial build for Sisyphus

