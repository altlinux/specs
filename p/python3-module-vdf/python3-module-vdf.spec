%define pypi_name vdf

%def_without check

Name:    python3-module-%pypi_name
Version: 3.4.1
Release: alt1

Summary: Package for working with Valve's text and binary KeyValue format
License: MIT
Group:   Development/Python3
URL:     https://github.com/ValvePython/vdf

Packager: Artyom Bystrov <arbars@altlinux.org>

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
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/vdf-3.4.dist-info

%changelog
* Sun Jul 02 2023 Artyom Bystrov <arbars@altlinux.org> 3.4.1-alt1
- New version 3.4.1.

* Sun Jul 02 2023 Artyom Bystrov <arbars@altlinux.org> 3.4-alt1
- Initial build for Sisyphus
