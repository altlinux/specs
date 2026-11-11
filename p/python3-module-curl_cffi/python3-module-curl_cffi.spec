%define pypi_name curl_cffi

Name: python3-module-curl_cffi
Version: 0.17.0
Release: alt1

Summary: Python CFFI bindings for curl with browser impersonation

License: MIT
Group: Development/Python3
ExcludeArch: %ix86
URL: https://github.com/lexiforest/curl_cffi
# Source-url: https://github.com/lexiforest/curl_cffi/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch: use-system-curl-impersonate.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-cffi
BuildRequires: python3-module-certifi python3-module-pytest
BuildRequires: pkgconfig(libcurl-impersonate)

%description
Python bindings for libcurl-impersonate, with browser TLS/HTTP fingerprints
and a requests-compatible API. Uses the system libcurl-impersonate library.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# These upstream tests are offline and do not use the network/server conftest.
mkdir offline-tests check-run
cp tests/unittest/test_{headers,cookies,fingerprint_application}.py offline-tests/
export PYTHONPATH=%buildroot%python3_sitelibdir
cd check-run
python3 -m pytest -q "$OLDPWD/offline-tests"
python3 - <<'PY'
from curl_cffi import Curl
from curl_cffi.requests import Session
from curl_cffi.requests.impersonate import DEFAULT_CHROME

curl = Curl()
try:
    version = curl.version().decode()
    assert "impersonate" in version, version
    assert "BoringSSL" in version, version
    assert curl.impersonate(DEFAULT_CHROME) == 0
finally:
    curl.close()
with Session(impersonate="chrome") as session:
    assert session.impersonate == "chrome"
print(version)
PY

%files
%doc README.md LICENSE
%_bindir/curl-cffi
%python3_sitelibdir/curl_cffi/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Nov 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt1
- initial build for Sisyphus.
- exclude %%ix86: libcurl-impersonate is unavailable on this architecture.

