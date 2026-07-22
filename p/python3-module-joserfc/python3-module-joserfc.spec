%define pypi_name joserfc

Name: python3-module-%pypi_name
Version: 1.7.3
Release: alt1

Summary: The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT

License: BSD-3-Clause
Group: Development/Python3
URL: https://jose.authlib.org/
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
The ultimate Python library for JOSE RFCs, including JWS, JWE, JWK, JWA, JWT.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Jul 18 2026 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- initial build for ALT Linux Sisyphus (dep of authlib 1.7.2)
