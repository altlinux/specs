Name: python3-module-unicode-rbnf
Version: 2.4.0
Release: alt1.1

Summary: Pure-python RBNF
License: MIT
Group: Development/Python
Url: https://pypi.org/project/unicode-rbnf
VCS: https://github.com/rhasspy/unicode-rbnf

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
A pure Python implementation of ICU's rule-based number format engine

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/unicode_rbnf
%python3_sitelibdir/unicode_rbnf-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1.1
- Demodernized packaging.

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.0-alt1
- 2.4.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released
