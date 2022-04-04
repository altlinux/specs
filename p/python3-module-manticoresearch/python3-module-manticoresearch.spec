%define oname manticoresearch

Name: python3-module-manticoresearch
Version: 1.0.6
Release: alt1

Summary: Official Python client for Manticore Search

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/manticoresoftware/manticoresearch-python

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel

%description
Experimental low-level client for Manticore Search.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info/


%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Sun Jun 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt2
- initial build for ALT Sisyphus

* Mon May 24 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 1.0.5-alt1
- new version (1.0.5) with rpmgs script
