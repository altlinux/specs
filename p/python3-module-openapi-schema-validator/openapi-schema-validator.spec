%define _unpackaged_files_terminate_build 1
%define pypi_name openapi-schema-validator

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: OpenAPI schema validation
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/openapi-schema-validator
VCS: https://github.com/p1c2u/openapi-schema-validator

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
# direct runtime dependencies
BuildRequires: python3(attrs)
BuildRequires: python3(jsonschema)

# extra
BuildRequires: python3(isodate)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name
Provides: python3-module-openapi_schema_validator = %EVR

%description
Openapi-schema-validator is a Python library that validates schema against:
- OpenAPI Schema Specification v3.0 which is an extended subset of the JSON
  Schema Specification Wright Draft 00.
- OpenAPI Schema Specification v3.1 which is an extended superset of the JSON
  Schema Specification Draft 2020-12.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/openapi_schema_validator/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.4 -> 0.4.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1
- 0.3.0 -> 0.3.4.

* Tue Aug 02 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
