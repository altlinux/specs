%define _unpackaged_files_terminate_build 1
%define pypi_name coverage-pyver-pragma

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: Plugin for Coverage.py to selectively ignore branches depending on the Python version
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/coverage-pyver-pragma/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(coverage)
BuildRequires: python3(coincidence)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(domdf-python-tools)
BuildRequires: python3(packaging)
BuildRequires: python3(pyparsing)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/coverage_pyver_pragma/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus

