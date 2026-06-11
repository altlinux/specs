Name: python3-module-holidays
Version: 0.98
Release: alt1

Summary: Holidays calculator
License: BSD
Group: Development/Python
URL: https://pypi.org/project/holidays
VCS: https://github.com/vacanza/holidays

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
A fast, efficient Python library for generating country, province and state
specific sets of holidays on the fly. It aims to make determining whether
a specific date is a holiday as fast and flexible as possible.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup tests

%build
%pyproject_build

%install
%pyproject_install

%check
scripts/l10n/generate_mo_files.py
%pyproject_run_pytest -o addopts= tests/countries

%files
%python3_sitelibdir/holidays
%python3_sitelibdir/holidays-%version.dist-info

%changelog
* Thu Jun 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.98-alt1
- 0.98 released

* Wed May 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.97-alt1
- 0.97 released

* Wed May 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.96-alt1
- 0.96 released

* Tue Apr 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.95-alt1
- 0.95 released

* Thu Apr 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.94-alt1
- 0.94 released

* Fri Feb 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.90-alt1
- 0.90 released

* Mon Dec 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.86-alt1
- 0.86 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.83-alt1
- 0.83 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.64-alt1
- 0.64 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.56-alt1
- 0.56 released

* Mon Jul 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.52-alt1
- 0.52 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.35-alt1
- 0.35 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.13-alt1
- 0.21.13 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16-alt1
- 0.16 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.2-alt1
- 0.14.2 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13-alt1
- 0.13 released

* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.3-alt1
- initial
