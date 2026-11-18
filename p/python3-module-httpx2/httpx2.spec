%define _unpackaged_files_terminate_build 1
%define pypi_name httpx2
%define module_name httpx2
%define src_dir src/%pypi_name
%define tests_dir ../../tests/%pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 2.16.2
Release: alt1

Summary: A next generation HTTP client for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/httpx2/
Vcs: https://github.com/pydantic/httpx2
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: python3-module-httpcore2 = %version

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
# The test deps are the dev group of the root pyproject.toml, which the
# deps setup run in the project subdirectory cannot read: the extras come
# from the project metadata, the rest of the group is listed here.
%pyproject_configure_without_autodiscovery
%pyproject_configure_with_check_deps metadata_extra brotli
%pyproject_configure_with_check_deps metadata_extra cli
%pyproject_configure_with_check_deps metadata_extra http2
%pyproject_configure_with_check_deps metadata_extra socks
%pyproject_configure_with_check_deps metadata_extra ws
%pyproject_configure_with_check_deps metadata_extra zstd
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-chardet
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-flaky
BuildRequires: python3-module-pytest-codspeed
BuildRequires: python3-module-pytest-httpbin
BuildRequires: python3-module-pytest-trio
BuildRequires: python3-module-starlette
BuildRequires: python3-module-trio
BuildRequires: python3-module-trustme
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-websockets
BuildRequires: python3-module-werkzeug
%endif
%pyproject_configure_pypi_package

%description
HTTPX2 is a fully featured HTTP client library for Python. It
includes an integrated command line client, has support for both
HTTP/1.1 and HTTP/2, and provides both sync and async APIs.

%pyproject_configure_pypi_subpackage brotli
%pyproject_configure_pypi_subpackage cli
%pyproject_configure_pypi_subpackage http2
%pyproject_configure_pypi_subpackage socks
%pyproject_configure_pypi_subpackage ws
%pyproject_configure_pypi_subpackage zstd

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
    --ignore=%tests_dir/models/test_whatwg.py \
    -m 'not network'
cd -

%files
%doc README.md LICENSE.md
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.16.2-alt1
- Updated to 2.16.2.

* Wed Nov 18 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.16.0-alt2
- Fixed FTBFS (anyio 4.16.0).

* Wed Oct 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.16.0-alt1
- Updated to 2.16.0.

* Wed Sep 23 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.13.1-alt1
- Updated to 2.13.1.

* Thu Sep 17 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.13.0-alt1
- Updated to 2.13.0.

* Mon Sep 07 2026 Stanislav Levin <slev@altlinux.org> 2.12.0-alt2
- NMU: fixed FTBFS (click 8.5.0).

* Tue Sep 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.12.0-alt1
- Updated to 2.12.0.

* Tue Jul 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.9.1-alt1
- Updated to 2.9.1.

* Fri Jul 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Fri Jul 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.
- Split package: moved httpcore2 to a separate source package.

* Thu Jun 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.3.0-alt1
- Initial build for ALT Sisyphus.
