%define pypi_name repology-client
%define mod_name repology_client

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.2
Release: alt1

Summary: Asynchronous wrapper for Repology API

License: EUPL-1.2
Group: Development/Python3
URL: https://git.sysrq.in/python/repology-client

# Source-url: %__pypi_url %mod_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-yarl
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-recording
%endif

%description
Asynchronous wrapper for the Repology API (repology.org), a service that
monitors package repositories of many distributions and projects.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# the suite replays recorded HTTP cassettes, no network is needed
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- initial build for Sisyphus

