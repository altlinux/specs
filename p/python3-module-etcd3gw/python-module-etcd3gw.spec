%define oname etcd3gw

Name: python3-module-%oname
Version: 0.2.4
Release: alt2
Summary: etcd3 gateway Python Client

Group: Development/Python3
License: ASL 2.0
Url: https://github.com/dims/etcd3-gateway
Source: %oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-urllib3 >= 1.15.1
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-futurist >= 0.11.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx >= 4.7
BuildRequires: python3-module-reno >= 1.8.0

%description
A python client for etcd3 grpc-gateway v3alpha API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Cache storage for Openstack projects
Group: Development/Documentation

%description doc
Documentation for etcd3 gateway Python Client.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html
%doc README.md LICENSE
%doc etcd3gw/examples

%changelog
* Tue Oct 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt2
- Build without python2.

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 0.2.4-alt1
- Initial build
