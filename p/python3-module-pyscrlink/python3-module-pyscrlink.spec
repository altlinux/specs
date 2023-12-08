%define pypi_name pyscrlink

%def_without check

Name:    python3-module-%pypi_name
Version: 0.2.8
Release: alt1

Summary: Scratch-link for Linux written in python
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/kawasaki/pyscrlink

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Pyscrlink is a Scratch-link for Linux. Scratch-link is a software module which
connects Scratch to Bluetooth devices such as micro:bit.

%package -n %pypi_name
Summary: Scratch-link for Linux written in python
Group: Development/Python3

%description -n %pypi_name
Pyscrlink is a Scratch-link for Linux. Scratch-link is a software module which
connects Scratch to Bluetooth devices such as micro:bit.

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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %pypi_name
%doc README.md
%_bindir/*

%changelog
* Thu Dec 07 2023 Andrey Cherepanov <cas@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus.
