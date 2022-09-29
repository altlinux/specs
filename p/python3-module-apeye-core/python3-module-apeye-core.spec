%define _unpackaged_files_terminate_build 1
%define pypi_name apeye-core

# due to circular dependency
%def_without check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Core (offline) functionality for the apeye library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/apeye-core/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(flit)

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
%python3_sitelibdir/apeye_core/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

