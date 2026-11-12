%define pypi_name matrix-nio

Name: python3-module-matrix-nio
Version: 0.26.0
Release: alt1

Summary: Python Matrix client library with end-to-end encryption

License: ISC and Apache-2.0
Group: Development/Python3
URL: https://github.com/matrix-nio/matrix-nio
# Source-url: https://github.com/matrix-nio/matrix-nio/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-aiohttp python3-module-aiofiles
BuildRequires: python3-module-h11 python3-module-h2 python3-module-jsonschema
BuildRequires: python3-module-unpaddedbase64 python3-module-pycryptodome
BuildRequires: python3-module-aiohttp-socks python3-module-atomicwrites
BuildRequires: python3-module-cachetools python3-module-peewee
BuildRequires: python3-module-vodozemac
BuildRequires: python3-module-pytest python3-module-hypothesis python3-module-faker
BuildRequires: python3-module-pytest-asyncio python3-module-pytest-benchmark
BuildRequires: python3-module-aioresponses

%description
nio is a multilayered Matrix client library. Its base layer does not
perform network I/O, while its asyncio layer uses aiohttp. It supports
end-to-end encryption, encrypted attachments and persistent key storage.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# aioresponses-ng is not packaged; the older aioresponses provides the
# shared fixture import, but cannot mock current aiohttp responses.
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -m pytest \
    --ignore=tests/async_client_test.py --benchmark-disable

%files
%doc README.md LICENSE.md apache_license.txt
%python3_sitelibdir/nio/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 10 2026 Vitaly Lipatov <lav@altlinux.ru> 0.26.0-alt1
- initial build for ALT Sisyphus

