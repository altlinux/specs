%define oname easysnmp

%def_with python3
%def_without tests

Summary: Easy SNMP is a fork of the official Net-SNMP Python Bindings
Name: python-module-%oname
Version: 0.2.5
Release: alt1%ubt.1
Url: https://github.com/kamakazikamikaze/easysnmp
Source: %oname-%version.tar.gz
License: BSD
Group: Development/Python

BuildPreReq: rpm-build-ubt
BuildRequires: python-devel python-module-setuptools
BuildRequires: libnet-snmp-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
A blazingly fast and Pythonic SNMP library based on the official Net-SNMP bindings

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Easy SNMP is a fork of the official Net-SNMP Python Bindings
Group: Development/Python3

%description -n python3-module-%oname
A blazingly fast and Pythonic SNMP library based on the official Net-SNMP bindings

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version
%if_with python3
cp -fR . ../python3
%endif

%build
export LANG=en_US.UTF-8
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LANG=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc README.rst
%python_sitelibdir/*
#%exclude %python_sitelibdir/*/tests

%if_with tests
%files tests
%python_sitelibdir/*/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
#%exclude %python3_sitelibdir/*/tests

%if_with tests
%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1%ubt.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 02 2017 Alexey Shabalin <shaba@altlinux.ru> 0.2.5-alt1%ubt
- initial build

