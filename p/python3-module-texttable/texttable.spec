%define _unpackaged_files_terminate_build 1
%define pypi_name texttable
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.1
Release: alt1

Summary: Module for creating simple ASCII tables

License: %lgpl3only
Group: Development/Python3
Url: https://pypi.org/project/texttable
Vcs: https://github.com/foutaise/texttable
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter cjkwrap
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
texttable is a module to generate a formatted text table, using ASCII characters.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests.py

%files
%python3_sitelibdir/%mod_name.*
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 15 2026 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1
- 1.7.0 -> 1.7.1

* Thu Nov 2 2023 Vladimir Didenko <cow@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.ru> 1.6.7-alt1
- 1.6.7

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Tue Jan 26 2021 Vladimir Didenko <cow@altlinux.ru> 1.6.3-alt1
- 1.6.3
- build Python 3 version only

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.3-alt1
- 0.8.3
