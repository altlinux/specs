%define _unpackaged_files_terminate_build 1
%define pypi_name whatthepatch

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.3
Release: alt1

Summary: What The Patch!? -- A Python patch parsing library  
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/whatthepatch/

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
What The Patch!? is a library for both parsing and applying patch files.

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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jan 19 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.3-alt1
- 1.0.3

* Tue Oct 04 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.2-alt1
- initial build for Sisyphus

