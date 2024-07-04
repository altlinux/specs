Name: python3-module-aiooui
Version: 0.1.6
Release: alt1

Summary: Async OUI lookups
License: MIT
Group: Development/Python
Url: https://github.com/bluetooth-devices/aiooui

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-pyproject
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(requests)

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
%python3_sitelibdir/aiooui
%python3_sitelibdir/aiooui-%version.dist-info

%changelog
* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.6-alt1
- 0.1.6 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.5-alt1
- 0.1.5 released

