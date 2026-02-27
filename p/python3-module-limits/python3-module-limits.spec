%define modulename limits

%def_with check

Name: python3-module-%modulename
Version: 5.8.0
Release: alt1

Summary: Python module to implement rate limiting

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/limits
VCS: https://github.com/alisaifee/limits

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-pymemcache
BuildRequires: python3-module-pymongo
BuildRequires: python3-module-redis
BuildRequires: python3-module-valkey
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-deprecated
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-pytest-lazy-fixtures
BuildRequires: python3-module-flaky
%endif

%description
Python module to implement rate limiting using various strategies and
storage backends such as redis & memcached.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
sed -i '/-K/d' pytest.ini
%pyproject_run_pytest -k"not flaky and not memcached and not mongodb and \
              not redis and not redis_cluster and not redis_sentinel and \
              not valkey and not valkey_cluster"

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info/

%changelog
* Tue Feb 24 2026 Grigory Ustinov <grenka@altlinux.org> 5.8.0-alt1
- Automatically updated to 5.8.0.

* Thu Sep 22 2022 Danil Shein <dshein@altlinux.org> 2.7.0-alt1
- new version 2.7.0
  + migrate to pyproject macroses

* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build for ALT
