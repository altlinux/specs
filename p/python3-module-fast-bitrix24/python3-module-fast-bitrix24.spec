%define _unpackaged_files_terminate_build 1

%define oname fast-bitrix24

%def_with check

Name: python3-module-%oname
Version: 1.8.14
Release: alt1

Summary: High-performance Python API wrapper for fast bulk data exchange with Bitrix24 via REST API.
License: MIT
Group: Development/Python3
Url: https://github.com/leshchenko1979/fast_bitrix24.git
BuildArch: noarch

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-tqdm
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-icontract
BuildRequires: python3-module-beartype

%if_with check
# synced to .github/workflows/full-test.yml
BuildRequires: python3(pytest)
BuildRequires: python3-module-pytest-asyncio
%endif

%description
fast_bitrix24 is a high-performance Python wrapper for the Bitrix24 REST API.
It provides synchronous and asynchronous clients, automatically batches and
parallelizes requests, and includes throttling to help comply with Bitrix24
request limits.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc *.md LICENSE
%python3_sitelibdir/*

%changelog
* Mon Oct 12 2026 Dmitry Lyalyaev <fruktime@altlinux.org> 1.8.14-alt1
- updated from 1.7.4 to 1.8.14

* Fri Feb 20 2026 Stanislav Levin <slev@altlinux.org> 1.7.4-alt3
- NMU: fixed FTBFS (pytest 9).

* Thu Sep 11 2025 Stanislav Levin <slev@altlinux.org> 1.7.4-alt2
- NMU: fixed FTBFS (pytest 8.4.0).

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 1.7.4-alt1
- Initial build for ALT Linux

