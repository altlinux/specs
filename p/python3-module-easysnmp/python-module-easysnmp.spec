%define oname easysnmp

%def_without tests

Name: python3-module-%oname
Version: 0.2.5
Release: alt3

Summary: Easy SNMP is a fork of the official Net-SNMP Python Bindings
Url: https://github.com/kamakazikamikaze/easysnmp
Source: %oname-%version.tar.gz
License: BSD
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: libnet-snmp-devel


%description
A blazingly fast and Pythonic SNMP library based on the official Net-SNMP bindings

%package -n tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
export LANG=en_US.UTF-8
%python3_build

%install
export LANG=en_US.UTF-8
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*
#%exclude %python_sitelibdir/*/tests

%if_with tests
%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt3
- disable python2

* Tue Apr 02 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt2
- Rebuild without %%ubt macro.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.5-alt1.S1.2
- NMU: updated build dependencies.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.5-alt1.S1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1.S1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 02 2017 Alexey Shabalin <shaba@altlinux.ru> 0.2.5-alt1.S1
- initial build

