%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-logging
%define mod_name flake8_logging

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1

Summary: A Flake8 plugin that checks for issues using the standard library logging module

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/flake8-logging
Vcs: https://github.com/adamchainz/flake8-logging

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Fri Nov 14 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.8.0-alt1
- Initial build for ALT Sisyphus.
