%def_with check

%define pypi_name etesync

Name: python3-module-%pypi_name
Version: 0.12.1
Release: alt1

Summary: Python client library for the legacy EteSync protocol

License: LGPL-3.0-only
Group: Development/Python3
Url: https://pypi.org/project/etesync/

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-furl
BuildRequires: python3-module-peewee
BuildRequires: python3-module-requests
BuildRequires: python3-module-vobject
%endif

# optional fallbacks, used only when hashlib has no scrypt
%add_python3_req_skip scrypt pyscrypt

%description
Python client library for EteSync servers speaking the legacy (1.0)
protocol: end-to-end encrypted and journaled sync of contacts,
calendars and tasks.

It is used by etesync-dav to access legacy EteSync accounts.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# test_service.py requires a running EteSync server on localhost:8000
%pyproject_run_pytest -v tests --ignore=tests/test_service.py

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.12.1-alt1
- initial build for Sisyphus

