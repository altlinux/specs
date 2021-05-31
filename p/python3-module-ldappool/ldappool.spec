%define oname ldappool

%def_disable check

Name: python3-module-%oname
Version: 2.0.0
Release: alt2
Summary: A connection pool for python-ldap
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/ldappool/

# https://git.openstack.org/openstack/ldappool
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-ldap python3-module-pbr

Requires: python3-module-pyldap
%py3_provides ldappool

%description
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

%package tests
Summary: Tests for ldappool
Group: Development/Python3
Requires: %name = %EVR

%description tests
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

This package contains tests for ldappool.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
rm -fR build
py.test-%_python3_version

%files
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.git20130422
- Fixed build

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20130422
- Initial build for Sisyphus

