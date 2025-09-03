%define oname mdit-plugins
%define mname mdit_py_plugins
%define pypi_name mdit-py-plugins

%def_with check

Name: python3-module-%oname
Version: 0.5.0
Release: alt1
Summary: Collection of core plugins for markdown-it-py 
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/mdit-py-plugins
VCS: https://github.com/executablebooks/mdit-py-plugins

BuildArch: noarch

Source: %name-%version.tar

Provides: python3-module-%pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-markdown-it-py
BuildRequires: python3-module-pytest-regressions
%endif

%description
Collection of core plugins for markdown-it-py.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject
%pyproject_run_pytest -ra tests

%files
%doc LICENSE README.md
%python3_sitelibdir/%mname/
%python3_sitelibdir/%{pyproject_distinfo %mname}

%changelog
* Wed Sep 03 2025 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Automatically updated to 0.5.0 (Closes: #55825).

* Wed Sep 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.2-alt1
- Automatically updated to 0.4.2.

* Tue May 14 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Automatically updated to 0.4.1.

* Tue Jul 11 2023 Andrey Limachko <liannnix@altlinux.org> 0.4.0-alt1
- 0.3.5 -> 0.4.0

* Fri Mar 03 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.5-alt1
- Automatically updated to 0.3.5.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.4-alt1
- Automatically updated to 0.3.4.

* Fri Dec 09 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1
- Automatically updated to 0.3.3.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Automatically updated to 0.3.1.

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1
- Automatically updated to 0.3.0.

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.8-alt1
- Initial build for ALT.
