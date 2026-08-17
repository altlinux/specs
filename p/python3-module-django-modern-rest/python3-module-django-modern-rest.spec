%define _unpackaged_files_terminate_build 1
%define pypi_name django-modern-rest
%define mod_name dmr
%define dmr_pytest_name dmr_pytest

%def_with check

Name: python3-module-%pypi_name
Version: 0.14.0
Release: alt1
Summary: Modern REST framework for Django with types and async support
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/django-modern-rest/
VCS: https://github.com/wemake-services/django-modern-rest.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3

%add_pyproject_deps_check_filter codespell
%add_pyproject_deps_check_filter import-linter
%add_pyproject_deps_check_filter pyrefly
%add_pyproject_deps_check_filter pytest-custom-exit-code
%add_pyproject_deps_check_filter slotscheck
%add_pyproject_deps_check_filter wemake-python-styleguide
#not packaged in Sisyphus
%add_pyproject_deps_check_filter xmltodict-rs

%pyproject_builddeps_metadata_extra jwt
%pyproject_builddeps_metadata_extra msgspec
%pyproject_builddeps_metadata_extra openapi
%pyproject_builddeps_metadata_extra pydantic
# extra for pydantic
BuildRequires: python3-module-email-validator
%pyproject_builddeps_check
%endif

%description
Django Modern REST is a typed framework for building synchronous and
asynchronous REST APIs with Django. It provides request and response
validation, pluggable serializers, authentication, content negotiation,
and OpenAPI schema generation.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup unit-test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# xmltodict-rs is not packaged in Sisyphus; skip tests that import it.
%pyproject_run_pytest -o addopts="-vra" -o filterwarnings=ignore::DeprecationWarning \
  --ignore=tests/test_unit/test_metadata/test_unsupported_serializer.py \
  --ignore=tests/test_unit/test_negotiation/test_breaking_contract.py \
  --ignore=tests/test_unit/test_negotiation/test_global_configuration.py \
  --ignore=tests/test_unit/test_openapi/test_schema_snapshots.py \
  --ignore=tests/test_unit/test_plugins/test_pydantic/test_pydantic_fast.py \
  --ignore=tests/test_unit/test_routing/test_not_found_handler.py \
  --ignore=tests/test_unit/test_routing/test_server_error_handler.py \
  --ignore=tests/test_unit/test_streaming/test_sse/test_sse_settings.py \
  --ignore=tests/test_unit/test_throttling/test_throttling_and_parsing.py \
  tests/test_unit/

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/%dmr_pytest_name.py
%python3_sitelibdir/__pycache__/%dmr_pytest_name.*

%changelog
* Fri Aug 14 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.14.0-alt1
- Initial build for ALT.
