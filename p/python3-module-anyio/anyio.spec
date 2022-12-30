%define oname anyio

Name: python3-module-anyio
Version: 3.6.2
Release: alt1

Summary: High level compatibility layer for multiple asynchronous event loop implementations

License: MIT
Group: Development/Python3
Url: https://github.com/agronholm/anyio

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

# either asyncio or trio
%add_python3_req_skip trio.from_thread trio.socket trio.to_thread


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

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version 3.6.2 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 3.6.1-alt1
- new version 3.6.1 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt1
- new version 3.5.0 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus
