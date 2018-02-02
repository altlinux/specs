
%def_with python3
%def_disable check

Name: python-module-ldappool
Version: 2.0.0
Release: alt1.1
Summary: A connection pool for python-ldap
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ldappool/

# https://git.openstack.org/openstack/ldappool
Source: %name-%version.tar
BuildArch: noarch

Requires: python-module-pyldap

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pyldap python-module-pbr
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-ldap python3-module-pbr
%endif

%py_provides ldappool

%description
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

%package tests
Summary: Tests for ldappool
Group: Development/Python
Requires: %name = %EVR

%description tests
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

This package contains tests for ldappool.

%if_with python3
%package -n python3-module-ldappool
Summary: A connection pool for python-ldap
Group: Development/Python3
%py3_provides ldappool

Requires: python3-module-pyldap

%description -n python3-module-ldappool
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

%package -n python3-module-ldappool-tests
Summary: Tests for ldappool
Group: Development/Python3
Requires: python3-module-ldappool = %EVR

%description -n python3-module-ldappool-tests
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

This package contains tests for ldappool.
%endif

%prep
%setup -q

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
rm -fR build
py.test
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc CONTRIBUTORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-ldappool
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-ldappool-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.git20130422
- Fixed build

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20130422
- Initial build for Sisyphus

