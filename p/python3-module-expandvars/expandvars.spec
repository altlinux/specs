Name: python3-module-expandvars
Version: 0.12.0
Release: alt1

Summary: Expand system variables Unix style
License: MIT
Group: Development/Python
Url: https://pypi.org/project/expandvars/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(hatchling)
BuildRequires: python3(pytest-cov)

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
%python3_sitelibdir/expandvars.*
%python3_sitelibdir/*/expandvars.*
%python3_sitelibdir/expandvars-%version.dist-info

%changelog
* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

