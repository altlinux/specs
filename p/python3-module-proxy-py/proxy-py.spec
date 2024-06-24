%define _unpackaged_files_terminate_build 1
%define pypi_name proxy-py
%define mod_name proxy

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.4
Release: alt1
Summary: Proxy server
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/proxy-py
Vcs: https://github.com/abhinavsingh/proxy.py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage extra dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
# required by proxy/common/pki.py
Requires: %_bindir/openssl
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# py-spy: sampling profiler for Python programs (not packaged)
%add_pyproject_deps_check_filter py-spy
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# required by proxy/common/pki.py
BuildRequires: %_bindir/openssl
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-testing.txt
%endif

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

%files
%doc README.*
%_bindir/grout
%_bindir/proxy
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/proxy.py-%version.dist-info/

%changelog
* Fri Jun 21 2024 Stanislav Levin <slev@altlinux.org> 2.4.4-alt1
- Initial build for Sisyphus.
