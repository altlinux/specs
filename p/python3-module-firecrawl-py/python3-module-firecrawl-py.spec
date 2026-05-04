%define pypi_name firecrawl-py
%define mod_name firecrawl

Name: python3-module-firecrawl-py
Version: 4.24.0
Release: alt1

Summary: Python SDK for Firecrawl API

License: MIT
Group: Development/Python3
Url: https://github.com/firecrawl/firecrawl-py

# Source-url: https://files.pythonhosted.org/packages/source/f/firecrawl-py/firecrawl_py-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Firecrawl Python SDK is the official Python client library for the
Firecrawl API (firecrawl.dev). It provides scrape, crawl, map, search,
extract and batch operations for converting web content into structured
data, with both synchronous and asynchronous interfaces.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/tests
rm -rf %buildroot%python3_sitelibdir/%mod_name/__tests__

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 04 2026 Vitaly Lipatov <lav@altlinux.ru> 4.24.0-alt1
- initial build for ALT Sisyphus
