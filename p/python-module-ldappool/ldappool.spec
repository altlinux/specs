%define oname ldappool

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.1
Release: alt1.git20130422
Summary: A connection pool for python-ldap
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ldappool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/ldappool.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-ldap python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-ldap python3-module-py
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A connection pool for python-ldap
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The pool keeps LDAP connectors alive and let you reuse them, drastically
reducing the time spent to initiate a ldap connection.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%files -n python3-module-%oname
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20130422
- Initial build for Sisyphus

