%define _unpackaged_files_terminate_build 1
%define pypi_name xdg-base-dirs
%define mod_name xdg_base_dirs

%def_with check

Name: python3-module-%pypi_name
Version: 6.0.2
Release: alt1

Summary: Paths to the directories defined by the XDG Base Directory Specification
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/xdg-base-dirs/
Vcs: https://github.com/srstevenson/xdg-base-dirs
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-poetry

%description
xdg-base-dirs is a Python module that provides functions to return paths
to the directories defined by the XDG Base Directory Specification, to
save you from duplicating the same snippet of logic in every Python
utility you write that deals with user cache, configuration, or data
files. It has no external dependencies and consists of a single file,
making it easy to integrate.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vca

%files
%doc README.md LICENSE
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Mar 20 2026 Andrey Kuzma <kuzmaav@altlinux.org> 6.0.2-alt1
- Initial build for Sisyphus.
