%define _unpackaged_files_terminate_build 1
%define pypi_name sdjson

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Custom JSON Encoder for Python utilising functools.singledispatch to support custom encoders for both Python's built-in classes and user-created classes, without as much legwork
License: MIT
Group: Development/Python3
Url: https://pypi.org/projects/sdjson/

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
BuildRequires: python3(pytz)
%endif

BuildArch: noarch

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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- 0.3.1 -> 0.4.0
- use python3(whey) to build the package
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus

