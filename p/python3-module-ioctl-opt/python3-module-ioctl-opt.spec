%define pypi_name ioctl-opt

%def_without check

Name:    python3-module-%pypi_name
Version: 1.3.1
Release: alt1

Summary: Pythonified linux asm-generic/ioctl.h
License: LGPL-2.1
Group:   Development/Python3
URL:     https://github.com/vpelletier/python-ioctl-opt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst COPYING COPYING.LESSER
%python3_sitelibdir/ioctl_opt
%python3_sitelibdir/ioctl_opt-1.3.1.dist-info

%changelog
* Tue Aug 18 2026 Artyom Bystrov <arbars@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
