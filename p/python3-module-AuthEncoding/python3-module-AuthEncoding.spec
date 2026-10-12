%define oname AuthEncoding

Name: python3-module-AuthEncoding
Version: 6.1
Release: alt1

Summary: Framework for handling LDAP style password hashes.

Group: Development/Python3
License: ZPL-2.1
Url: https://pypi.org/project/AuthEncoding/

# Source-url: %__pypi_url authencoding
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-bcrypt
%endif

%description
AuthEncoding is a framework for handling LDAP style password hashes.
It is used in Zope but does not depend on any other Zope package.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
%pyproject_run_pytest -v src

%files
%doc README.txt CHANGES.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt1
- new version 6.1
- switch to pyproject build
- fix License: ZPL-2.1
- enable tests

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- initial build for ALT Sisyphus
