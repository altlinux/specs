%define _unpackaged_files_terminate_build 1
%define pypi_name deprecation-alias

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt2

Summary: A wrapper around 'deprecation' providing support for deprecated aliases
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/deprecation-alias/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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
BuildRequires: python3(deprecation)
BuildRequires: python3(packaging)
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
%python3_sitelibdir/deprecation_alias/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt2
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus

