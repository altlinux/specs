%define _unpackaged_files_terminate_build 1
%define pypi_name logfire-sdk
%def_with check

Name: python3-module-%pypi_name
Version: 5.6.0
Release: alt1

Summary: Observability and telemetry tooling for Python built on OpenTelemetry
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logfire-sdk/
Vcs: https://github.com/pydantic/logfire
BuildArch: noarch

Source0: %name-%version.tar
Source1: export-dependency-group.py
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: python3-module-pytest-timeout
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
# The dev group asks for fastmcp-slim[server] only; test_mcp_v2.py also
# needs the FastMCP client.
BuildRequires: python3-module-fastmcp-slim+client
# No +extra subpackages of these exist in Sisyphus: psycopg[binary],
# faststream[redis] and openai-agents[voice] are required as the plain
# packages instead.
%pyproject_configure_with_check_filter 'psycopg$' 'faststream$' 'openai-agents$'
BuildRequires: python3-module-psycopg
BuildRequires: python3-module-faststream
BuildRequires: python3-module-openai-agents
# Not packaged for ALT yet.
%pyproject_configure_with_check_filter '^openinference-instrumentation-litellm$'
%pyproject_configure_with_check_filter '^openinference-instrumentation-dspy$'
%pyproject_configure_with_check_filter '^dspy$'
%pyproject_configure_with_check_filter '^testcontainers$'
%pyproject_configure_with_check_filter '^pydantic-ai-slim$'
%pyproject_configure_with_check_filter '^pydantic-evals$'
%pyproject_configure_with_check_filter '^surrealdb$'
%pyproject_configure_with_check_filter '^mysql-connector-python$'
# ALT ships the elasticsearch client at 5.x only, and elastic-transport,
# imported by the integration tests at collection, is not packaged at all.
%pyproject_configure_with_check_filter '^elasticsearch$'
# Not packaged in ALT.
%pyproject_configure_with_check_filter '^psycopg2-binary$'
# Type stubs for pyright only; the test suite never imports them.
%pyproject_configure_with_check_filter '^types-requests$'
%pyproject_configure_with_check_filter '^pyarrow-stubs$'
# Backport for Python < 3.10, a no-op on the packaged interpreter.
%pyproject_configure_with_check_filter '^eval-type-backport$'
# Not packaged for ALT yet: the Monty sandboxed interpreter, the
# Snowflake driver and the Logfire Fleet client.
%pyproject_configure_with_check_filter '^pydantic-monty$'
%pyproject_configure_with_check_filter '^snowflake-connector-python$'
%pyproject_configure_with_check_filter '^logfire-fleet-otel$'
%endif
%pyproject_configure_pypi_package
# The extras whose deps are all in ALT are packaged as the subpackages
# below. Not packaged, their deps are missing: agent-sandboxes
# (pydantic-monty-client), datasets (pydantic-evals), dspy and litellm
# (openinference instrumentations), fleet (logfire-fleet-otel).

%description
Logfire is an observability tool built on OpenTelemetry: structured
logging, tracing and metrics with a developer-friendly Python API and
console output. This package carries the SDK implementation that the
logfire distribution has delegated to logfire-sdk since 5.4.0.

%pyproject_configure_pypi_subpackage gateway
%pyproject_configure_pypi_subpackage system-metrics
%pyproject_configure_pypi_subpackage asgi
%pyproject_configure_pypi_subpackage wsgi
%pyproject_configure_pypi_subpackage aiohttp
%pyproject_configure_pypi_subpackage aiohttp-client
%pyproject_configure_pypi_subpackage aiohttp-server
%pyproject_configure_pypi_subpackage celery
%pyproject_configure_pypi_subpackage django
%pyproject_configure_pypi_subpackage fastapi
%pyproject_configure_pypi_subpackage flask
%pyproject_configure_pypi_subpackage httpx
%pyproject_configure_pypi_subpackage starlette
%pyproject_configure_pypi_subpackage litestar
%pyproject_configure_pypi_subpackage sqlalchemy
%pyproject_configure_pypi_subpackage asyncpg
%pyproject_configure_pypi_subpackage psycopg
%pyproject_configure_pypi_subpackage psycopg2
%pyproject_configure_pypi_subpackage pymongo
%pyproject_configure_pypi_subpackage redis
%pyproject_configure_pypi_subpackage requests
%pyproject_configure_pypi_subpackage mysql
%pyproject_configure_pypi_subpackage sqlite3
%pyproject_configure_pypi_subpackage urllib
%pyproject_configure_pypi_subpackage aws-lambda
%pyproject_configure_pypi_subpackage google-genai
%pyproject_configure_pypi_subpackage variables

%prep
%setup
%autopatch -p1
cd logfire-sdk
%if_with check
# The test deps are the dev group of the workspace root pyproject.toml,
# which the deps sync cannot read from logfire-sdk/: export the group as
# the dev-requirements.txt reqfile the check autodiscovery picks up.
%SOURCE1 --pyproject ../pyproject.toml --group dev \
	--output dev-requirements.txt
%endif
%pyproject_setup_deps
cd -

%build
cd logfire-sdk
%pyproject_build
cd -

%install
cd logfire-sdk
%pyproject_install
cd -

%check
# The suite lives at the repository root and runs against the installed
# SDK; pytest configuration is read from the root pyproject.toml. The
# wheel tracker written by the build step sits in logfire-sdk/dist,
# so expose it at the root for the test runner.
# These files import, at collection or unconditionally, a module whose
# package is still absent from ALT: dspy, mysql.connector, pydantic_ai
# (pydantic-ai-slim), surrealdb, elastic_transport (elasticsearch) and
# testcontainers (celery, redis, mysql); testcontainers would also need
# a Docker daemon, which hasher never has.
# New in 5.4.0 and likewise unpackaged: pydantic-monty (test_monty.py,
# and test_agent_sandboxes.py through pydantic-monty-client) and the
# Snowflake driver.
# test_docs.py: doc-example output drifts against the packaged doc
# toolchain versions.
# test_editable_sdk_uses_the_source_tree asserts the upstream editable
# dev install; the package runs the suite against the built wheel.
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
ln -s logfire-sdk/dist dist
%pyproject_run_pytest --session-timeout=600 \
	tests \
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
	--ignore tests/otel_integrations/test_monty.py \
	--ignore tests/otel_integrations/test_snowflake.py \
	--ignore tests/test_agent_sandboxes.py \
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
	--deselect tests/test_json_args.py::test_numpy_array_truncation \
	--deselect tests/test_distribution_metadata.py::test_editable_sdk_uses_the_source_tree

%files
%doc logfire-sdk/README.md logfire-sdk/LICENSE
# The wheel ships the SDK twice: as the top-level logfire package and
# as the _logfire_sdk fallback copy that logfire_sdk.pth puts on
# sys.path for upgrades from the monolithic logfire 5 wheel.
%python3_sitelibdir/logfire/
%python3_sitelibdir/_logfire_sdk/
%python3_sitelibdir/logfire_sdk.pth
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.6.0-alt1
- Updated to 5.6.0.

* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.4.0-alt1
- Initial build for ALT Sisyphus.
