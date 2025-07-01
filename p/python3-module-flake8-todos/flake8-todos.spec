%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-todos
%define mod_name flake8_todos

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: Lint TODO comments in a Python code

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/flake8-todos/
Vcs: https://github.com/orsinium-labs/flake8-todos

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
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
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Thu Apr 19 2025 Timofei Fedotov <sovtouch@altlinux.org> 0.3.1-alt1
- Initial build for ALT Sisyphus.
