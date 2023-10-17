%define modulename linstor

Name: python3-module-%modulename
Summary: Linstor Python API
Version: 1.20.0
Release: alt1
Group: Development/Python3
License: GPLv3
URL: https://github.com/LINBIT/linstor-api-py
Source: http://www.linbit.com/downloads/linstor/python-%modulename-%version.tar.gz
Patch1: linstor-remove-distutils.patch
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-dev

%description
This library provides functions to access the Linstor controller
e.g.: add nodes, resources and query object status

%prep
%setup -n python-%modulename-%version
%patch1 -p1
make -C linstor-common cleanpython
make -C linstor-common python

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Wed Oct 18 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.20.0-alt1
- 1.20.0
- remove distutils

* Mon Aug 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.19.0-alt1
- 1.19.0
- migrate to pyproject

* Wed May 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.18.0-alt1
- 1.18.0

* Tue Nov 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.15.1-alt1
- 1.15.1

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.10.2-alt1
- 1.10.2

* Sun Nov 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build for ALT
