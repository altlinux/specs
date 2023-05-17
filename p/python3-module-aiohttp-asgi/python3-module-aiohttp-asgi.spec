%define _unpackaged_files_terminate_build 1
%define pypi_name aiohttp-asgi
%define mod_name aiohttp_asgi

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: Run ASGI application with aiohttp
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiohttp-asgi/
Vcs: https://github.com/mosquito/aiohttp-asgi

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter coveralls
%add_pyproject_deps_check_filter pylava
%add_pyproject_deps_check_filter types-
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This module provides a way to use any ASGI compatible frameworks
and aiohttp together.

%prep
%setup
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
%pyproject_run_pytest -vra

%files
%doc LICENSE.md README.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.5.2-alt1
- Initial build for ALT Sisyphus.

