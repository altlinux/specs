%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-deprecated
%define mod_name flake8_deprecated

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Flake8 plugin that warns about deprecated method calls

License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/flake8-deprecated
Vcs: https://github.com/gforcada/flake8-deprecated

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
%endif
Requires: python3-module-flake8

%description
%summary.

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
%python3_sitelibdir_noarch/%mod_name.py
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}/

%changelog
* Mon Aug 25 2025 Timofei Fedotov <sovtouch@altlinux.org> 2.2.1-alt1
- Initial build for ALT Sisyphus.
