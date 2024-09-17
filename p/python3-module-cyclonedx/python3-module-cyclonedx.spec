%define pypi_name cyclonedx-python-lib

Name: python3-module-cyclonedx
Version: 7.6.0
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
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

Requires: python3-module-referencing python3-module-jsonschema

%description
OWASP CycloneDX is a full-stack Bill of Materials (BOM) standard that provides
advanced supply chain capabilities for cyber risk reduction.

This Python package provides data models, validators and more, to help you
create/render/read CycloneDX documents.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 7.6.0-alt1
- Initial build for Sisyphus.
