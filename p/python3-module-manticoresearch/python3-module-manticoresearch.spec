%define oname manticoresearch

Name: python3-module-manticoresearch
Version: 11.0.0
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
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Experimental low-level client for Manticore Search.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 11.0.0-alt1
- new version 11.0.0

* Thu Dec 26 2025 Vitaly Lipatov <lav@altlinux.ru> 9.0.0-alt1
- new version 9.0.0
- switch to pyproject_build

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Sun Jun 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt2
- initial build for ALT Sisyphus

* Mon May 24 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 1.0.5-alt1
- new version (1.0.5) with rpmgs script
