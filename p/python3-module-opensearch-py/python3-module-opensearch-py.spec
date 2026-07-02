%global _unpackaged_files_terminate_build 1
%global pypi_name opensearch-py
%global module_name opensearchpy
%def_with check

Name: python3-module-opensearch-py
Version: 3.2.0
Release: alt1
Summary: Python Client for OpenSearch
License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/opensearch-py
VCS: https://github.com/opensearch-project/opensearch-py

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-events
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-urllib3
%endif

%description
opensearch-py is a community-driven, open source fork
of elasticsearch-py licensed under the Apache v2.0 License.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests needed opensearch server to use
%pyproject_run_pytest \
	--ignore=test_opensearchpy/test_server \
	--ignore=test_opensearchpy/test_async/test_server \
	--ignore=test_opensearchpy/test_async/test_aiohttp.py \
	--ignore=test_opensearchpy/test_async/test_connection.py \
	--ignore=test_opensearchpy/test_async/test_signer.py \
	--ignore=test_opensearchpy/test_connection

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo opensearch_py}

%changelog
* Thu Jul 02 2026 Alexander Makeenkov <amakeenk@altlinux.org> 3.2.0-alt1
- Initial build for ALT.

