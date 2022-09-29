%define _unpackaged_files_terminate_build 1
%define pypi_name consolekit

# due to circular dependency
%def_without check

Name: python3-module-%pypi_name
Version: 1.4.1
Release: alt1

Summary: Additional utilities for click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/consolekit/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(flit)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(click)
BuildRequires: python3(colorama)
BuildRequires: python3(deprecation-alias)
BuildRequires: python3(domdf-python-tools)
BuildRequires: python3(mistletoe)
BuildRequires: python3(typing_extensions)
%endif

BuildArch: noarch

%filter_from_requires /python3(coincidence.*)/d

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
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- initial build for Sisyphus (temporary broken)

