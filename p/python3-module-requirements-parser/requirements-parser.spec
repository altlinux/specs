%define _unpackaged_files_terminate_build 1
%define pypi_name requirements-parser
%define mod_name requirements

%def_with check

Name: python3-module-%pypi_name
Version: 0.13.0
Release: alt1

Summary: A Pip requirements file parser

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/requirements-parser
Vcs: https://github.com/madpah/requirements-parser

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

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
%python3_sitelibdir/%mod_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 16 2025 Timofei Fedotov <sovtouch@altlinux.org> 0.13.0-alt1
- Initial build for ALT Sisyphus.
