%define _unpackaged_files_terminate_build 1
%define oname pytest-benchmark

%def_with check

Name: python3-module-%oname
Version: 3.4.1
Release: alt2
Summary: pytest fixture for benchmarking code
License: BSD-2-Clause
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pytest-benchmark/

# https://github.com/ionelmc/pytest-benchmark.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(pytest)
BuildRequires: python3(cpuinfo)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)

BuildRequires: python3(aspectlib)
BuildRequires: python3(elasticsearch)
BuildRequires: python3(freezegun)
BuildRequires: python3(pygal)
BuildRequires: /usr/bin/git
%endif

%py3_requires cpuinfo

# PEP503 name
%py3_provides %oname

%description
A pytest fixture for benchmarking code.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}.py3
done

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}-nocov
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.rst CHANGELOG.rst
%_bindir/py.test-benchmark.py3
%_bindir/pytest-benchmark.py3
%python3_sitelibdir/pytest_benchmark/
%python3_sitelibdir/pytest_benchmark-%version-py%_python3_version.egg-info/

%changelog
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

