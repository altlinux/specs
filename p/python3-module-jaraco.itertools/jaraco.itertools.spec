%define _unpackaged_files_terminate_build 1

%define pypi_name jaraco.itertools
%define ns_name jaraco
%define mod_name itertools

%def_with check

Name: python3-module-%pypi_name
Version: 6.4.1
Release: alt1
Summary: Tools to supplement packaging Python releases
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.itertools/
Vcs: https://github.com/jaraco/jaraco.itertools
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%summary

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
%pyproject_run_pytest -ra -Wignore

%files
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name.py
%dir %python3_sitelibdir/%ns_name/__pycache__/
%python3_sitelibdir/%ns_name/__pycache__/%mod_name.*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 6.4.1-alt1
- 6.3.0 -> 6.4.1.

* Fri Jun 09 2023 Stanislav Levin <slev@altlinux.org> 6.3.0-alt1.1
- Mapped PyPI name to distro's one.

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 6.3.0-alt1
- new version 6.3.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 6.2.1-alt1
- new version 6.2.1 (with rpmrb script)

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 5.0.0-alt2
- Provided jaraco.itertools.

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt1
- initial build for ALT Sisyphus
