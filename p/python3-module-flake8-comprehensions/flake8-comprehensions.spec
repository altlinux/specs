%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-comprehensions
%define mod_name flake8_comprehensions

%def_with check

Name: python3-module-%pypi_name
Version: 3.16.0
Release: alt1

Summary: A flake8 plugin to help you write better list/set/dict comprehensions

License: MIT
Group: Development/Python3
Url: https://piwheels.org/project/flake8-comprehensions
Vcs: https://github.com/adamchainz/flake8-comprehensions

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest-randomly
BuildRequires: python3-module-pytest-flake8
BuildRequires: python3-module-pytest-flake8-path
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
%python3_sitelibdir_noarch/%mod_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}/

%changelog
* Mon Aug 25 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.16.0-alt1
- Initial build for ALT Sisyphus.
