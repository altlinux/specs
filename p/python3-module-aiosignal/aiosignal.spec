Name: python3-module-aiosignal
Version: 1.2.0
Release: alt1

Summary: A project to manage callbacks in asyncio projects.
License: Apache-2.0
Group: Development/Python
Url: https://github.com/aio-libs/aiosignal

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/aiosignal
%python3_sitelibdir/aiosignal-%version-*-info

%changelog
* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

