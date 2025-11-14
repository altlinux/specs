%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-isort
%define mod_name flake8_isort

%def_with check

Name: python3-module-%pypi_name
Version: 7.0.0
Release: alt1

Summary: Flake8 plugin that integrates isort

License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/flake8-isort
Vcs: https://github.com/gforcada/flake8-isort

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-isort
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest run_tests.py

%files
%doc LICENSE README.rst
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Fri Nov 14 2025 Timofei Fedotov <sovtouch@altlinux.org> 7.0.0-alt1
- Updated to 7.0.0.

* Thu Apr 19 2025 Timofei Fedotov <sovtouch@altlinux.org> 6.1.2-alt1
- Initial build for ALT Sisyphus.
