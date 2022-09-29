%define _unpackaged_files_terminate_build 1
%define pypi_name tox-pip-version

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.7
Release: alt1

Summary: A tox plugin to select your pip version
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-pip-version/

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
%doc LICENSE README.md
%python3_sitelibdir/tox_pip_version/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.7-alt1
- initial build for Sisyphus

