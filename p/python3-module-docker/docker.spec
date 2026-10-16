%define _unpackaged_files_terminate_build 1
%define pypi_name docker
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 7.2.0
Release: alt1

Summary: Python client for Docker

License: %asl
Group: Development/Python3
Url: https://pypi.org/project/docker
Vcs: https://github.com/docker/docker-py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra ssh
%pyproject_builddeps_metadata_extra dev
%endif

%description
An API client for docker written in Python

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/ci.yml
%pyproject_run_pytest -vra tests/unit

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 16 2026 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- 7.1.0 -> 7.2.0

* Thu May 30 2024 Vladimir Didenko <cow@altlinux.ru> 7.1.0-alt1
- 7.1.0

* Wed Jan 24 2024 Vladimir Didenko <cow@altlinux.ru> 7.0.0-alt1
- 7.0.0

* Thu Jun 22 2023 Vladimir Didenko <cow@altlinux.ru> 6.1.3-alt1
- 6.1.3

* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Mon Dec 6 2021 Vladimir Didenko <cow@altlinux.ru> 5.0.3-alt1
- 5.0.3

* Tue Sep 28 2021 Vladimir Didenko <cow@altlinux.ru> 5.0.2-alt1
- 5.0.2

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Thu Mar 11 2021 Vladimir Didenko <cow@altlinux.ru> 4.4.4-alt1
- 4.4.4

* Fri Dec 4 2020 Vladimir Didenko <cow@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Wed Sep 9 2020 Vladimir Didenko <cow@altlinux.ru> 4.3.1-alt1
- 4.3.1
- Build Python3 version as separate package

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Tue Jun 23 2020 Vladimir Didenko <cow@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Wed Mar 11 2020 Vladimir Didenko <cow@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Thu Oct 17 2019 Vladimir Didenko <cow@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.ru> 3.7.2-alt1
- 3.7.2

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.ru> 3.5.1-alt1
- 3.5.1

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.ru> 3.1.4-alt1
- 3.1.4

* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 1.10.6-alt1
- 1.10.6

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Wed Aug 3 2016 Vladimir Didenko <cow@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0
