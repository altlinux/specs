%define _unpackaged_files_terminate_build 1
%define pypi_name openapi-schema-validator
%define mod_name openapi_schema_validator

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: OpenAPI schema validation
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/openapi-schema-validator
VCS: https://github.com/p1c2u/openapi-schema-validator
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not yet packaged
%add_pyproject_deps_check_filter tbump
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Openapi-schema-validator is a Python library that validates schema against:
- OpenAPI Schema Specification v3.0 which is an extended subset of the JSON
  Schema Specification Wright Draft 00.
- OpenAPI Schema Specification v3.1 which is an extended superset of the JSON
  Schema Specification Draft 2020-12.
- OpenAPI Schema Specification v3.2 using the published OAS 3.2 JSON Schema
  dialect resources.

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -vra -o=addopts=''

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 14 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.9.0-alt1
- NMU: New version 0.9.0.
- Updated dependency management.

* Mon Jan 13 2025 Anton Vyatkin <toni@altlinux.org> 0.6.3-alt1
- New version 0.6.3.

* Wed Nov 15 2023 Anton Vyatkin <toni@altlinux.org> 0.6.2-alt1.1
- Fixed FTBFS.

* Fri Oct 06 2023 Anton Vyatkin <toni@altlinux.org> 0.6.2-alt1
- New version 0.6.2.

* Thu Sep 21 2023 Anton Vyatkin <toni@altlinux.org> 0.6.1-alt1
- New version 0.6.1.

* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Wed Jan 25 2023 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1.

* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.4 -> 0.4.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1
- 0.3.0 -> 0.3.4.

* Tue Aug 02 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
