%define  modulename httpcore

Name:    python3-module-%modulename
Version: 0.16.3
Release: alt1

Summary: A minimal HTTP client

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://www.encode.io/httpcore/

# Source-url: https://github.com/encode/httpcore/archive/%version.tar.gz
Source:  %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

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
sed -ri 's/,\s+"anyio==[^"]+"//' setup.py
sed -ri '/h11/ s/,<[^,"]+//p' setup.py

%build
%python3_build

%install
%python3_install

# asyncio alternatives, optional
%add_python3_req_skip anyio.abc
%add_python3_req_skip anyio.streams.tls
%add_python3_req_skip curio.io

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
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
