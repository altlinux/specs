%define _unpackaged_files_terminate_build 1
%define module_name simple-term-menu
%define pypi_name simple_term_menu

Name: python3-module-%module_name
Version: 1.6.1
Release: alt1
Summary: A Python package which creates simple interactive menus on the command line
License: MIT
Group: Development/Python3
Url: https://github.com/IngoMeyer441/simple-term-menu
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%module_name
%python3_sitelibdir/%{pypi_name}.py
%python3_sitelibdir/__pycache__/%{pypi_name}*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 27 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.1-alt1
- Initial build for ALT

