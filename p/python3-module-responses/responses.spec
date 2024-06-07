%define _unpackaged_files_terminate_build 1
%define pypi_name responses

%def_with check

Name: python3-module-%pypi_name
Version: 0.25.2
Release: alt1
Summary: A utility library for mocking out the requests Python library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/responses/
VCS: https://github.com/getsentry/responses.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%add_pyproject_deps_runtime_filter types-
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
A utility library for mocking out the `requests` Python library.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

rm -r %buildroot%python3_sitelibdir/responses/tests/

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/responses/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 07 2024 Stanislav Levin <slev@altlinux.org> 0.25.2-alt1
- 0.25.0 -> 0.25.2.

* Mon Mar 04 2024 Stanislav Levin <slev@altlinux.org> 0.25.0-alt1
- 0.24.1 -> 0.25.0.

* Wed Nov 15 2023 Stanislav Levin <slev@altlinux.org> 0.24.1-alt1
- 0.24.0 -> 0.24.1.

* Tue Nov 07 2023 Stanislav Levin <slev@altlinux.org> 0.24.0-alt1
- 0.23.3 -> 0.24.0.

* Wed Aug 02 2023 Stanislav Levin <slev@altlinux.org> 0.23.3-alt1
- 0.23.2 -> 0.23.3.

* Wed Jul 26 2023 Stanislav Levin <slev@altlinux.org> 0.23.2-alt1
- 0.23.1 -> 0.23.2.

* Mon May 22 2023 Stanislav Levin <slev@altlinux.org> 0.23.1-alt1
- 0.22.0 -> 0.23.1.

* Wed Oct 12 2022 Stanislav Levin <slev@altlinux.org> 0.22.0-alt1
- 0.21.0 -> 0.22.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1
- 0.12.0 -> 0.21.0.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version (0.12.0) with rpmgs script

* Wed Feb 12 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.9-alt1
- new version 0.10.9 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 0.3.0-alt3
- Rebuild with changed site-packages in sisyphus

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 0.3.0-alt2
- Rebuild into sisyphus

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

