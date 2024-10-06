%define _unpackaged_files_terminate_build 1
%define oname pytest-regtest

%def_with check

Name: python3-module-%oname
Version: 2.2.1
Release: alt1

Summary: pytest plugin for regression tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-regtest

Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pandas
%endif

%py3_provides pytest_regtest
%add_python3_req_skip  pandas numpy

%description
pytest-regtest is a pytest-plugin for implementing regression tests. Compared
to functional testing a regression test does not test if software produces
correct results, instead a regression test checks if software behaves the same
way as it did before introduced changes.

%prep
%setup -q -n %{oname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v tests/

%files
%doc README.*
%python3_sitelibdir/pytest_regtest
%python3_sitelibdir/pytest_regtest-%version.dist-info

%changelog
* Sun Oct 06 2024 Anton Vyatkin <toni@altlinux.org> 2.2.1-alt1
- new version 2.2.1

* Thu Oct 03 2024 Anton Vyatkin <toni@altlinux.org> 2.2.0-alt1
- new version 2.2.0

* Mon Mar 04 2024 Anton Vyatkin <toni@altlinux.org> 2.1.1-alt1
- new version 2.1.1

* Fri Aug 18 2023 Anton Vyatkin <toni@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Mon Feb 27 2023 Anton Vyatkin <toni@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.15.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.15.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141120
- Version 0.4.1

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141114
- Initial build for Sisyphus

