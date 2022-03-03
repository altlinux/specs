%define _unpackaged_files_terminate_build 1
%define oname pytest-cov

%def_with check

Name: python3-module-%oname
Version: 3.0.0
Release: alt2

Summary: pytest plugin for coverage reporting with support for centralised and distributed testing
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pytest-dev/pytest-cov.git
Url: https://pypi.org/project/pytest-cov/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/shm
BuildRequires: python3(coverage)
BuildRequires: python3(fields)
BuildRequires: python3(process_tests)
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%prep
%setup
%patch -p1

grep -qsF 'time.sleep(1)' tests/test_pytest_cov.py || exit 1
sed -i 's/time\.sleep(1)/time.sleep(5)/g' tests/test_pytest_cov.py

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export PYTHONPATH_PY3=%_libdir/python3/site-packages
export TOX_TESTENV_PASSENV='PYTHONPATH_PY3'
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/pytest-cov.pth
%python3_sitelibdir/pytest_cov/
%python3_sitelibdir/pytest_cov-%version-py%_python3_version.egg-info/

%changelog
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

