%define  oname mocket

%def_with check

Name:    python3-module-%oname
Version: 3.11.0
Release: alt1

Summary: Python socket mock framework

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/mindflayer/python-mocket

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-decorator
BuildRequires: python3-module-http-parser
BuildRequires: python3-module-pook
BuildRequires: python3-module-requests
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-sure
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-httpx
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-httptools
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
Socket Mock Framework - for all kinds of socket animals, web-clients
included, with gevent/asyncio/SSL support.

%prep
%setup
# gitignored by upstream, nessesary for setup.py
touch requirements.txt

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
export SKIP_TRUE_HTTP=1
export LANG=en_US.UTF-8
# TrueRedisTestCase requires a running Redis server
# other checks trying to record a real request and response
py.test-3 -k "not test_file_object and \
              not test_truesendall_with_dump_from_recording and \
              not test_asyncio_record_replay and \
              not TrueRedisTestCase"

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%doc LICENSE *.rst

%changelog
* Mon Feb 20 2023 Grigory Ustinov <grenka@altlinux.org> 3.11.0-alt1
- Automatically updated to 3.11.0.

* Sun Dec 04 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.9-alt1
- Automatically updated to 3.10.9.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.8-alt1
- Automatically updated to 3.10.8.

* Wed Aug 17 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.7-alt1
- Automatically updated to 3.10.7.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 3.10.6-alt1
- Initial build for Sisyphus.
