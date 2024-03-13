%define _unpackaged_files_terminate_build 1

%define oname traitlets

%def_with check

Name: python3-module-%oname
Version: 5.14.2
Release: alt1

Summary: Traitlets Python config system

License: BSD-3-Clause
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/traitlets

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(argcomplete)
BuildRequires: python3(pytest-mock)
%endif

%py3_provides %oname

%description
A configuration system for Python applications.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A configuration system for Python applications.

This package contains tests for %oname.

%prep
%setup
sed -i 's/"--color=yes",//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v --ignore tests/test_typing.py

%files
%doc README.*
%python3_sitelibdir/traitlets/
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Mar 13 2024 Anton Vyatkin <toni@altlinux.org> 5.14.2-alt1
- new version 5.14.2

* Mon Feb 26 2024 Anton Vyatkin <toni@altlinux.org> 5.14.1-alt1
- new version 5.14.1

* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 5.3.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Build new version.

* Fri Mar 19 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.5-alt1
- Build new version (Closes: #39489).
- Drop python2 support.

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.2-alt2
- Updated build and runtime dependencies.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.2-alt1
- Updated to upstream version 4.3.2.

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt1.1.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

