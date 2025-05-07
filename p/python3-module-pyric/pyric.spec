Name: python3-module-pyric
Version: 0.1.6.4
Release: alt1.1

Summary: Python Radio Interface Controller
License: GPLv3
Group: Development/Python
Url: https://pypi.org/project/PyRIC/

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
%python3_sitelibdir/pyric
%python3_sitelibdir/%{pyproject_distinfo pyric}/

%changelog
* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.1.6.4-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.6.4-alt1
- 0.1.6.4 released
