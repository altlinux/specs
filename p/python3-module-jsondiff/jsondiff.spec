%define _unpackaged_files_terminate_build 1
%define pypi_name jsondiff
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1
Summary: Diff JSON and JSON-like structures in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jsondiff/
Vcs: https://github.com/xlwings/jsondiff
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
Conflicts: jdiff
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
Diff JSON and JSON-like structures in Python.

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
# .github/workflows/pr_check.yml
%pyproject_run_pytest -vra

%files
%doc README.*
%_bindir/jdiff
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 23 2024 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.0.0 -> 2.2.1.

* Mon May 22 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)
- add conflicts: jdiff (ALT bug 41297)

* Wed Apr 12 2023 Anton Vyatkin <toni@altlinux.org> 1.3.0-alt2
- Fix BuildRequires

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus
