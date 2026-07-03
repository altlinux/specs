%define _unpackaged_files_terminate_build 1
%define pypi_name httpcore2
%define module_name httpcore2
%define src_dir src/%module_name
%define tests_dir ../../tests/%pypi_name
%def_with check

%define _add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1 \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1

Summary: A minimal low-level HTTP client
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/httpcore2/
Vcs: https://github.com/pydantic/httpx2
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
%add_pyproject_deps_check_filter 'httpx2$'
%add_pyproject_deps_check_filter 'trio-typing$'
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra asyncio
%pyproject_builddeps_metadata_extra http2
%pyproject_builddeps_metadata_extra socks
%pyproject_builddeps_metadata_extra trio
%pyproject_builddeps_check
%endif

%_add_python_extra asyncio
%_add_python_extra http2
%_add_python_extra socks
%_add_python_extra trio

%description
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

%prep
%setup
%autopatch -p1
cd %src_dir
sed -i '/^fallback-version/s/= ".*"/= "%version"/' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
cd -
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
cd %src_dir
%pyproject_build
cd -

%install
cd %src_dir
%pyproject_install
cd -

%check
cd %src_dir
%pyproject_run_pytest %tests_dir \
    --ignore=%tests_dir/benchmark
cd -

%files
%doc %src_dir/README.md %src_dir/LICENSE.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.
- Detached httpcore2 from the python3-module-httpx2 source package.
