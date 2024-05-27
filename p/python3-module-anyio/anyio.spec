%define _unpackaged_files_terminate_build 1
%define pypi_name anyio

%def_with check

Name: python3-module-anyio
Version: 4.4.0
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
%pyproject_builddeps_metadata_extra test
%endif

# either asyncio or trio
%filter_from_requires /python3(trio.*)/d
# clean pytest from requirements
%add_python3_req_skip pytest

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

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -Wignore -m "not network"

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
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
