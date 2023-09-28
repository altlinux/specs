%define _unpackaged_files_terminate_build 1
%define pypi_name zipp

%def_with check

Name: python3-module-%pypi_name
Version: 3.17.0
Release: alt1

Summary: A pathlib-compatible Zipfile object wrapper

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/zipp/
VCS: https://github.com/jaraco/zipp.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
A pathlib-compatible Zipfile object wrapper.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.rst
%python3_sitelibdir/zipp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 27 2023 Stanislav Levin <slev@altlinux.org> 3.17.0-alt1
- 3.16.2 -> 3.17.0.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 3.16.2-alt1
- 3.15.0 -> 3.16.2.

* Fri Jun 09 2023 Stanislav Levin <slev@altlinux.org> 3.15.0-alt2
- Modernized packaging.

* Mon Feb 27 2023 Stanislav Levin <slev@altlinux.org> 3.15.0-alt1
- 3.14.0 -> 3.15.0.

* Mon Feb 20 2023 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.11.0 -> 3.14.0.

* Wed Nov 30 2022 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.0 -> 3.11.0.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.1 -> 3.10.0.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 3.9.1-alt1
- 3.8.1 -> 3.9.1.

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1
- 3.7.0 -> 3.8.1.

* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.0 -> 3.7.0.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.1 -> 3.6.0.

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.5.0 -> 3.5.1.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 1.0.0 -> 3.5.0.
- Reenabled testing.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- NMU: build python3 module only, cleanup spec

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0.

* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.3 -> 0.4.0.

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build.
