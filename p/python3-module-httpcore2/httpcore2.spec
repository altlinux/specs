%define _unpackaged_files_terminate_build 1
%define pypi_name httpcore2
%define module_name httpcore2
%define src_dir src/%module_name
%define tests_dir ../../tests/%pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 2.16.2
Release: alt1

Summary: A minimal low-level HTTP client
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/httpcore2/
Vcs: https://github.com/pydantic/httpx2
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
# The test deps are the dev group of the root pyproject.toml, which the
# deps setup run in the project subdirectory cannot read: the extras come
# from the project metadata, the rest of the group is listed here. The
# group also pulls httpx2, which is built on top of httpcore2.
%pyproject_configure_without_autodiscovery
%pyproject_configure_with_check_deps metadata_extra asyncio
%pyproject_configure_with_check_deps metadata_extra http2
%pyproject_configure_with_check_deps metadata_extra socks
%pyproject_configure_with_check_deps metadata_extra trio
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-chardet
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-flaky
BuildRequires: python3-module-pytest-codspeed
BuildRequires: python3-module-pytest-httpbin
BuildRequires: python3-module-pytest-trio
BuildRequires: python3-module-starlette
BuildRequires: python3-module-trustme
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-websockets
BuildRequires: python3-module-werkzeug
%endif
%pyproject_configure_pypi_package

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

%pyproject_configure_pypi_subpackage asyncio
%pyproject_configure_pypi_subpackage http2
%pyproject_configure_pypi_subpackage socks
%pyproject_configure_pypi_subpackage trio

%prep
%setup
%autopatch -p1
cd %src_dir
sed -i '/^fallback-version/s/= ".*"/= "%version"/' pyproject.toml
%pyproject_setup_deps
cd -

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
%pyproject_run_pytest --session-timeout=600 %tests_dir \
    --ignore=%tests_dir/benchmark
cd -

%files
%doc %src_dir/README.md %src_dir/LICENSE.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.16.2-alt1
- Updated to 2.16.2.

* Wed Nov 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.16.0-alt2
- Migrated to the new pyproject macros.

* Wed Oct 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.16.0-alt1
- Updated to 2.16.0.

* Wed Sep 23 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.13.1-alt1
- Updated to 2.13.1.

* Thu Sep 17 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.13.0-alt1
- Updated to 2.13.0.

* Tue Sep 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.12.0-alt1
- Updated to 2.12.0.

* Tue Jul 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.9.1-alt1
- Updated to 2.9.1.

* Fri Jul 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Fri Jul 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.
- Detached httpcore2 from the python3-module-httpx2 source package.
