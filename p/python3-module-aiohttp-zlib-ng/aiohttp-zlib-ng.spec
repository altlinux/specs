Name: python3-module-aiohttp-zlib-ng
Version: 0.3.2
Release: alt1

Summary: Enable zlib_ng on aiohttp
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohttp-zlib-ng/

Requires: python3(zlib_ng)

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(aiohttp)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(zlib_ng)

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
%python3_sitelibdir/aiohttp_zlib_ng
%python3_sitelibdir/aiohttp_zlib_ng-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.2-alt1
- 0.3.2 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released
