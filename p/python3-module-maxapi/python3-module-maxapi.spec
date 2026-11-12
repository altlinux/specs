%define pypi_name maxapi-python

Name: python3-module-maxapi
Version: 2.5.0
Release: alt1

Summary: Asynchronous Python client for the MAX messenger API

License: MIT
Group: Development/Python3
URL: https://github.com/MaxApiTeam/PyMax
# Source-url: https://github.com/MaxApiTeam/PyMax/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 python3-module-hatchling
BuildRequires: python3-module-pytest python3-module-pytest-asyncio
BuildRequires: python3-module-aiofiles >= 25.1.0
BuildRequires: python3-module-aiohttp >= 3.13.5
BuildRequires: python3-module-aiosqlite >= 0.22.1
BuildRequires: python3-module-msgpack >= 1.1.2
BuildRequires: python3-module-pydantic >= 2.10.0
BuildRequires: python3-module-python-socks >= 2.8.1
BuildRequires: python3-module-qrcode >= 8.2
BuildRequires: python3-module-websockets >= 16.0
BuildRequires: python3-module-zstandard >= 0.25.0

%description
PyMax is an asynchronous Python client for the unofficial MAX messenger API.
It supports TCP and WebSocket connections, messaging, chats, attachments,
routers, filters and SQLite sessions.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
test -s %buildroot%python3_sitelibdir/pymax/_data/apk_fingerprints.json
%pyproject_run_pytest

%files
%doc README.md LICENSE
# Includes _data/apk_fingerprints.json, loaded through importlib.resources.
%python3_sitelibdir/pymax/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 08 2026 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- initial build for Sisyphus.

