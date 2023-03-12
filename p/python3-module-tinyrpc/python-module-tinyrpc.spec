%define oname tinyrpc

Name: python3-module-%oname
Version: 1.1.6
Release: alt1

Summary: Modular RPC library

License: MIT
Group: Development/Python
Url: http://github.com/mbr/tinyrpc

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch1: tinyrpc-0.9.3-python3.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
tinyrpc is a library for making and handling RPC calls in python.
Its initial scope is handling jsonrpc,
although it aims to be very well-documented and modular
to make it easy to add support for further protocols.

A feature is support of multiple transports (or none at all)
and providing clever syntactic sugar for writing dispatchers.

%prep
%setup
#patch1 -p1
find tinyrpc -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove bundled egg-info
rm -rfv %oname.egg-info

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- new version 1.1.6 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- new version 1.1.4 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt2
- build python3 package separately

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.3-alt1
- 0.9.3
- build python3 package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt2
- fix permitions inside egg-info dir

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5-alt1
- Initial package.
