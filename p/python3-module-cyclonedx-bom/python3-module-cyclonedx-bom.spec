%define _unpackaged_files_terminate_build 1
%define pypi_name cyclonedx-bom
%define module_name cyclonedx_py

Name: python3-module-%pypi_name
Version: 7.3.0
Release: alt1

Summary: CycloneDX Python SBOM Generation Tool
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/cyclonedx-bom/
VCS: https://github.com/CycloneDX/cyclonedx-python

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
This tool generates Software Bill of material (SBOM) documents
in OWASP CycloneDX format. This is probably the most accurate,
complete SBOM generator for any python-related projects.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%_bindir/cyclonedx-py
%python3_sitelibdir_noarch/%module_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 31 2026 Denis Rastyogin <gerben@altlinux.org> 7.3.0-alt1
- Initial build for ALT Sisyphus.
