%define _unpackaged_files_terminate_build 1
%define pypi_name harfile

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt2

Summary: This package provides zero dependency writer for building HAR (HTTP Archive) files in Python
License: MIT
Group: Development/Python3
Url: https://github.com/schemathesis/harfile
Vcs: https://github.com/schemathesis/harfile.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
This package provides zero dependency writer for building
HAR (HTTP Archive) files in Python.

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
%doc LICENSE README.*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 24 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.5.0-alt2
- Dropped the dependency on hypothesis-jsonschema.

* Wed Jun 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.5.0-alt1
- New version (0.5.0).

* Mon Oct 06 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.4.0-alt1
- New version (0.4.0).

* Thu Sep 04 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.3.1-alt1
- New version (0.3.1).
- Updated dependencies managment.

* Mon Sep 30 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.3.0-alt1
  - Initial build for ALT.
