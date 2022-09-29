%define _unpackaged_files_terminate_build 1
%define pypi_name domdf-python-tools

# circular dependecy on coindicence
%def_without check

Name: python3-module-%pypi_name
Version: 3.4.0
Release: alt1

Summary: Helpful functions for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/domdf-python-tools/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(natsort)
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
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/domdf_python_tools/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 3.4.0-alt1
- initial build for Sisyphus

