%define _unpackaged_files_terminate_build 1
%define pypi_name cyclonedx-python-lib

%def_with check

Name: python3-module-cyclonedx
Version: 9.1.0
Release: alt1
Summary: Python implementation of OWASP CycloneDX
License: Apache-2.0
Group: Development/Python3
Url: https://cyclonedx.org
VCS: https://github.com/CycloneDX/cyclonedx-python-lib.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Provides: python3-module-%pypi_name = %EVR

%pyproject_runtimedeps_metadata
%pyproject_runtimedeps_metadata_extra validation

BuildRequires(pre): rpm-build-pyproject

%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter pep8-naming
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
OWASP CycloneDX is a full-stack Bill of Materials (BOM) standard that provides
advanced supply chain capabilities for cyber risk reduction.

This Python package provides data models, validators and more, to help you
create/render/read CycloneDX documents.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%python3_sitelibdir/*

%changelog
* Wed Mar 05 2025 Andrey Kovalev <ded@altlinux.org> 9.1.0-alt1
- Updated to upstream version 9.1.0.

* Wed Jan 15 2025 Andrey Kovalev <ded@altlinux.org> 8.5.0-alt1
- Updated to upstream version 8.5.0.
- Terminate build if unpackaged files were found.
- Added %%check section that runs test suite by default.

* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 7.6.0-alt1
- Initial build for Sisyphus.
