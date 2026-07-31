%define _unpackaged_files_terminate_build 1

%def_with check

# This is needed to fix LTO error:
# undefined symbol: ring_core_0_17_14__p256_mul_mont and etc.
# See also: https://github.com/briansmith/ring/discussions/2753
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%python3_set_limited_api

Name: python3-module-nemo-relay
Version: 0.6.0
Release: alt1

Summary: Python bindings for the NeMo Relay agent runtime
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/nemo-plugin/
Vcs: https://github.com/NVIDIA/NeMo-Relay

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nemo_relay_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps -- nemo_relay_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nemo_relay_plugin_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}

%pyproject_builddeps -- nemo_relay_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- nemo_relay_plugin_pep517 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}

Buildrequires: protobuf-compiler
BuildRequires: libprotobuf-devel

%if_with check
%add_pyproject_deps_check_filter nemo-relay-plugin

%pyproject_builddeps -- nemo_relay_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%pyproject_builddeps -- nemo_relay_plugin_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}

%pyproject_builddeps -- nemo_relay_check %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%endif

%description
NVIDIA NeMo Relay provides visibility into and control over agent runs
without requiring changes to the existing agent stack. It gives coding
agents, applications, framework integrations, middleware, and
observability backends a shared runtime for scopes, policy, plugins,
and lifecycle events.

%package plugin
Summary: Python SDK for NeMo Relay dynamic worker plugins
Group: Development/Python3
Url: https://pypi.org/project/nemo-relay-plugin/
BuildArch: noarch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- nemo_relay_plugin_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description plugin
nemo-relay-plugin is the Python authoring SDK for NeMo Relay
out-of-process dynamic worker plugins. Use it when plugin code should
run in its own Python process and communicate with Relay through the
versioned grpc-v1 worker protocol.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync nemo_relay_pep518 pep518
%pyproject_deps_resync nemo_relay_pep517 pep517
%pyproject_deps_resync nemo_relay_metadata metadata
%if_with check
%pyproject_deps_resync nemo_relay_check pep735 test
%endif

cd python/plugin
%pyproject_deps_resync nemo_relay_plugin_pep518 pep518
%pyproject_deps_resync nemo_relay_plugin_pep517 pep517
%pyproject_deps_resync nemo_relay_plugin_metadata metadata

%build
export PROTOC=%_bindir/protoc
export PROTOC_INCLUDE=%_includedir
export ZSTD_SYS_USE_PKG_CONFIG=1
%pyproject_build

cd python/plugin
%pyproject_build

%install
%pyproject_install

cd python/plugin
%pyproject_install

%check
# Can't use venv of pyproject-installer due to few packages
# built from this monorepo required for testing. Futhermore,
# some of them are platform-dependent and some noarch.
export PYTHONPATH=%buildroot%python3_sitelibdir:%buildroot%python3_sitelibdir_noarch

# Remove nemo_relay package to use built one (from builroot).
# It is necessary to workaround the problem with missed compiled
# python module.
rm -r python/nemo_relay

# Testing itself.
# Some weird tests are deselected (used uv for strange things).
python3 -m pytest -vra python/tests \
    --deselect python/tests/plugin/test_python_worker_example.py::test_example_validates_tag_configuration \
    --deselect python/tests/plugin/test_python_worker_example.py::test_manifest_entrypoint_serves_example_plugin \
    --deselect python/tests/plugin/test_python_worker_example.py::test_example_register_propagates_configured_tag \
    --deselect python/tests/test_dynamic_plugin_host.py::test_worker_activation_finalizer_never_waits_on_python_thread \
    --deselect python/tests/test_dynamic_plugin_host.py::test_worker_activation_executes_and_releases_callbacks \
    --deselect python/tests/plugin/test_package_build.py::test_sdist_rebuilds_worker_bindings_without_checked_in_codegen

%files
%python3_sitelibdir/nemo_relay/
%python3_sitelibdir/%{pyproject_distinfo nemo-relay}/

%files plugin
%python3_sitelibdir_noarch/nemo_relay_plugin/
%python3_sitelibdir_noarch/%{pyproject_distinfo nemo-relay-plugin}/

%changelog
* Fri Jul 31 2026 Anton Zhukharev <ancieg@altlinux.org> 0.6.0-alt1
- Packaged for ALT Sisyphus.
