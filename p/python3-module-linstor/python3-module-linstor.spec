%define modulename linstor

Name: python3-module-%modulename
Summary: Linstor Python API
Version: 1.15.1
Release: alt1
Group: Development/Python3
License: GPLv3
URL: https://github.com/LINBIT/linstor-api-py
Source: http://www.linbit.com/downloads/linstor/python-%modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%description
This library provides functions to access the Linstor controller
e.g.: add nodes, resources and query object status

%prep
%setup -n python-%modulename-%version
make -C linstor-common cleanpython
make -C linstor-common python

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Tue Nov 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.15.1-alt1
- 1.15.1

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.10.2-alt1
- 1.10.2

* Sun Nov 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build for ALT
