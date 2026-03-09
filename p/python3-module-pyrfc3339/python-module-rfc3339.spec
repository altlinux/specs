%define pypi_name pyrfc3339

Name: python3-module-pyrfc3339
Version: 2.1.0
Release: alt1

Summary: Generate and parse RFC 3339 timestamps

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyRFC3339

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

Provides: python3-module-rfc3339 = %EVR
Obsoletes: python3-module-rfc3339

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-setuptools-scm

%description
This package contains a python library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%python3_sitelibdir/pyrfc3339/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version (2.1.0) via gear-uupdate
- switch to pyproject_build

* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- build python3 package separately

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
