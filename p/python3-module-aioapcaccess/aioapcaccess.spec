%def_with check

Name: python3-module-aioapcaccess
Version: 1.0.0
Release: alt1.1

Summary: Python reimplementation of apcaccess tool
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aioapcaccess
VCS: https://github.com/yuxincs/aioapcaccess

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest-asyncio
%endif

%description
%summary

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/aioapcaccess
%python3_sitelibdir/aioapcaccess-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1.1
- Demodernized packaging.

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt1
- 1.0. released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- 0.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released

