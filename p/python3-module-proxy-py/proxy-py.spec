%define _unpackaged_files_terminate_build 1
%define pypi_name proxy-py
%define mod_name proxy

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.10
Release: alt1.2
Summary: Proxy server
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/proxy-py
Vcs: https://github.com/abhinavsingh/proxy.py
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# required by proxy/common/pki.py
Requires: %_bindir/openssl

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-autopep8
BuildRequires: python3-module-coverage
BuildRequires: python3-module-flake8
BuildRequires: python3-module-h2
BuildRequires: python3-module-hpack
BuildRequires: python3-module-httpx
BuildRequires: python3-module-hyperframe
BuildRequires: python3-module-mccabe
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pre-commit
BuildRequires: python3-module-pylint
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-rope
BuildRequires: python3-module-tox
BuildRequires: python3-module-wheel

# py-spy: sampling profiler for Python programs (not packaged)
# required by proxy/common/pki.py
BuildRequires: %_bindir/openssl
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
# broken with modern pytest-asyncio
# https://github.com/abhinavsingh/proxy.py/issues/1357
%pyproject_run_pytest -ra -o=addopts='' \
    --ignore=tests/http/exceptions/ \
    --ignore=tests/http/proxy/ \
    --ignore=tests/http/test_protocol_handler.py \
    --ignore=tests/http/web/test_web_server.py \
    --ignore=tests/integration/test_integration.py \
    --ignore=tests/plugin/test_http_proxy_plugins.py \
    --ignore=tests/plugin/test_http_proxy_plugins_with_tls_interception.py \
    --ignore=tests/http/test_client.py \
    --ignore=tests/test_grout.py \

%files
%doc README.*
%_bindir/grout
%_bindir/proxy
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.4.10-alt1.2
- Demodernized packaging.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 2.4.10-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 2.4.10-alt1
- 2.4.9 -> 2.4.10.

* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 2.4.9-alt1
- 2.4.8 -> 2.4.9.

* Mon Sep 23 2024 Stanislav Levin <slev@altlinux.org> 2.4.8-alt1
- 2.4.4 -> 2.4.8.

* Fri Jun 21 2024 Stanislav Levin <slev@altlinux.org> 2.4.4-alt1
- Initial build for Sisyphus.
