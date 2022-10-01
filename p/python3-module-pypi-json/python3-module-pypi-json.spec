%define _unpackaged_files_terminate_build 1
%define pypi_name pypi-json

# tests require the Internet connection
%def_without check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: PyPI JSON API client library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pypi-json/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(coverage)
BuildRequires: python3(coverage-pyver-pragma)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(coincidence)
BuildRequires: python3(packaging)
BuildRequires: python3(apeye)
BuildRequires: python3(betamax)
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
%python3_sitelibdir/pypi_json/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- initial build for Sisyphus

