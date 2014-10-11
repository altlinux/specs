%define oname Products.LDAPMultiPlugins
Name: python-module-%oname
Version: 2.0
Release: alt1.dev.git20111218
Summary: LDAP-backed plugins for the Zope2 PluggableAuthService
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.LDAPMultiPlugins
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://git.dataflake.org/git/Products.LDAPMultiPlugins.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ldap python-module-Products.LDAPUserFolder
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-sphinx-devel python-module-pkginfo
BuildPreReq: python-module-repoze.sphinx.autointerface

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.LDAPUserFolder Products.PluggableAuthService
%py_requires Products.GenericSetup

%description
The LDAPMultiPlugins provides PluggableAuthService plugins that use LDAP
as the backend for the services they provide. The PluggableAuthService
is a Zope user folder product that can be extended in modular fashion
using various plugins.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The LDAPMultiPlugins provides PluggableAuthService plugins that use LDAP
as the backend for the services they provide. The PluggableAuthService
is a Zope user folder product that can be extended in modular fashion
using various plugins.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The LDAPMultiPlugins provides PluggableAuthService plugins that use LDAP
as the backend for the services they provide. The PluggableAuthService
is a Zope user folder product that can be extended in modular fashion
using various plugins.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The LDAPMultiPlugins provides PluggableAuthService plugins that use LDAP
as the backend for the services they provide. The PluggableAuthService
is a Zope user folder product that can be extended in modular fashion
using various plugins.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev.git20111218
- Initial build for Sisyphus

