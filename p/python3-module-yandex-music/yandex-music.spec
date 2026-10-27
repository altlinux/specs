Name: python3-module-yandex-music
Version: 3.2.2
Release: alt1

Summary: Library for the Yandex.Music API
License: LGPL-3.0-only
Group: Development/Python
URL: https://pypi.org/project/yandex-music/
VCS: https://github.com/MarshalX/yandex-music-api

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
This library provides a Python interface for the undocumented and
self-hosted Yandex Music API. It is compatible with Python 3.8+ and
supports both synchronous and asynchronous (asyncio) code.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup test

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/yandex_music/
%python3_sitelibdir/yandex_music-%version.dist-info/

%changelog
* Wed Oct 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.2-alt1
- 3.2.2 released

* Sat Nov 01 2025 Tatyana Gagina <treza@altlinux.org> 2.2.0-alt1
- Packaged for ALT Sisyphus.
