Name: python3-module-uvicorn
Version: 0.23.2
Release: alt1

Summary: An ASGI web server, for Python
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/uvicorn/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

BuildRequires: python3(pytest)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(click)
BuildRequires: python3(h11)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(trustme)
BuildRequires: python3(yaml)
BuildRequires: python3(httpx)
BuildRequires: python3(asgiref)
BuildRequires: python3(websockets)
BuildRequires: python3(wsproto)
BuildRequires: python3(watchfiles)
BuildRequires: python3(watchgod)
BuildRequires: python3(httptools)
BuildRequires: python3(dotenv)
BuildRequires: python3(a2wsgi)

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
