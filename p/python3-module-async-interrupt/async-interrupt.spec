Name: python3-module-async-interrupt
Version: 1.1.2
Release: alt1

Summary: Interrupt context manager for asyncio. 
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/async-interrupt/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(pytest-cov)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc LICENSE* README*
%python3_sitelibdir/async_interrupt
%python3_sitelibdir/async_interrupt-%version.dist-info

%changelog
* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt1
- 1.1.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- 1.1.1 released

