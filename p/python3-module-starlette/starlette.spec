%define _unpackaged_files_terminate_build 1
%define pypi_name starlette

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1

Summary: The little ASGI framework that shines
License: BSD-3-Clause
Group: Development/Python3
Url: https://www.starlette.io
Vcs: https://github.com/encode/starlette

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# See: https://github.com/Kludex/starlette/pull/3054
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-zstandard
%pyproject_builddeps_metadata_extra full
%pyproject_builddeps_metadata
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
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -Wignore -q --timeout 120

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 16 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.

* Mon Mar 23 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.0-alt1
- Updated to 1.0.0.

* Tue Jan 20 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.52.1-alt1
- Updated to 0.52.1.

* Tue Dec 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.50.0-alt1
- Updated to 0.50.0.

* Thu Nov 06 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.49.1-alt1
- Updated to 0.49.1.

* Mon Jul 14 2025 Stanislav Levin <slev@altlinux.org> 0.47.1-alt2
- Fixed FTBFS (httpx 0.28.0).

* Sat Jun 21 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.47.1-alt1
- Updated to 0.47.1.

* Tue Jun 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.47.0-alt1
- Updated to 0.47.0.

* Thu Apr 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.46.2-alt1
- Updated to 0.46.2.

* Mon Mar 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.46.1-alt1
- Updated to 0.46.1.

* Mon Feb 24 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.46.0-alt1
- Updated to 0.46.0.

* Tue Jan 28 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.45.3-alt1
- Updated to 0.45.3.

* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.45.2-alt1
- Updated to 0.45.2.

* Fri Dec 27 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.43.0-alt1
- Updated to 0.43.0.

* Tue Oct 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.41.2-alt1
- Updated to 0.41.2.

* Fri Oct 25 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.41.1-alt1
- Updated to 0.41.1.

* Thu Oct 17 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.41.0-alt1
- Updated to 0.41.0.

* Tue Oct 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.40.0-alt1
- Updated to 0.40.0.

* Mon Sep 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.39.2-alt1
- Updated to 0.39.2.

* Tue Sep 24 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.39.0-alt1
- Updated to 0.39.0.

* Mon Sep 09 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.38.5-alt1
- Updated to 0.38.5.

* Wed Sep 04 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.38.4-alt1
- Updated to 0.38.4.

* Mon Jul 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.38.2-alt1
- Updated to 0.38.2.

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
