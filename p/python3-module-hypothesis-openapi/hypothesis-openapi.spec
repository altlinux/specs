%define _unpackaged_files_terminate_build 1
%define pypi_name hypothesis-openapi
%define mod_name hypothesis_openapi

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Hypothesis plugin for generating valid Open API documents
License: MIT
Group: Development/Python3
Url: https://github.com/Stranger6667/hypothesis-openapi
VCS: https://github.com/Stranger6667/hypothesis-openapi.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
Hypothesis plugin for generating valid Open API documents.

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
%doc LICENSE README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.3.0-alt1
- New version (0.3.0).
- Updated dependencies management.

* Thu Oct 03 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.2.1-alt1
  - Initial build for ALT.
