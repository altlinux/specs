%define pypi_name flask_caching

Name: python3-module-flask-caching
Version: 2.5.1
Release: alt2

Summary: Cache support for Flask
License: BSD-3-Clause
Group: Development/Python3

URL: https://github.com/pallets-eco/flask-caching
BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar
Patch: isolate-memcached-tests.patch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_disabled check
%else
BuildRequires: python3-module-flask
BuildRequires: python3-module-cachelib >= 0.17.0
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xprocess
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-pylibmc
BuildRequires: redis
BuildRequires: memcached
%endif

%description
Adds easy cache support to Flask.

This is a fork of the Flask-Cache extension.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# redis-server is in /usr/sbin
export PATH=$PATH:%_sbindir
%pyproject_run_pytest -v

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 08 2026 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt2
- Isolate Memcached test keys and account for server clock resolution.

* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1
- build with pyproject (flit-core), enable tests

* Thu May 22 2025 Alexander Danilov <admsasha@altlinux.org> 1.11.1-alt1
- new version 1.11.1 (Fixes: CVE-2021-33026).

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt1
- new version 1.10.1 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- build python3 package separately

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
