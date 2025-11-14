%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-tidy-imports
%define mod_name flake8_tidy_imports

%def_with check

Name: python3-module-%pypi_name
Version: 4.12.0
Release: alt1

Summary: A flake8 plugin that helps you write tidier imports

License: LGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/flake8-tidy-imports
Vcs: https://github.com/adamchainz/flake8-tidy-imports

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-flake8
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
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}/

%changelog
* Fri Nov 14 2025 Timofei Fedotov <sovtouch@altlinux.org> 4.12.0-alt1
- Initial build for ALT Sisyphus.
