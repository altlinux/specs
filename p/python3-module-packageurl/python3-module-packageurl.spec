%define _unpackaged_files_terminate_build 1
%define pypi_name packageurl-python

%def_with check

Name: python3-module-packageurl
Version: 0.16.0
Release: alt1
Summary: Python implementation of the package url spec
License: MIT
Group: Development/Python3
Url: https://github.com/package-url/packageurl-python

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Provides: python3-module-%pypi_name = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
Python library to parse and build "purl" aka. Package URLs.

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
%python3_sitelibdir/*

%changelog
* Mon Nov 11 2024 Andrey Kovalev <ded@altlinux.org> 0.16.0-alt1
- Updated to upstream version 0.16.0.
- Terminate build if unpackaged files were found.
- Added %%check section that runs test suite by default.

* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 0.15.6-alt1
- Initial build for Sisyphus.
