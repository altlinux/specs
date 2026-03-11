%define _unpackaged_files_terminate_build 1
%define pypi_name superqt
%define mod_name superqt

Name: python3-module-%pypi_name
Version: 0.7.8
Release: alt1

Summary: Missing widgets and components for Qt-python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/superqt/
Vcs: https://github.com/pyapp-kit/superqt
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%description
This package aims to provide high-quality community-contributed Qt
widgets and components for PyQt & PySide that are not provided in the
native QtWidgets module.

%prep
%setup
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.* LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 10 2026 Aleksandr Dovydenkov <asd@altlinux.org> 0.7.8-alt1
- Initial build for ALT Sisyphus.