Name: python3-module-aiohttp-fast-url-dispatcher
Version: 0.3.1
Release: alt1

Summary: A faster URL dispatcher for aiohttp
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohttp-fast-url-dispatcher/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(aiohttp)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-asyncio)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/aiohttp_fast_url_dispatcher
%python3_sitelibdir/aiohttp_fast_url_dispatcher-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.1-alt1
- 0.3.1 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released
