%define  modulename starlette

Name:    python3-module-%modulename
Version: 0.21.0
Release: alt1

Summary: The little ASGI framework that shines

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://www.starlette.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/encode/starlette/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)

BuildArch: noarch

%description
Starlette is a lightweight ASGI framework/toolkit,
which is ideal for building high performance asyncio services.

It is production-ready, and gives you the following:

Seriously impressive performance.
WebSocket support.
GraphQL support.
In-process background tasks.
Startup and shutdown events.
Test client built on requests.
CORS, GZip, Static Files, Streaming responses.
Session and Cookie support.
100%% test coverage.
100%% type annotated codebase.
Zero hard dependencies.


%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
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
