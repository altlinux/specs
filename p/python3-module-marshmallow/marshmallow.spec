%def_with check

Name: python3-module-marshmallow
Version: 4.2.2
Release: alt1.1

Summary: Simplified object serialization
License: MIT
Group: Development/Python
URL: https://pypi.org/project/marshmallow
VCS: https://github.com/marshmallow-code/marshmallow

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-simplejson
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/marshmallow
%python3_sitelibdir/marshmallow-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.2.2-alt1.1
- Demodernized packaging.

* Tue Feb 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.2.2-alt1
- 4.2.2 released

* Wed Feb 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.1.2-alt1
- 4.1.2 (closes: CVE-2025-68480)

* Thu Dec 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.1.1-alt1
- 4.1.1 released

* Wed Nov 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.1.0-alt1
- 4.1.0 released

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.1-alt1
- 4.0.1 released

* Mon Feb 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.19.0-alt1
- 3.19.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.17.0-alt1
- 3.17.0 released

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.0-alt1
- initial
