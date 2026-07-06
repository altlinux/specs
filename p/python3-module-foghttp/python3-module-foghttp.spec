%define _unpackaged_files_terminate_build 1
%define pypi_name foghttp
%define mod_name foghttp

%def_with check

# This is needed to fix LTO error:
# undefined symbol: ring_core_0_17_14__p256_mul_mont
# See also: https://github.com/briansmith/ring/discussions/2753
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%python3_set_limited_api

Name: python3-module-%pypi_name
Version: 0.3.5
Release: alt2

Summary: Observable Rust-powered HTTP client for Python services
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/foghttp/
Vcs: https://github.com/AmberFog/foghttp

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
Rust-powered HTTP client for Python with sync and asyncio APIs.

FogHTTP is an early MVP HTTP client. The public API is Python-first,
while the transport core is implemented in Rust on top of hyper.

FogHTTP is positioned as an observable, high-concurrency Rust-powered
transport for Python services. It is built for controlled
service-to-service HTTP workloads where explicit lifecycle, predictable
resource usage, cancellation, redirect history, and request
backpressure visibility matter more than browser-like feature parity.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- pytest -vra --import-mode=importlib \
               --ignore=tests/client_multipart/test_async_multipart.py

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.3.5-alt2
- Disabled flaky tests.

* Fri Jul 03 2026 Anton Zhukharev <ancieg@altlinux.org> 0.3.5-alt1
- Packaged for ALT Sisyphus.
