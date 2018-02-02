%def_with python3

%define oname pyroute2

Name: python-module-%oname
Version: 0.4.15
Release: alt1.1
Summary: Python Netlink library
Group: Development/Python
License: GPLv2+, ASL 2.0
Url: http://github.com/mbr/tinyrpc
Source: %oname-%version.tar.gz
BuildArch: noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
Pyroute2 is a pure Python netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Netlink library
Group: Development/Python3

%description -n python3-module-%oname
Pyroute2 is a pure Python netlink library.
It requires only Python stdlib, no 3rd party libraries.
The library was started as an RTNL protocol implementation,
so the name is pyroute2, but now it supports many netlink protocols.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Python Netlink library
Group: Development/Documentation

%description doc
Documentation for Python Netlink library.


%prep
%setup -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
# install tests
cp -pr tests %buildroot%python_sitelibdir/%oname/
%if_with python3
pushd ../python3
%python3_install
cp -pr tests %buildroot%python3_sitelibdir/%oname/
popd
%endif

%files
%doc README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc docs/html examples

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.15-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.15-alt1
- Initial package.
