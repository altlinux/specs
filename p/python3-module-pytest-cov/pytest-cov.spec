%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-cov
%define mod_name pytest_cov

%def_with check

Name: python3-module-%pypi_name
Version: 7.1.0
Release: alt1.1
Summary: Pytest plugin for measuring coverage
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-cov/
Vcs: https://github.com/pytest-dev/pytest-cov
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme

%if_with check
BuildRequires: python3-module-celery

BuildRequires: python3-module-coverage
BuildRequires: python3-module-pluggy
BuildRequires: python3-module-process-tests
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-virtualenv
%endif

%description
This plugin produces coverage reports. Compared to just using coverage run this
plugin does some extras:
- Subprocess support: you can fork or run stuff in a subprocess and will get
  covered without any fuss.
- Xdist support: you can use all of pytest-xdist's features and still get
coverage.
- Consistent pytest behavior. If you run coverage run -m pytest you will have
  slightly different sys.path (CWD will be in it, unlike when running pytest).

%prep
%setup
%patch -p1

grep -qsF 'time.sleep(1)' tests/test_pytest_cov.py || exit 1
sed -i 's/time\.sleep(1)/time.sleep(5)/g' tests/test_pytest_cov.py


%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 7.1.0-alt1.1
- Demodernized packaging.

* Mon Mar 23 2026 Stanislav Levin <slev@altlinux.org> 7.1.0-alt1
- 7.0.0 -> 7.1.0.

* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 7.0.0-alt1
- 6.3.0 -> 7.0.0.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 6.3.0-alt1
- 6.2.1 -> 6.3.0.

* Mon Jun 16 2025 Stanislav Levin <slev@altlinux.org> 6.2.1-alt1
- 6.1.1 -> 6.2.1.

* Mon Apr 07 2025 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.1.0 -> 6.1.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1
- 5.0.0 -> 6.1.0.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.1.0 -> 5.0.0.

* Thu May 25 2023 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1
- 4.0.0 -> 4.1.0.

* Thu May 18 2023 Stanislav Levin <slev@altlinux.org> 4.0.0-alt2
- Fixed FTBFS.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 3.0.0 -> 4.0.0.

* Tue Jul 26 2022 Stanislav Levin <slev@altlinux.org> 3.0.0-alt3
- Fixed FTBFS (coverage 6.3.3).

* Wed Mar 02 2022 Stanislav Levin <slev@altlinux.org> 3.0.0-alt2
- Fixed FTBFS (pytest-xdist 2.5.0).

* Mon Oct 11 2021 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.11.1 -> 3.0.0.

* Sun Apr 18 2021 Stanislav Levin <slev@altlinux.org> 2.11.1-alt1
- 2.10.1 -> 2.11.1.

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 2.10.1-alt2
- Drop python2 support.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 2.10.1-alt1
- 2.8.1 -> 2.10.1.

* Tue Oct 08 2019 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1
- 2.7.1 -> 2.8.1.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 2.7.1-alt2
- Fixed testing against Pytest 5.

* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1
- 2.6.1 -> 2.7.1.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 2.6.1-alt2
- Fixed build.

* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 2.6.1-alt1
- 2.6.0 -> 2.6.1.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.4.0 -> 2.6.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.git20150823.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.git20150823.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20150823
- Version 2.1.0

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150801
- New snapshot

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150728
- Version 2.0.0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141125
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141106
- Version 1.8.1

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.git20140822
- Initial build for Sisyphus

