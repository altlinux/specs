%define        _unpackaged_files_terminate_build 1
%define        pypiname webauthn
%define        modname %pypiname
%define        distname %pypiname
%def_enable    check

Name:          python3-module-%pypiname
Version:       3.0.1
Release:       alt1
Summary:       Pythonic WebAuthn
License:       BSD-3-Clause
Group:         Development/Python3
Url:           https://github.com/duo-labs/py_webauthn
Vcs:           https://github.com/duo-labs/py_webauthn.git

BuildArch:     noarch
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(cbor2)
BuildRequires: python3(cryptography)
BuildRequires: python3(OpenSSL)
BuildRequires: python3(pyasn1)
BuildRequires: python3(pyasn1_modules)
%endif

%description
A Python3 implementation of the server-side of the WebAuthn API focused on
making it easy to leverage the power of WebAuthn.

This library supports all FIDO2-compliant authenticators, including security
keys, Touch ID, Face ID, Windows Hello, Android biometrics...and pretty much
everything else.

Simple user session protection.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest
%pyproject_run_unittest

%files
%doc *.md
%python3_sitelibdir/%{distname}
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Sun Oct 18 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- NMU: new version 3.0.1.
- Fixed License tag (BSD-3-Clause).
- Removed unused empty Patch.
- Removed BuildRequires: python3(asn1crypto), upstream moved to pyasn1.
- Added BuildRequires: python3(pyasn1) (tests).
- Added BuildRequires: python3(pyasn1_modules) (tests).

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Wed Jan 31 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build v2.0.0 for Sisyphus.
