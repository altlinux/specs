Name: python3-module-uvicorn
Version: 0.42.0
Release: alt1

Summary: An ASGI web server, for Python
License: BSD-3-Clause
Group: Development/Python
URL: https://pypi.org/project/uvicorn
VCS: https://github.com/encode/uvicorn

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra standard
%pyproject_builddeps_check

%description
Uvicorn is an ASGI web server implementation for Python.

Until recently Python has lacked a minimal low-level server/application
interface for async frameworks. The ASGI specification fills this gap,
and means we're now able to start building a common set of tooling usable
across all async frameworks.

Uvicorn supports HTTP/1.1 and WebSockets.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%_bindir/uvicorn
%python3_sitelibdir/uvicorn
%python3_sitelibdir/uvicorn-%version.dist-info

%changelog
* Mon Mar 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.42.0-alt1
- 0.42.0 released

* Tue Feb 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.41.0-alt1
- 0.41.0 released

* Mon Dec 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.40.0-alt1
- 0.40.0 released

* Wed Nov 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.38.0-alt1
- 0.38.0 released

* Mon Jul 14 2025 Stanislav Levin <slev@altlinux.org> 0.35.0-alt2
- Fixed FTBFS (httpx 0.28.0).

* Thu Jul 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.35.0-alt1
- 0.35.0 released

* Tue Nov 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.32.0-alt1
- 0.32.0 released

* Tue May 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.29.0-alt1
- 0.29.0 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.26.0-alt1
- 0.26.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23.2-alt1
- 0.23.2 released

* Wed May 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.0-alt1
- 0.22.0 released

* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.0-alt1
- 0.20.0 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- 0.19.0 released

* Thu Aug 04 2022 Anton Zhukharev <ancieg@altlinux.org> 0.18.2-alt2
- update summary and description
- add check

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.2-alt1
- 0.18.2 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17.5-alt1
- 0.17.5

* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.3-alt1
- initial
