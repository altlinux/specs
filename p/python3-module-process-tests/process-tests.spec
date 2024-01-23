%define _unpackaged_files_terminate_build 1
%define oname process-tests

%def_with check

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: Tools for testing processes

License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/process-tests
VCS: https://github.com/ionelmc/python-process-tests

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-cov
%endif

%description
Testcase classes and assertions for testing processes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/process_tests.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/process_tests-%version.dist-info

%changelog
* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Build with check.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt1
- Build new version.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt2
- Drop python2 support.

* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 2.0.1 -> 2.0.2.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.2.1 -> 2.0.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20150618.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150618
- Version 1.0.0

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20140725
- Initial build for Sisyphus

