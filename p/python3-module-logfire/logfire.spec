%define _unpackaged_files_terminate_build 1
%define pypi_name logfire
%def_with check

Name: python3-module-%pypi_name
Version: 5.1.1
Release: alt1

Summary: Observability and telemetry tooling for Python built on OpenTelemetry
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logfire/
Vcs: https://github.com/pydantic/logfire
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# test_cli.py drives the git binary in scratch repositories and expects
# the uv binary for its install hints.
BuildRequires: git-core
BuildRequires: uv
# Needed at pytest config parse: filterwarnings imports beartype classes.
BuildRequires: python3-module-beartype
# pytest-django needs the stdlib sqlite3 module for django's sqlite backend.
BuildRequires: python3-modules-sqlite3
# ALT splits django backends out of the main package; pytest-django's sqlite
# settings need the sqlite3 backend subpackage.
BuildRequires: python3-module-django-dbbackend-sqlite3
# Not packaged for ALT yet.
%add_pyproject_deps_check_filter '^openinference-instrumentation-litellm$'
%add_pyproject_deps_check_filter '^openinference-instrumentation-dspy$'
%add_pyproject_deps_check_filter '^dspy$'
%add_pyproject_deps_check_filter '^testcontainers$'
%add_pyproject_deps_check_filter '^pydantic-ai-slim$'
%add_pyproject_deps_check_filter '^pydantic-evals$'
%add_pyproject_deps_check_filter '^surrealdb$'
%add_pyproject_deps_check_filter '^mysql-connector-python$'
# ALT ships the elasticsearch client at 5.x only, and elastic-transport,
# imported by the integration tests at collection, is not packaged at all.
%add_pyproject_deps_check_filter '^elasticsearch$'
# Not packaged in ALT.
%add_pyproject_deps_check_filter '^psycopg2-binary$'
# Type stubs for pyright only; the test suite never imports them.
%add_pyproject_deps_check_filter '^types-requests$'
%add_pyproject_deps_check_filter '^pyarrow-stubs$'
# Backport for Python < 3.10, a no-op on the packaged interpreter.
%add_pyproject_deps_check_filter '^eval-type-backport$'
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Logfire is an observability tool built on OpenTelemetry: structured
logging, tracing and metrics with a developer-friendly Python API and
console output.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# These files import, at collection or unconditionally, a module whose
# package is still absent from ALT: dspy, mysql.connector, pydantic_ai
# (pydantic-ai-slim), surrealdb, elastic_transport (elasticsearch) and
# testcontainers (celery, redis, mysql); testcontainers would also need
# a Docker daemon, which hasher never has.
# test_docs.py: doc-example output drifts against the packaged doc
# toolchain versions.
# The anthropic, google_genai, langchain, litellm, openai, openai_agents
# and sqlalchemy files compare against snapshots recorded with other
# library versions than Sisyphus ships, and test_openai_agents_mcp.py
# reaches into FastMCP internals renamed in mcp 2.x.
# Deselected: test_cli.py::test_inspect, whose summary lists every
# instrumentable package installed (tornado is in the check set);
# snapshots that depend on the exact library versions in the check set
# (test_configure, test_logfire_api, test_otel_logs, aiohttp-client, asgi,
# and fastapi 0.141.1 for the subapp tests); numpy tests hardcoding the
# int64 dtype, which is int32 on i586.
%pyproject_run_pytest \
	--ignore tests/otel_integrations/test_celery.py \
	--ignore tests/otel_integrations/test_dspy.py \
	--ignore tests/otel_integrations/test_elasticsearch.py \
	--ignore tests/otel_integrations/test_mysql.py \
	--ignore tests/otel_integrations/test_pydantic_ai.py \
	--ignore tests/otel_integrations/test_pydantic_ai_mcp.py \
	--ignore tests/otel_integrations/test_redis.py \
	--ignore tests/otel_integrations/test_surrealdb.py \
	--ignore tests/test_docs.py \
	--ignore tests/otel_integrations/test_anthropic.py \
	--ignore tests/otel_integrations/test_anthropic_bedrock.py \
	--ignore tests/otel_integrations/test_google_genai.py \
	--ignore tests/otel_integrations/test_langchain.py \
	--ignore tests/otel_integrations/test_litellm.py \
	--ignore tests/otel_integrations/test_openai.py \
	--ignore tests/otel_integrations/test_openai_agents.py \
	--ignore tests/otel_integrations/test_openai_agents_mcp.py \
	--ignore tests/otel_integrations/test_sqlalchemy.py \
	--deselect tests/test_cli.py::test_inspect \
	--deselect tests/test_configure.py::test_configure_service_version \
	--deselect tests/test_configure.py::test_auto_detected_service_version_serialized \
	--deselect tests/test_configure.py::test_configuration_span_emitted_when_opted_in \
	--deselect tests/test_logfire_api.py::test_runtime \
	--deselect tests/test_otel_logs.py::test_log_events \
	--deselect tests/test_otel_logs.py::test_log_events_with_kwargs \
	--deselect tests/otel_integrations/test_aiohttp_client.py::test_aiohttp_client_capture_all \
	--deselect tests/otel_integrations/test_aiohttp_client.py::test_aiohttp_client_capture_all_environment_variable \
	--deselect tests/otel_integrations/test_aiohttp_client.py::test_aiohttp_client_capture_response_body \
	--deselect tests/otel_integrations/test_asgi.py::test_asgi_middleware \
	--deselect tests/otel_integrations/test_fastapi.py::test_first_lvl_subapp_fastapi_arguments \
	--deselect tests/otel_integrations/test_fastapi.py::test_second_lvl_subapp_fastapi_arguments \
	--deselect 'tests/test_json_args.py::test_log_non_scalar_args[numpy_array]' \
	--deselect 'tests/test_json_args.py::test_log_non_scalar_args[numpy_array_2d]' \
	--deselect 'tests/test_json_args.py::test_log_non_scalar_args[numpy_array_3d]' \
	--deselect 'tests/test_json_args.py::test_log_non_scalar_args[numpy_matrix]' \
	--deselect tests/test_json_args.py::test_numpy_array_truncation

%files
%doc README.md LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.1.1-alt1
- Initial build for ALT Sisyphus.
