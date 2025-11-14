%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-flake8-path
%define mod_name pytest_flake8_path

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt1
BuildArch: noarch

Summary: A pytest fixture for testing flake8 plugins
License: MIT
Group: Development/Python3
Url: https://piwheels.org/project/pytest-flake8-path/
Vcs: https://github.com/adamchainz/pytest-flake8-path

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-flake8
%pyproject_builddeps_check
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
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Fri Nov 14 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.7.0-alt1
- Updated to 1.7.0.

* Tue Aug 26 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.6.0-alt1
- Initial build for ALT Sisyphus.
