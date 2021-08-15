%define oname diskcache

Name: python3-module-diskcache
Version: 5.2.1
Release: alt1

Summary: Disk Cache -- Disk and file backed persistent cache

License: MIT
Group: Development/Python3
Url: http://www.grantjenks.com/docs/diskcache/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-modules-sqlite3

%description
DiskCache is an Apache2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- initial build for ALT Sisyphus
