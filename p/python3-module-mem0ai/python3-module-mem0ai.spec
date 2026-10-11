%define pypi_name mem0ai
%define mod_name mem0

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Long-term memory layer for AI agents
License: Apache-2.0
Group: Development/Python3
URL: https://github.com/mem0ai/mem0

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

# Optional provider backends (vector stores, embedders, LLMs, rerankers):
# their modules are loaded lazily by mem0.utils.factory only when selected
# in the config, so the provider libraries are not hard dependencies.
%add_python3_req_skip azure.identity
%add_python3_req_skip databricks.sdk databricks.sdk.service.catalog
%add_python3_req_skip databricks.sdk.service.sql databricks.sdk.service.vectorsearch
%add_python3_req_skip google google.api_core.exceptions google.cloud google.genai google.oauth2
%add_python3_req_skip google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint
%add_python3_req_skip numpy pymilvus sentence_transformers together
%add_python3_req_skip redis redis.commands.search.query
%add_python3_req_skip redisvl.index redisvl.query redisvl.query.filter
%add_python3_req_skip valkey valkey.exceptions vertexai.language_models
%add_python3_req_skip weaviate.classes.config weaviate.classes.init
%add_python3_req_skip weaviate.classes.query weaviate.util

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_disabled check
%else
# for the import smoke test in %%check
BuildRequires: python3-module-httpx python3-module-openai python3-module-posthog
BuildRequires: python3-module-pydantic python3-module-pytz python3-module-qdrant-client
BuildRequires: python3-module-sqlalchemy
%endif

%description
Mem0 is an intelligent memory layer for AI assistants and agents.
It remembers user preferences, adapts to individual needs and
continuously learns over time.

This package contains the core library with the OpenAI LLM
and Qdrant vector store backends; other providers are optional.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# upstream tests are not shipped in the sdist; smoke-test the imports
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c 'import mem0, mem0.llms.openai, mem0.configs.llms.openai; print(mem0.__version__)'

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- initial build for Sisyphus
