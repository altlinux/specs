%define        _unpackaged_files_terminate_build 1
%define        pypiname webauthn
%define        modname %pypiname
%define        distname %pypiname
%def_enable    check

Name:          python3-module-%pypiname
Version:       2.0.0
Release:       alt1
Summary:       Pythonic WebAuthn
License:       MIT
Group:         Development/Python3
Url:           https://github.com/duo-labs/py_webauthn
Vcs:           https://github.com/duo-labs/py_webauthn.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(wheel)
%if_enabled check
BuildRequires: python3(pytest)
BuildRequires: python3(cbor2)
BuildRequires: python3(cryptography)
BuildRequires: python3(OpenSSL)
BuildRequires: python3(asn1crypto)
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
%autopatch -p1

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
* Wed Jan 31 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build v2.0.0 for Sisyphus.
