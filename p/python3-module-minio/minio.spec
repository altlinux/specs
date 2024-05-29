%define _unpackaged_files_terminate_build 1
%define pypi_name minio

%def_with check

Name: python3-module-%pypi_name
Version: 7.2.7
Release: alt1

Summary: MinIO Client SDK for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/minio/
Vcs: https://github.com/minio/minio-py

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-pytest
%pyproject_builddeps_metadata
%endif

%description
The MinIO Python Client SDK provides high level APIs to access any MinIO
Object Storage or other Amazon S3 compatible service.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.* docs/API.md examples
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 7.2.7-alt1
- Initial build for ALT Sisyphus.

