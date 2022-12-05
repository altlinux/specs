%define _unpackaged_files_terminate_build 1
%define pypi_name sqlitedict

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1
Summary: Persistent dict in Python, backed up by sqlite3 and pickle, multithread-safe
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/sqlitedict/
VCS: https://github.com/RaRe-Technologies/sqlitedict

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(sqlite3)
%endif

%description
A lightweight wrapper around Python's sqlite3 database, with a dict-like
interface and multi-thread access support.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
mkdir tests/db
%tox_check_pyproject -- -vra tests

%files
%doc *.rst
%python3_sitelibdir/sqlitedict.py
%python3_sitelibdir/__pycache__/sqlitedict.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Dec 05 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 1.5.0 -> 2.1.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.0-alt1
- Updated to upstream version 1.5.0.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20140727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20140727.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20140727
- Initial build for Sisyphus

