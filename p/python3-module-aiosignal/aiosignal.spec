Name: python3-module-aiosignal
Version: 1.3.1
Release: alt1

Summary: A project to manage callbacks in asyncio projects.
License: Apache-2.0
Group: Development/Python
Url: https://github.com/aio-libs/aiosignal

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
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
%python3_sitelibdir/aiosignal
%python3_sitelibdir/aiosignal-%version.dist-info

%changelog
* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

