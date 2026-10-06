%define  srcname cachelib

Name:    python3-module-%srcname
Version: 0.17.0
Release: alt1

Summary: A collection of cache libraries in the same API interface
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/pallets-eco/cachelib

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_disabled check
%else
BuildRequires: /proc
BuildRequires: memcached
BuildRequires: redis
BuildRequires: python3-module-pylibmc
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xprocess
BuildRequires: python3-module-redis-py
%endif

BuildArch: noarch

# Source-url: https://github.com/pallets-eco/cachelib/archive/refs/tags/%version.tar.gz
Source: %srcname-%version.tar

%description
%summary.

%prep
%setup -n %srcname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
# redis-server is in /usr/sbin
export PATH=$PATH:%_sbindir
# MongoDB, DynamoDB and Valkey backends need servers not available here
%pyproject_run_pytest -v \
    --ignore=tests/test_mongodb_cache.py \
    --ignore=tests/test_dynamodb_cache.py \
    --ignore=tests/test_valkey_cache.py

%files
%python3_sitelibdir/%srcname/
%python3_sitelibdir/%{pyproject_distinfo %srcname}/
%doc *.md

%changelog
* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 0.17.0-alt1
- NMU: new version 0.17.0 (needed by flask-caching 2.5)
- build with pyproject (flit-core), enable tests

* Sat May 31 2025 Andrey Limachko <liannnix@altlinux.org> 0.13.0-alt1
- new version (0.13.0) with rpmgs script

* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
