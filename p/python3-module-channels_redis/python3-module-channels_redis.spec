%define pypi_name channels_redis

%def_with check

Name:    python3-module-%pypi_name
Version: 4.3.0
Release: alt1

Summary: Provides Django Channels channel layers that use Redis
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/django/channels_redis

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-channels
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-async-timeout
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-msgpack
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v \
    --ignore=tests/test_core.py \
    --ignore=tests/test_sentinel.py \
    --ignore=tests/test_pubsub.py \
    --ignore=tests/test_pubsub_sentinel.py

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 18 2026 Nikita Panov <nexxy@altlinux.org> 4.3.0-alt1
- Initial build for Sisyphus.


