%define  oname pyHanko-certvalidator
%define  mname pyhanko_certvalidator

%def_with check

Name:    python3-module-%oname
Version: 0.24.0
Release: alt1

Summary: Python library for validating X.509 certificates and paths

License: MIT
Group:   Development/Python3
URL:     https://github.com/MatthiasValvekens/certvalidator

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-asn1crypto
BuildRequires: python3-module-oscrypto
BuildRequires: python3-module-requests
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-uritools
BuildRequires: python3-module-freezegun
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
Forked from wbond/certvalidator, with patches for pyHanko.

A Python library for validating X.509 certificates or paths.
Supports various options, including: validation at a specific moment in time,
whitelisting and revocation checks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 --ignore tests/test_crl_client.py --ignore tests/test_ocsp_client.py -k"
not test_revocation_mode_hard and \
not test_revocation_mode_hard_aiohttp_autofetch and \
not test_revocation_mode_hard_async and \
not test_revocation_mode_hard_requests_autofetch and \
not test_basic_certificate_validator_tls_aia"

%files
%doc *.md
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version.dist-info

%changelog
* Mon Sep 11 2023 Grigory Ustinov <grenka@altlinux.org> 0.24.0-alt1
- Automatically updated to 0.24.0.

* Tue May 16 2023 Grigory Ustinov <grenka@altlinux.org> 0.23.0-alt1
- Automatically updated to 0.23.0.

* Mon Apr 24 2023 Grigory Ustinov <grenka@altlinux.org> 0.22.0-alt1
- Automatically updated to 0.22.0.

* Fri Feb 24 2023 Grigory Ustinov <grenka@altlinux.org> 0.20.1-alt1
- Automatically updated to 0.20.1.

* Tue Feb 07 2023 Grigory Ustinov <grenka@altlinux.org> 0.20.0-alt1
- Automatically updated to 0.20.0.

* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 0.19.8-alt1
- Automatically updated to 0.19.8.

* Sun Oct 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.19.6-alt1
- Automatically updated to 0.19.6.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.19.5-alt1
- Initial build for Sisyphus.
