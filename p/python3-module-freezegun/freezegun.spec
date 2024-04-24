%define _unpackaged_files_terminate_build 1

%define pypi_name freezegun
%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1
Summary: Let your Python tests travel through time
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/freezegun/
Vcs: https://github.com/spulec/freezegun.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-modules-sqlite3
%endif

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 24 2024 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.4.0 -> 1.5.0.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.2.2 -> 1.4.0.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2.

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.0 -> 1.2.1.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2
- Fixed FTBFS (Python3.10).

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.15-alt2
- Drop python2 support.

* Thu Apr 09 2020 Ivan A. Melnikov <iv@altlinux.org> 0.3.15-alt1
- 0.3.12 -> 0.3.15.

* Wed Oct 02 2019 Stanislav Levin <slev@altlinux.org> 0.3.12-alt1
- 0.3.11 -> 0.3.12.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 0.3.11-alt1
- 0.3.9 -> 0.3.11.

* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.9-alt1
- 0.3.9

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1.git20141231.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.8-alt1.git20141231.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1.git20141231.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141231
- Initial build for Sisyphus

