%define _unpackaged_files_terminate_build 1

Name: python3-module-fido2
Version: 1.0.0
Release: alt2

Summary: Provides library functionality for communicating with a FIDO device over USB as well as verifying attestation and assertion signatures.
License: BSD-2-Clause Apache-2.0 MPL-2.0
Group: Development/Python3
Url: https://github.com/Yubico/python-fido2
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry-core)
BuildRequires: python3(pytest)
BuildRequires: python3(setuptools)
BuildRequires: python3(cryptography)
BuildRequires: python3(smartcard)

%description
Provides library functionality for communicating with a FIDO device over USB
as well as verifying attestation and assertion signatures.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc COPYING COPYING.APLv2 COPYING.MPLv2 NEWS
%python3_sitelibdir/*

%changelog
* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

