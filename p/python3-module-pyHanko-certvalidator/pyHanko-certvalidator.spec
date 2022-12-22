%define  oname pyHanko-certvalidator
%define  mname pyhanko_certvalidator

%def_with check

Name:    python3-module-%oname
Version: 0.19.8
Release: alt1

Summary: Python library for validating X.509 certificates and paths

License: MIT
Group:   Development/Python3
URL:     https://github.com/MatthiasValvekens/certvalidator

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-asn1crypto
BuildRequires: python3-module-oscrypto
BuildRequires: python3-module-requests
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-uritools
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
%python3_build

%install
%python3_install

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
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info

%changelog
* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 0.19.8-alt1
- Automatically updated to 0.19.8.

* Sun Oct 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.19.6-alt1
- Automatically updated to 0.19.6.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.19.5-alt1
- Initial build for Sisyphus.
