%define _unpackaged_files_terminate_build 1
%define pypi_name pytweening

Name: python3-module-%pypi_name
# Due to upstream doesn't make tags we need to pull version
# from pytweening/__init__.py (based on setup.py version discovery).
Version: 1.2.0
Release: alt1
Summary: A set of tweening / easing functions implemented in Python. 
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pytweening/
Vcs: https://github.com/asweigart/pytweening
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
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
#imposible run tests witout graphical interface
#pyproject_run_pytest

%files
%doc README.md LICENSE* 
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 1.2.0-alt1
- initial build for Sisyphus

