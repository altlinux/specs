%define oname AuthEncoding

Name: python3-module-AuthEncoding
Version: 4.2.1
Release: alt1

Summary: Framework for handling LDAP style password hashes.

Group: Development/Python3
License: LGPL-3.0
Url: https://pypi.org/project/AuthEncoding/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%description
AuthEncoding is a framework for handling LDAP style password hashes.
It is used in Zope but does not depend on any other Zope package.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/


%changelog
* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- initial build for ALT Sisyphus
