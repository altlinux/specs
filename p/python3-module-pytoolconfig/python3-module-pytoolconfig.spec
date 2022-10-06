%define _unpackaged_files_terminate_build 1
%define pypi_name pytoolconfig

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.2
Release: alt1

Summary: Python tool configuration
License: LGPL-3.0
Group: Development/Python3
Vcs: https://github.com/bagel897/pytoolconfig
Url: https://pypi.org/project/pytoolconfig/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(pdm-pep517)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(docutils)
BuildRequires: python3(sphinx)
BuildRequires: python3(tabulate)
BuildRequires: python3(appdirs)
%endif

BuildArch: noarch

%description
The goal of this project is to manage configuration for python tools,
such as black and rope and add support for a pyproject.toml
configuration file.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.2-alt1
- initial build for Sisyphus

