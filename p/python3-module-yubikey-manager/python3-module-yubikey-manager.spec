%define _unpackaged_files_terminate_build 1
%define pypi_name yubikey-manager

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.1
Release: alt1

Summary: Tool for managing your YubiKey configuration
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/yubikey-manager/
Vcs: https://github.com/Yubico/yubikey-manager

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(unittest)
BuildRequires: python3(fido2)
BuildRequires: python3(click)
BuildRequires: python3(makefun)
BuildRequires: python3(OpenSSL)
BuildRequires: python3(keyring)
BuildRequires: python3(importlib-metadata)
BuildRequires: python3(jaraco.classes)
BuildRequires: python3(jeepney)
BuildRequires: python3(secretstorage)
BuildRequires: libpcsclite-devel
%endif

BuildArch: noarch

Requires: ykpers
Requires: libykpers-1
Requires: pcsc-lite-ccid

Provides: ykman

%py3_provides %pypi_name

%description
Python 3.6 (or later) library for configuring a YubiKey.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

install -pD -m0644 man/ykman.1 %buildroot%_man1dir/ykman.1

%check
%tox_check_pyproject

%files
%doc COPYING NEWS
%_bindir/*
%_man1dir/*
%python3_sitelibdir/*

%changelog
* Sun Mar 05 2023 Anton Zhukharev <ancieg@altlinux.org> 5.0.1-alt1
- 4.0.9 -> 5.0.1.
- Removed ykman subpackage.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 4.0.9-alt4
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Sat Sep 10 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt3
- add ykpers dependency

* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt2
- add pcsc-lite-ccid dependency

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt1
- initial build for Sisyphus

