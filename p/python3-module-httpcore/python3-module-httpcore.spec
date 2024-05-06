%define  modulename httpcore

Name:    python3-module-%modulename
Version: 1.0.5
Release: alt1

Summary: A minimal HTTP client

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://www.encode.io/httpcore/

# Source-url: https://github.com/encode/httpcore/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-fancy-pypi-readme)

BuildArch: noarch

%description
The HTTP Core package provides a minimal low-level HTTP client,
which does one thing only. Sending HTTP requests.

It does not provide any high level model abstractions over the API,
does not handle redirects, multipart uploads, building authentication headers,
transparent HTTP caching, URL parsing, session cookie handling,
content or charset decoding, handling JSON,
environment based configuration defaults, or any of that Jazz.

Some things HTTP Core does do:

* Sending HTTP requests.
* Provides both sync and async interfaces.
* Supports HTTP/1.1 and HTTP/2.
* Async backend support for asyncio and trio.
* Automatic connection pooling.
* HTTP(S) proxy support.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

# asyncio alternatives, optional
%add_python3_req_skip anyio sockio trio
%add_python3_req_skip h2.config h2.connection h2.events h2.exceptions h2.settings

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.dist-info

%changelog
* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.5-alt1
- 1.0.5

* Fri Jan 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt1
- new version 0.17.0 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 0.16.3-alt1
- new version 0.16.3 (with rpmrb script)

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.7-alt1
- 0.14.7

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.7-alt1
- 0.13.7

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 0.13.6-alt1
- new version 0.13.6 (with rpmrb script)

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.3-alt1
- 0.13.3

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.3-alt1
- new version 0.12.3 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.2-alt1
- new version 0.12.2 (with rpmrb script)

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for Sisyphus
