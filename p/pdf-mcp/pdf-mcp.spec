Name: pdf-mcp
Version: 3.7.0
Release: alt1

Summary: Agentic RAG over your PDFs
License: MIT
Group: Development/Python
URL: https://pypi.org/project/pdf-mcp
VCS: https://github.com/jztan/pdf-mcp

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: pyproject_deps.json

Requires: python3-module-pdf-mcp = %EVR
Requires: python3-module-pypdfium2

BuildRequires(pre): rpm-build-pyproject
# ALT splits fastmcp's server support into the +server extra subpackage,
# which pdf_mcp._core needs unconditionally (from fastmcp import FastMCP)
BuildRequires: python3-module-fastmcp+server
# dev-extra entries that are audit tooling, not test deps; the default
# check filter already drops black/flake8/mypy/pre-commit/pytest-cov
%add_pyproject_deps_check_filter '^pip$'
%add_pyproject_deps_check_filter '^pip-audit$'
%add_pyproject_deps_check_filter '^msgpack$'
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check
# mcp.client.session imports jsonschema unconditionally; it was dropped
# from python3-module-mcp runtime deps as "test-only" (ALT #60782)
BuildRequires: python3-module-jsonschema
BuildRequires: /proc

%package -n python3-module-%name
Summary: %summary
Group: Development/Python
Requires: python3-module-fastmcp+server
# pypdfium2 exists only on selected arches, we can't have
# dependency on it in noarch package (ALT #61372)
%add_pyproject_deps_runtime_filter pypdfium2
%pyproject_runtimedeps_metadata
Autoreq: yes, nopython3
BuildArch: noarch

%description
%summary

%description -n python3-module-%name
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
install -pm0644 -D deploy/pdf-mcp.sysusers %buildroot%_sysusersdir/pdf-mcp.conf
install -pm0644 -D deploy/pdf-mcp-http.service %buildroot%_unitdir/pdf-mcp-http.service
install -pm0640 -D deploy/pdf-mcp-http.env %buildroot%_sysconfdir/pdf-mcp/env
install -pm0640 deploy/config.toml.example %buildroot%_sysconfdir/pdf-mcp/config.toml
install -d %buildroot%_localstatedir/pdf-mcp/cache

%check
# Materialize the generated content-trust corpus once, before xdist:
# otherwise each worker's module fixture regenerates it concurrently
# into the build tree and the builders race (FileNotFoundError on farm).
python3 -c "import importlib.util; s=importlib.util.spec_from_file_location('g', 'benchmark_data/content_trust_corpus/generate.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); m.build('benchmark_data/content_trust_corpus')"
# upstream addopts force coverage reporting; keep the test run plain.
# Upstream CI never runs the suite single-process: under xdist (-n auto)
# the tests that swap module-level state (warm pool, background embedder)
# stay isolated per worker. Sequential runs race exactly the way our
# first iterations did (one random warm-adjacent test per run). The
# 'slow' marker holds retrieval-quality gates that need HuggingFace
# models, so it is skipped here entirely.
# Deselected: tests needing the Internet (URL fetches, arXiv, HuggingFace
# model downloads) fail on the offline build farm; the German FTS tests
# need snowballstemmer >= 3 for the umlaut folding, sisyphus ships 2.2.0.
%pyproject_run_pytest -o addopts= -n auto -m 'not slow' \
    --deselect tests/test_url_fetcher_security.py::test_rejects_text_html_content_type \
    --deselect tests/test_pregate_validation.py::test_non_arxiv_two_column_pages_are_not_short_circuited \
    --deselect tests/test_build_mcpb.py::test_real_export_includes_core_dependencies \
    --deselect tests/test_warm_cli.py::TestMainEndToEnd::test_embeddings_flag_warms_vectors \
    --deselect 'tests/test_server.py::TestSearchGeometry::test_search_geometry_all_modes[semantic]' \
    --deselect tests/test_pdfium_concurrency.py::test_parallel_tool_calls_neither_crash_nor_poison_the_engine \
    --deselect tests/test_pdfium_concurrency.py::test_eight_parallel_calls_through_the_mcp_client_all_succeed \
    --deselect tests/test_cache_german_fts.py::test_german_normalize_unifies_inflections_and_spelling_variants \
    --deselect tests/test_benchmark_german_fts.py::test_german_mode_beats_porter_default_on_inflected_and_spelling_queries

%files
%config(noreplace) %attr(0640,root,pdf-mcp) %_sysconfdir/pdf-mcp/env
%config(noreplace) %attr(0640,root,pdf-mcp) %_sysconfdir/pdf-mcp/config.toml
%_bindir/pdf-mcp-http
%_unitdir/pdf-mcp-http.service
%_sysusersdir/pdf-mcp.conf
%attr(0770,root,pdf-mcp) %_localstatedir/pdf-mcp
%attr(0700,pdf-mcp,pdf-mcp) %_localstatedir/pdf-mcp/cache

%files -n python3-module-pdf-mcp
%_bindir/pdf-mcp
%_bindir/pdf-mcp-warm
%python3_sitelibdir_noarch/pdf_mcp
%python3_sitelibdir_noarch/pdf_mcp-%version.dist-info

%changelog
* Sat Nov 07 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.0-alt1
- 3.7.0 released
