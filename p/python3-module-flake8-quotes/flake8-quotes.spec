%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-quotes
%define mod_name flake8_quotes

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.0
Release: alt1

BuildArch: noarch
Summary: Flake8 extension for checking quotes in python

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/flake8-quotes/
Vcs: https://github.com/zheller/flake8-quotes

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
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
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Thu Apr 19 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.4.0-alt1
- Initial build for ALT Sisyphus
