%define  modulename cssselect2

%def_with check

Name:    python3-module-%modulename
Version: 0.7.0
Release: alt1

Summary: CSS selectors for Python ElementTree
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/cssselect2
Vcs:     https://github.com/Kozea/cssselect2

BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-webencodings
BuildRequires: python3-module-tinycss2
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Thu May 02 2024 Anton Vyatkin <toni@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Mon Aug 05 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1.1
- NMU: Little spec refactoring.

* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.1-alt1
- Initial build for ALT
