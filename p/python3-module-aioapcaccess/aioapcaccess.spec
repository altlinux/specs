Name: python3-module-aioapcaccess
Version: 0.5.0
Release: alt1

Summary: Python reimplementation of apcaccess tool
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aioapcaccess/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-asyncio)

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/aioapcaccess
%python3_sitelibdir/aioapcaccess-%version.dist-info

%changelog
* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- 0.5.0 released

* Wed Jan 17 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released

