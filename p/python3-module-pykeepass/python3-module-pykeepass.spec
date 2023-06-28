%define pypi_name pykeepass

%def_disable check

Name: python3-module-%pypi_name
Version: 4.0.5
Release: alt1

Summary: Python library to interact with KeePass databases
Group: Development/Python3
License: GPL-3.0
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/libkeepass/pykeepass.git
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
Python library to interact with KeePass databases.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* CHANGELOG*


%changelog
* Fri Jun 23 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0.5-alt1
- first build for Sisyphus



