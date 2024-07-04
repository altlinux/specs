Name: python3-module-aiohttp-fast-zlib
Version: 0.1.1
Release: alt1

Summary: Another nothingburger
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/aiohttp-fast-zlib/

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
%python3_sitelibdir/aiohttp_fast_zlib
%python3_sitelibdir/aiohttp_fast_zlib-%version.dist-info

%changelog
* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.1-alt1
- 0.1.1 released

