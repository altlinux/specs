%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-cov

%def_with check

Name: python3-module-%pypi_name
Version: 4.0.0
Release: alt2
Summary: Pytest plugin for measuring coverage
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-cov/
Vcs: https://github.com/pytest-dev/pytest-cov
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter hunter
%pyproject_builddeps_metadata_extra testing
BuildRequires: python3-module-coverage
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

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH_PY3=%_libdir/python3/site-packages
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/pytest-cov.pth
%python3_sitelibdir/pytest_cov/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

