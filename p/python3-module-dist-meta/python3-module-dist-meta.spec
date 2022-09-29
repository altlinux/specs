%define _unpackaged_files_terminate_build 1
%define pypi_name dist-meta

# due to circular dependency
%def_without check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: Parse and create Python distribution metadata
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dist-meta/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
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
%python3_sitelibdir/dist_meta/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.0-alt1
- initial build for Sisyphus

