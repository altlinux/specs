%define _unpackaged_files_terminate_build 1

%define pypi_name cpylog

%def_without check

Name: python3-module-%pypi_name
Version: 1.6.1
Release: alt1.git20260414.b8e3516

Summary: Simple pure python colorama/HTML capable logger
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/SteveDoyle2/cpylog

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A simple pure python colorama/HTML capable logger.

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
%doc LICENSE.txt README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 19 2026 Nikolay Strelkov <snk@altlinux.org> 1.6.1-alt1.git20260414.b8e3516
- Initial build for Sisyphus
