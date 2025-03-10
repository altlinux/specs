%define pypi_name vulkan

%def_without check

Name:    python3-module-%pypi_name
Version: 1.3.275.1
Release: alt1

Summary: The ultimate Python binding for Vulkan API
License: Apache-2.0
Group:   Development/Python3
Url:     https://pypi.org/project/vulkan/
Vcs:     https://github.com/realitix/vulkan

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-cffi
Requires: vulkan

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}


%changelog
* Thu Jan 30 2025 Sergey Palcheh <minergenon@altlinux.org> 1.3.275.1-alt1
- Initial build for Sisyphus
