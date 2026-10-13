%define _unpackaged_files_terminate_build 1
%define pypi_name idna
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.20
Release: alt1
Summary: Internationalized Domain Names in Applications (IDNA)
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/idna/
Vcs: https://github.com/kjd/idna
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Support for Internationalized Domain Names in Applications (IDNA) and
Unicode IDNA Compatibility Processing. It supersedes the standard
library's encodings.idna, which only implements the 2003 specification,
offering broader script coverage and limiting domains with known
security vulnerabilities.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
# see .github/workflows/python-package.yml
%pyproject_deps_resync_check_pipreqfile .github/requirements/test.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%_bindir/idna
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 09 2026 Stanislav Levin <slev@altlinux.org> 3.20-alt1
- 3.18 -> 3.20

* Thu Jun 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 3.18-alt1
- NMU: new version

* Mon May 25 2026 Vladimir Didenko <cow@altlinux.org> 3.16-alt1
- New version (fixes: CVE-2026-45409)

* Wed Apr 29 2026 Vladimir Didenko <cow@altlinux.org> 3.13-alt1
- New version

* Tue Oct 14 2025 Vladimir Didenko <cow@altlinux.org> 3.11-alt1
- New version

* Thu Sep 26 2024 Vladimir Didenko <cow@altlinux.org> 3.10-alt1
- New version

* Thu Sep 12 2024 Vladimir Didenko <cow@altlinux.org> 3.8-alt1
- New version

* Mon Apr 22 2024 Vladimir Didenko <cow@altlinux.org> 3.7-alt1
- New version

* Tue Nov 28 2023 Vladimir Didenko <cow@altlinux.org> 3.6-alt1
- New version

* Thu Oct 6 2022 Vladimir Didenko <cow@altlinux.org> 3.4-alt1
- New version

* Wed Nov 3 2021 Vladimir Didenko <cow@altlinux.org> 3.3-alt1
- New version

* Fri Jun 18 2021 Vladimir Didenko <cow@altlinux.org> 3.2-alt1
- New version

* Thu Mar 4 2021 Vladimir Didenko <cow@altlinux.org> 3.1-alt1
- New version

* Fri Jul 17 2020 Vladimir Didenko <cow@altlinux.org> 2.10-alt1
- New version
- Build Python3 version as separate package

* Wed Mar 18 2020 Vladimir Didenko <cow@altlinux.org> 2.9-alt1
- New version

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.org> 2.8-alt1
- New version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 2.7-alt1
- New version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.org> 2.6-alt1
- New version

* Wed Mar 15 2017 Vladimir Didenko <cow@altlinux.org> 2.5-alt1
- New version

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 2.4-alt1
- New version

* Thu Feb 2 2017 Vladimir Didenko <cow@altlinux.org> 2.2-alt1
- New version

* Fri Jul 22 2016 Vladimir Didenko <cow@altlinux.org> 2.1-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0-alt1.1
- NMU: Use buildreq for BR.

* Sun Jun 7 2015 Vladimir Didenko <cow@altlinux.ru> 2.0-alt1
- initial build for Sisyphus
