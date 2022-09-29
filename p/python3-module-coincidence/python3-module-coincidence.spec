%define _unpackaged_files_terminate_build 1
%define pypi_name coincidence

# due to circular dependencies
%def_without check

Name: python3-module-%pypi_name
Version: 0.6.3
Release: alt1

Summary: Helper functions for pytest
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/coincidence/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(whey)
BuildRequires: python3(consolekit)
BuildRequires: python3(dist-meta)
BuildRequires: python3(handy-archives)
BuildRequires: python3(pyproject-parser)
BuildRequires: python3(shippinglabel)

%if_with check
BuildRequires: python3(pytest)
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
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.3-alt1
- initial build for Sisyphus

