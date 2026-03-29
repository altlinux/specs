Name: python3-module-text-unidecode
Version: 1.3
Release: alt2.1

Summary: Python port of Text::Unidecode Perl library.
License: GPLv2
Group: Development/Python
Url: https://pypi.org/project/text-unidecode
VCS: https://github.com/kmike/text-unidecode

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test_unidecode.py

%files
%python3_sitelibdir/text_unidecode
%python3_sitelibdir/text_unidecode-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.3-alt2.1
- Demodernized packaging.

* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3-alt2
- moved to pyproject

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- initial
