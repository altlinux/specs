Name: python3-module-aiohttp-session
Version: 2.12.0
Release: alt1

Summary: Sessions for aiohttp.web
License: Apache-2.0
Group: Development/Python
Url: https://github.com/aio-libs/aiohttp-session

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aiohttp_session
%python3_sitelibdir/aiohttp_session-%version.dist-info

%changelog
* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12.0-alt1
- 2.12.0 released

