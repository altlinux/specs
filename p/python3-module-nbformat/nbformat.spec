%define _unpackaged_files_terminate_build 1

%define pypi_name nbformat

%def_with check

Name: python3-module-%pypi_name
Version: 5.9.2
Release: alt1
Summary: The Jupyter Notebook format
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/nbformat
Vcs: https://github.com/jupyter/nbformat

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-nodejs-version
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-testpath
BuildRequires: python3-module-pep440
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-fastjsonschema
BuildRequires: python3-module-jupyter_core
BuildRequires: python3-modules-sqlite3
%endif

%py3_provides %pypi_name
%py3_requires traitlets jsonschema fastjsonschema jupyter_core

%description
This package contains the base implementation of the Jupyter Notebook
format, and Python APIs for working with notebooks.

%prep
%setup

# Remove useless test dependencies
sed -i '/"pre-commit",/d' pyproject.toml
sed -i '/"check-manifest",/d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v --color=no

%files
%doc README.*
%_bindir/jupyter-trust
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 02 2023 Anton Vyatkin <toni@altlinux.org> 5.9.2-alt1
- New version 5.9.2.

* Wed Jul 12 2023 Anton Vyatkin <toni@altlinux.org> 5.9.1-alt1
- New version 5.9.1.

* Tue Jun 27 2023 Anton Vyatkin <toni@altlinux.org> 5.9.0-alt1
- New version 5.9.0.

* Tue Apr 11 2023 Anton Vyatkin <toni@altlinux.org> 5.7.3-alt2
- Fix BuildRequires

* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 5.7.3-alt1
- 5.7.0 -> 5.7.3

* Sun Dec 04 2022 Anton Farygin <rider@altlinux.ru> 5.7.0-alt1
- 5.1.3 -> 5.7.0

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.3-alt1
- Updated to upstream version 5.1.3.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.7-alt1
- Updated to upstream version 5.0.7.
- Disabled build for python-2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream version 4.4.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

