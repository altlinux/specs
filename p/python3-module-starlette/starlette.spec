%define _unpackaged_files_terminate_build 1
%define pypi_name starlette

%def_with check

Name: python3-module-%pypi_name
Version: 0.38.0
Release: alt1

Summary: The little ASGI framework that shines
License: BSD-3-Clause
Group: Development/Python3
Url: https://www.starlette.io
Vcs: https://github.com/encode/starlette

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra full
%pyproject_builddeps_check
%endif

%description
Starlette is a lightweight ASGI framework/toolkit, which is ideal for
building async web services in Python.

It is production-ready, and gives you the following:
- A lightweight, low-complexity HTTP web framework.
- WebSocket support.
- In-process background tasks.
- Startup and shutdown events.
- Test client built on httpx.
- CORS, GZip, Static Files, Streaming responses.
- Session and Cookie support.
- 100%% test coverage.
- 100%% type annotated codebase.
- Few hard dependencies.
- Compatible with asyncio and trio backends.
- Great overall performance against independent benchmarks.

%prep
%setup
sed -n '/^# Testing$/,/^[[:space:]]*$/p' requirements.txt | \
    tee test-requirements.txt
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -Wignore

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 22 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.38.0-alt1
- 0.37.2 -> 0.38.0.

* Wed Mar 06 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.37.2-alt1
- 0.37.1 -> 0.37.2

* Tue Feb 13 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.37.1-alt1
- 0.37.0 -> 0.37.1

* Fri Feb 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.37.0-alt1
- 0.31.1 -> 0.37.0

* Sun Dec 31 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.31.1-alt1
- 0.28.0 -> 0.31.1

* Tue Aug 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.28.0-alt2
- Fixed dependency on wrong multipart module.

* Thu Jul 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.28.0-alt1
- 0.28.0

* Fri May 19 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.27.0-alt1
- new version (0.27.0) with rpmgs script

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 0.26.1-alt1
- new version 0.26.1 (with rpmrb script)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 0.25.0-alt1
- new version 0.25.0 (with rpmrb script)

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 0.23.1-alt1
- new version 0.23.1 (with rpmrb script)

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.0-alt1
- 0.21.0

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt1
- new version 0.20.4 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.13.4-alt1
- initial build for Sisyphus
