%define oname influxdb

Name: python-module-%oname
License: MIT
Group: Development/Python
Summary: Python client for InfluxDB
Version: 5.2.2
Release: alt1
Url: https://github.com/influxdata/influxdb-python
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
InfluxDB-Python is a client for interacting with InfluxDB.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: python-module-%oname = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Code checking using pep8 and pyflakes
Group: Development/Python3

%description -n python3-module-%oname
InfluxDB-Python is a client for interacting with InfluxDB.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup

%build
%python_build -b build2
%python3_build -b build3

%install
ln -sf build2 build
%python_install
ln -sf build3 build
%python3_install

%files
%python_sitelibdir/*
%doc docs/source examples README.rst
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%doc docs/source examples README.rst
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Mar 21 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.2-alt1
- 5.2.2
- add python3 package

* Sat Mar 17 2018 Terechkov Evgenii <evg@altlinux.org> 5.0.0-alt1
- 5.0.0

* Sun Oct 22 2017 Terechkov Evgenii <evg@altlinux.org> 4.1.1-alt1
- Initial build for ALT Linux Sisyphus
