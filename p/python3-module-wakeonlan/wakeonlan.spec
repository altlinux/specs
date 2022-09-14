Name: python3-module-wakeonlan
Version: 2.1.0
Release: alt2

Summary: Python WOL implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/wakeonlan/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
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
%python3_sitelibdir/wakeonlan.py
%python3_sitelibdir/__pycache__/wakeonlan.*
%python3_sitelibdir/wakeonlan-%version.dist-info

%changelog
* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- initial
