%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-sugar
%define mod_name pytest_sugar

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt2.1
Summary: Plugin for py.test that shows failures and errors instantly and shows a progress bar
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/pytest-sugar/
Vcs: https://github.com/Teemu/pytest-sugar/
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-termcolor
%endif

%description
pytest-sugar is a plugin for py.test that changes the default look and
feel of py.test (e.g. progressbar, show tests that fail instantly).

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra test_sugar.py

%files
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt2.1
- Demodernized packaging.

* Tue Feb 24 2026 Stanislav Levin <slev@altlinux.org> 1.1.1-alt2
- Fixed FTBFS (pytest 9).

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.0 -> 1.1.1.

* Fri Feb 02 2024 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- 0.9.7 -> 1.0.0.

* Fri Apr 28 2023 Stanislav Levin <slev@altlinux.org> 0.9.7-alt1
- 0.9.5 -> 0.9.7.

* Mon Oct 17 2022 Stanislav Levin <slev@altlinux.org> 0.9.5-alt2
- Fixed FTBFS (pip 22.3).

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 0.9.5-alt1
- 0.9.4 -> 0.9.5.

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 0.9.4-alt1
- 0.9.2 -> 0.9.4.
- Stopped Python2 package build(Python2 EOL).

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 0.9.2-alt1
- 0.9.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1.git20141126.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt1.git20141126.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141126
- Initial build for Sisyphus

