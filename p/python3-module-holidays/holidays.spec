Name: python3-module-holidays
Version: 0.56
Release: alt1

Summary: Holidays calculator
License: BSD
Group: Development/Python
Url: https://pypi.org/project/holidays/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

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
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt

%build
%pyproject_build

%install
%pyproject_install

%check
scripts/l10n/generate_mo_files.py
%pyproject_run_pytest tests/countries

%files
%python3_sitelibdir/holidays
%python3_sitelibdir/holidays-%version.dist-info

%changelog
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
