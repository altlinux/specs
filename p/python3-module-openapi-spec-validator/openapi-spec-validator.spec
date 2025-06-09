%define _unpackaged_files_terminate_build 1
%define pypi_name openapi-spec-validator

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.2
Release: alt1
Summary: OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 spec validator
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/openapi-spec-validator
VCS: https://github.com/p1c2u/openapi-spec-validator
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# PyPI name
%py3_provides %pypi_name
Provides: python3-module-openapi_spec_validator = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter bump2version
%add_pyproject_deps_check_filter deptry
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
OpenAPI Spec Validator is a Python library that validates OpenAPI Specs against
the OpenAPI 2.0 (aka Swagger) and OpenAPI 3.0 specification. The validator aims
to check for full compliance with the Specification.

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
%pyproject_run_pytest -vra -m 'not network' -o=addopts=''

%files
%doc README.rst
%_bindir/openapi-spec-validator
%python3_sitelibdir/openapi_spec_validator/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 09 2025 Stanislav Levin <slev@altlinux.org> 0.7.2-alt1
- 0.7.1 -> 0.7.2.

* Mon May 19 2025 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- NMU: fixed FTBFS (removed jsonschema-spec).

* Sat Oct 14 2023 Anton Vyatkin <toni@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Wed Oct 11 2023 Anton Vyatkin <toni@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Fri Jul 14 2023 Anton Vyatkin <toni@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.5.1 -> 0.5.2.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.4.0 -> 0.5.1.

* Tue Aug 02 2022 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
