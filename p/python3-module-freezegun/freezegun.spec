%define _unpackaged_files_terminate_build 1

%define pypi_name freezegun
%def_with check

Name: python3-module-%pypi_name
Version: 1.5.5
Release: alt1.1
Summary: Let your Python tests travel through time
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/freezegun/
Vcs: https://github.com/spulec/freezegun.git
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-python-dateutil

BuildRequires: python3-modules-sqlite3
%endif

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.5.5-alt1.1
- Demodernized packaging.

* Mon Aug 11 2025 Stanislav Levin <slev@altlinux.org> 1.5.5-alt1
- 1.5.4 -> 1.5.5.

* Thu Jul 31 2025 Stanislav Levin <slev@altlinux.org> 1.5.4-alt1
- 1.5.3 -> 1.5.4.

* Mon Jul 14 2025 Stanislav Levin <slev@altlinux.org> 1.5.3-alt1
- 1.5.2 -> 1.5.3.

* Thu May 29 2025 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1
- 1.5.1 -> 1.5.2.

* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1.

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

