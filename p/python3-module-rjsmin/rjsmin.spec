%define _unpackaged_files_terminate_build 1
%define pypi_name rjsmin
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.5
Release: alt1.1
Summary: Javascript Minifier
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/rjsmin/
Vcs: https://github.com/ndparker/rjsmin
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-invoke
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
%endif

%description
rJSmin is a javascript minifier written in python.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore tests

%files
%doc README.md
%python3_sitelibdir/_%mod_name.cpython-*.so
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.cpython-*.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.5-alt1.1
- Demodernized packaging.

* Thu Dec 04 2025 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1
- 1.2.4 -> 1.2.5.

* Mon Feb 17 2025 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1
- 1.2.3 -> 1.2.4.

* Mon Oct 14 2024 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- 1.2.2 -> 1.2.3.

* Thu Oct 05 2023 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2.

* Wed May 24 2023 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.0 -> 1.2.1.

* Thu Jul 02 2020 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.12 -> 1.1.0.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.12-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.12-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt3.git20141116.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 1.0.10-alt3.git20141116
- Python compilation for 3.5.

* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.10-alt2.git20141116
- Documentation creation disabled

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20141116
- Initial build for Sisyphus

