Name: python3-module-stringcase
Version: 1.2.1
Release: alt2.1

Summary: Convert string cases between camel case, pascal case, snake case etc
License: MIT
Group: Development/Python
Url: https://pypi.org/project/stringcase
VCS: https://github.com/okunishinishi/python-stringcase

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

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
%pyproject_run_pytest stringcase_test.py

%files
%python3_sitelibdir/stringcase.*
%python3_sitelibdir/*/stringcase.*
%python3_sitelibdir/stringcase-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt2.1
- Demodernized packaging.

* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt2
- moved to pyproject

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- initial
