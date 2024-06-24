%define _unpackaged_files_terminate_build 1
%define pypi_name dkimpy
%define mod_name dkim

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.7
Release: alt1
Summary: Python 3 module for DKIM and ARC signing and verification
License: BSD-2-Clause
Group: Development/Python
Url: https://pypi.org/project/dkimpy/
Vcs: https://git.launchpad.net/dkimpy
BuildArch: noarch
Source0: %name-%version.tar
Patch0: 0001-Don-t-rely-on-relative-import.patch
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# dkim/dknewkey.py
Requires: /usr/bin/openssl
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
# dkim/dknewkey.py
BuildRequires: /usr/bin/openssl
%endif

%description
Python 3 module that implements DKIM (DomainKeys Identified Mail) email signing
and verification as well as ARC (Authenticated Received Chain) signing and
verification. Supports both RSA and Ed25519 signing and verification.
It also provides helper scripts for key generation and command line signing and
verification.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python -m unittest dkim.tests.test_suite

%files
%doc ChangeLog README.md LICENSE
%_bindir/*
%_man1dir/*.1*
%python3_sitelibdir/%mod_name/
%exclude %python3_sitelibdir/%mod_name/__main__.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 24 2024 Stanislav Levin <slev@altlinux.org> 1.1.7-alt1
- 1.1.6 -> 1.1.7.

* Mon Apr 15 2024 Stanislav Levin <slev@altlinux.org> 1.1.6-alt1
- 1.0.5 -> 1.1.6.

* Thu Mar 11 2021 Stanislav Levin <slev@altlinux.org> 1.0.5-alt2
- Fixed wrong auto-generated dependency on python3(tests).

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Fri Jul 24 2020 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Sep 05 2019 Anton Farygin <rider@altlinux.ru> 0.9.3-alt1
- first build for ALT

