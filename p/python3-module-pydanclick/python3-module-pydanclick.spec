%define _unpackaged_files_terminate_build 1
%define pypi_name pydanclick

%def_with check

Name: python3-module-pydanclick
Version: 0.5.0
Release: alt1
Summary: Add click options from a Pydantic model
License: MIT
Group: Development/Python3
Url: https://github.com/felix-martel/pydanclick
VCS: https://github.com/felix-martel/pydanclick.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-%release.patch

%pyproject_runtimedeps_metadata
%pyproject_runtimedeps_metadata_extra griffe

BuildRequires(pre): rpm-build-pyproject

%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter typing_extensions
%add_pyproject_deps_check_filter deptry
%add_pyproject_deps_check_filter griffe2md
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra griffe
%pyproject_builddeps_check
%endif

%description
Use Pydantic models as Click options.

%prep
%setup
%patch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/*

%changelog
* Tue Feb 25 2025 Andrey Kovalev <ded@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
