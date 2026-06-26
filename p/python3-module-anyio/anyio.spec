%define _unpackaged_files_terminate_build 1
%define pypi_name anyio

%def_with check

Name: python3-module-anyio
Version: 4.14.1
Release: alt1

Summary: High level compatibility layer for multiple asynchronous event loop implementations
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/anyio
Vcs: https://github.com/agronholm/anyio

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-trio-tests
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

# either asyncio or trio
%filter_from_requires /python3(trio.*)/d
# don't add found requires from pytest plugin to requirement list
%add_findreq_skiplist %python3_sitelibdir/%pypi_name/pytest_plugin.py

%description
AnyIO is an asynchronous networking and concurrency library
that works on top of either asyncio or trio.
It implements trio-like structured concurrency (SC) on top of asyncio,
and works in harmony with the native SC of trio itself.

Applications and libraries written against AnyIO's API will run
unmodified on either asyncio or trio.
AnyIO can also be adopted into a library or application incrementally -
bit by bit, no full refactoring necessary.
It will blend in with native libraries of your chosen backend.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_socket.py:
# Ignore this file since configured DNS and internet are required by most of
# the tests. Another tests are bad itself and can fail accidentally.
%pyproject_run_pytest -Wignore -m "not network" --ignore="tests/test_sockets.py"

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 26 2026 Alexandr Shashkin <dutyrok@altlinux.org> 4.14.1-alt1
- Updated to 4.14.1.

* Tue Jun 16 2026 Alexandr Shashkin <dutyrok@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Wed Mar 25 2026 Alexandr Shashkin <dutyrok@altlinux.org> 4.13.0-alt1
- Updated to 4.13.0.

* Thu Jan 15 2026 Alexandr Shashkin <dutyrok@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Tue Dec 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Tue Oct 14 2025 Alexander Burmatov <thatman@altlinux.org> 4.11.0-alt1
- Updated to 4.11.0.

* Thu Aug 07 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.9.0-alt1
- Updated to 4.9.0.

* Sun Mar 02 2025 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt2
- skip _pytest.fixtures _pytest.outcomes from requires

* Wed Jan 15 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.8.0-alt1
- Updated to 4.8.0.

* Fri Dec 27 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.7.0-alt1
- Updated to 4.7.0.

* Tue Oct 15 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.6.2-alt1.post1
- Updated to 4.6.2.post1.

* Mon Sep 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.6.0-alt1
- Updated to 4.6.0.

* Fri Sep 20 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.5.0-alt1
- Updated to 4.5.0.

* Mon May 27 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.4.0-alt1
- 4.3.0 -> 4.4.0.

* Sun Mar 03 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.3.0-alt1
- 4.2.0 -> 4.3.0

* Thu Feb 08 2024 Alexandr Shashkin <dutyrok@altlinux.org> 4.2.0-alt1
- 3.6.2 -> 4.2.0

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version 3.6.2 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version 3.6.1 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt1
- new version 3.5.0 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus
