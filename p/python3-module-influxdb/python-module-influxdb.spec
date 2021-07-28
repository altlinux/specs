%define oname influxdb

Name: python3-module-%oname
Version: 5.2.2
Release: alt3

Summary: Python client for InfluxDB

License: MIT
Group: Development/Python3
Url: https://github.com/influxdata/influxdb-python

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
InfluxDB-Python is a client for interacting with InfluxDB.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc docs/source examples README.rst
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 5.2.2-alt3
- Rename package, spec cleanup.

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.2-alt2
- rebuild without python2 subpackage

* Thu Mar 21 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.2-alt1
- 5.2.2
- add python3 package

* Sat Mar 17 2018 Terechkov Evgenii <evg@altlinux.org> 5.0.0-alt1
- 5.0.0

* Sun Oct 22 2017 Terechkov Evgenii <evg@altlinux.org> 4.1.1-alt1
- Initial build for ALT Linux Sisyphus
