Name:           python-module-influxdb
License:        MIT
Group:          Development/Python
Summary:        Python client for InfluxDB 
Version:        5.0.0
Release:        alt1
URL:            https://github.com/influxdata/influxdb-python
Source:         %name-%version.tar
BuildArch:      noarch
BuildRequires:  python-module-setuptools

%description
InfluxDB-Python is a client for interacting with InfluxDB

%prep
%setup

%build
%python_build

%install
%python_install

%files
%{python_sitelibdir}/*
%doc docs/source examples README.rst

%changelog
* Sat Mar 17 2018 Terechkov Evgenii <evg@altlinux.org> 5.0.0-alt1
- 5.0.0

* Sun Oct 22 2017 Terechkov Evgenii <evg@altlinux.org> 4.1.1-alt1
- Initial build for ALT Linux Sisyphus
