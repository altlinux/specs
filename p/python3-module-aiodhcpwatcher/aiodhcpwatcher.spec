Name: python3-module-aiodhcpwatcher
Version: 0.8.0
Release: alt1

Summary: Watch for DHCP packets with asyncio
License: GPLv3
Group: Development/Python
Url: https://github.com/bdraco/aiodhcpwatcher

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aiodhcpwatcher
%python3_sitelibdir/aiodhcpwatcher-%version.dist-info

%changelog
* Tue Mar 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.0-alt1
- 0.8.0 released

