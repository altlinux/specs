%define _unpackaged_files_terminate_build 1
%define pypi_name openapi-spec-validator

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 spec validator
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/openapi-spec-validator
VCS: https://github.com/p1c2u/openapi-spec-validator

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
# direct runtime dependencies
BuildRequires: python3(jsonschema)
BuildRequires: python3(openapi-schema-validator)
BuildRequires: python3(importlib-resources)
BuildRequires: python3(jsonschema-spec)
BuildRequires: python3(lazy-object-proxy)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

# PyPI name
%py3_provides %pypi_name
Provides: python3-module-openapi_spec_validator = %EVR

%description
OpenAPI Spec Validator is a Python library that validates OpenAPI Specs against
the OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 specification. The validator aims
to check for full compliance with the Specification.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -m 'not network'

%files
%doc README.rst
%_bindir/openapi-spec-validator
%python3_sitelibdir/openapi_spec_validator/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.5.1 -> 0.5.2.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.4.0 -> 0.5.1.

* Tue Aug 02 2022 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
