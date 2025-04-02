%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name caio
%define module_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.9.21
Release: alt1

Summary: Linux AIO c python bindings
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/caio/
Vcs: https://github.com/mosquito/caio

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra develop
%endif

%description
Python bindings for Linux AIO API and simple asyncio wrapper.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.9.21-alt1
- Initial build for ALT Sisyphus.

