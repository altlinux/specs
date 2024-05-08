Name: python3-module-aiohttp-isal
Version: 0.3.1
Release: alt1

Summary: isal support for aiohttp
License: Apache-2.0
Group: Development/Python
Url: https://github.com/bdraco/aiohttp-isal

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry.core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aiohttp_isal
%python3_sitelibdir/aiohttp_isal-%version.dist-info

%changelog
* Wed May 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.1-alt1
- 0.3.1 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
