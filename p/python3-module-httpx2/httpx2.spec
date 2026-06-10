%define _unpackaged_files_terminate_build 1
%define core2_pypi_name httpcore2
%define core2_mod_name httpcore2
%define core2_dir src/httpcore2
%define x2_pypi_name httpx2
%define x2_mod_name httpx2
%define x2_dir src/httpx2

%define _add_x2_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps -- httpx2_metadata --extra %1 \
%%description -n %%name+%1 \
Extra "%1" for %%x2_pypi_name. \
%%files -n %%name+%1 \
}

%define _add_core2_extra() \
%{expand:%%package -n python3-module-%%core2_pypi_name+%1 \
Summary: A minimal low-level HTTP client \
Group: Development/Python3 \
Requires: python3-module-%%core2_pypi_name \
%%pyproject_runtimedeps -- httpcore2_metadata --extra %1 \
%%description -n python3-module-%%core2_pypi_name+%1 \
Extra "%1" for %%core2_pypi_name. \
%%files -n python3-module-%%core2_pypi_name+%1 \
}

%def_with check

Name: python3-module-%x2_pypi_name
Version: 2.3.0
Release: alt1

Summary: A next generation HTTP client for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/httpx2/
Vcs: https://github.com/pydantic/httpx2
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps -- httpx2_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject

%pyproject_builddeps -- httpx2_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%pyproject_builddeps -- httpcore2_pep518 %{?pyproject_deps_build_filter:--exclude %pyproject_deps_build_filter}
%if_with check
%add_pyproject_deps_check_filter 'httpcore2$'
%add_pyproject_deps_check_filter 'httpx2$'
%add_pyproject_deps_check_filter 'trio-typing$'
%pyproject_builddeps -- check_pep735 %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%pyproject_builddeps -- httpx2_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%pyproject_builddeps -- httpcore2_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
BuildRequires: python3-module-h2
BuildRequires: python3-module-socksio
BuildRequires: python3-module-zstandard
BuildRequires: python3-module-rich
%endif

%_add_x2_extra brotli
%_add_x2_extra cli
%_add_x2_extra http2
%_add_x2_extra socks
%_add_x2_extra zstd

%description
HTTPX2 is a fully featured HTTP client library for Python. It
includes an integrated command line client, has support for both
HTTP/1.1 and HTTP/2, and provides both sync and async APIs.

%package -n python3-module-%core2_pypi_name
Summary: A minimal low-level HTTP client
Group: Development/Python3
Url: https://pypi.org/project/httpcore2/

AutoReq: yes, nopython3
%pyproject_runtimedeps -- httpcore2_metadata %{?pyproject_deps_runtime_filter:--exclude %pyproject_deps_runtime_filter}

%description -n python3-module-%core2_pypi_name
The HTTP Core package provides a minimal low-level HTTP client,
which does one thing only. Sending HTTP requests.

It does not provide any high level model abstractions over the
API, does not handle redirects, multipart uploads, building
authentication headers, transparent HTTP caching, URL parsing,
session cookie handling, content or charset decoding, handling
JSON, environment based configuration defaults, or any of that
Jazz.

Some things HTTP Core does do:
- Sending HTTP requests
- Thread-safe / task-safe connection pooling
- HTTP(S) proxy & SOCKS proxy support
- Supports HTTP/1.1 and HTTP/2
- Provides both sync and async interfaces
- Async backend support for asyncio and trio

%_add_core2_extra asyncio
%_add_core2_extra http2
%_add_core2_extra socks
%_add_core2_extra trio

%prep
%setup
%autopatch -p1

for dir in %core2_dir %x2_dir; do
    sed -i 's/fallback-version = ".*"/fallback-version = "%version"/' \
        "$dir/pyproject.toml"
done

cd %core2_dir
%pyproject_deps_resync httpcore2_pep518 pep518
%pyproject_deps_resync httpcore2_metadata metadata
cd -

cd %x2_dir
%pyproject_deps_resync httpx2_pep518 pep518
%pyproject_deps_resync httpx2_metadata metadata
cd -

%if_with check
%pyproject_deps_resync check_pep735 pep735 dev
%endif

%build
for dir in %core2_dir %x2_dir; do
    cd "$dir"
    %pyproject_build
    cd -
done

%install
for dir in %core2_dir %x2_dir; do
    cd "$dir"
    %pyproject_install
    cd -
done

%check
cd %core2_dir
%pyproject_run_pytest ../../tests/httpcore2 \
    --ignore=../../tests/httpcore2/benchmark \
    -o 'filterwarnings=error'
cd -

cd %x2_dir
%pyproject_run -- bash -s <<-'ENDTESTS'
python3 -m pyproject_installer install \
    ../httpcore2/dist/httpcore2-*.whl
python3 -m pytest ../../tests/httpx2 \
    --ignore=../../tests/httpx2/models/test_whatwg.py \
    -m 'not network' \
    -o 'filterwarnings=error'
ENDTESTS
cd -

%files
%doc README.md LICENSE.md
%_bindir/%x2_pypi_name
%python3_sitelibdir/%x2_mod_name/
%python3_sitelibdir/%{pyproject_distinfo %x2_pypi_name}/

%files -n python3-module-%core2_pypi_name
%doc %core2_dir/README.md %core2_dir/LICENSE.md
%python3_sitelibdir/%core2_mod_name/
%python3_sitelibdir/%{pyproject_distinfo %core2_pypi_name}/

%changelog
* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.0-alt1
- Initial build for ALT Sisyphus.
