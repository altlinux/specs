%define _unpackaged_files_terminate_build 1
%define pypi_name docstring-parser
%define module_name docstring_parser
%def_with check

Name: python3-module-%pypi_name
Version: 0.16
Release: alt1

Summary: Parse Python docstrings in various flavors
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/docstring_parser/
Vcs: https://github.com/rr-/docstring_parser
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-%release.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Parse Python docstrings. Currently support ReST, Google, Numpydoc-style
and Epydoc docstrings.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 01 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.16-alt1
- Initial build for ALT Sisyphus.

