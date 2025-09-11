%define _unpackaged_files_terminate_build 1

%define oname fast-bitrix24

%def_with check

Name: python3-module-%oname
Version: 1.7.4
Release: alt2

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
This sphinx extension provides some useful extensions to the Sphinxs autodoc extension.
Those are
- It creates a Table of Contents in the style of the autosummary extension with
methods, classes, functions and attributes
- As you can include the __init__ method documentation for via the autoclass_content
configuration value, we provide the autodata_content configuration value to include the
documentation from the __call__ method
- You can exclude the string representation of specific objects. E.g.
if you have a large dictionary using the not_document_data configuration value.

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
* Thu Sep 11 2025 Stanislav Levin <slev@altlinux.org> 1.7.4-alt2
- NMU: fixed FTBFS (pytest 8.4.0).

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 1.7.4-alt1
- Initial build for ALT Linux

