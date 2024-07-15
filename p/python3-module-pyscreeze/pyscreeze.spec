%define _unpackaged_files_terminate_build 1
%define modulename pyscreeze
%define pypi_name PyScreeze

%def_with check

Name: python3-module-%modulename
# Due to upstream doesn't make tags we need to pull version
# from pyscreeze/__init__.py (based on setup.py version discovery)
Version: 0.1.30
Release: alt1
Summary: PyScreeze is a simple, cross-platform screenshot module for Python 3. 
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/PyScreeze/
Vcs: https://github.com/asweigart/pyscreeze
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
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Apr 16 2024 Pavel Shilov <zerospirit@altlinux.org> 0.1.30-alt1
- initial build for Sisyphus

