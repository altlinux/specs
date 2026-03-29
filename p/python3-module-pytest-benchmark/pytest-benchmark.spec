%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-benchmark
%define mod_name pytest_benchmark

%def_with check

Name: python3-module-%pypi_name
Version: 5.2.3
Release: alt1.1
Summary: pytest fixture for benchmarking code
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/pytest-benchmark/
Vcs: https://github.com/ionelmc/pytest-benchmark
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-aspectlib
BuildRequires: python3-module-elasticsearch
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-nbmake
BuildRequires: python3-module-pygal
BuildRequires: python3-module-pytest-instafail

BuildRequires: python3-module-py-cpuinfo
BuildRequires: python3-module-pytest
# required for some tests
BuildRequires: /usr/bin/git
%endif

%description
A pytest fixture for benchmarking code.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py3
done

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst CHANGELOG.rst
%_bindir/py.test-benchmark.py3
%_bindir/pytest-benchmark.py3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.2.3-alt1.1
- Demodernized packaging.

* Fri Nov 14 2025 Stanislav Levin <slev@altlinux.org> 5.2.3-alt1
- 5.1.0 -> 5.2.3.

* Tue Nov 05 2024 Stanislav Levin <slev@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Tue Oct 29 2024 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.0.0 -> 5.0.0.

* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 4.0.0-alt2
- Fixed FTBFS (Python 3.11).

* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 3.4.1 -> 4.0.0.

* Tue Mar 01 2022 Stanislav Levin <slev@altlinux.org> 3.4.1-alt2
- Fixed FTBFS (Pytest 7).

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.2.3 -> 3.4.1.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 3.2.3-alt2
- Fixed FTBFS.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 3.2.3-alt1
- 3.2.2 -> 3.2.3.

* Tue Dec 17 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt5
- Fixed testing against Pytest 5.3.2.

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt4
- Fixed testing against Pytest 5.2.

* Thu Aug 22 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt3
- Fixed testing against Pytest 5.1.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt2
- Fixed testing against Pytest 5.

* Wed May 29 2019 Stanislav Levin <slev@altlinux.org> 3.2.2-alt1
- 3.1.1 -> 3.2.2.

* Thu Dec 20 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt2
- Fixed build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.1-alt1
- Updated to upstream version 3.1.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.git20141219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1.git20141219.1
- NMU: Use buildreq for BR.

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20141219
- Initial build for Sisyphus

