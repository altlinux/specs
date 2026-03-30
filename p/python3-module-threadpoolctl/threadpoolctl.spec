%define _unpackaged_files_terminate_build 1
%define pypi_name threadpoolctl
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.6.0
Release: alt1.1
Summary: Thread-pool Controls
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/threadpoolctl
Vcs: https://github.com/joblib/threadpoolctl
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-cython
BuildRequires: python3-module-flit
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-setuptools
%endif

%description
Python helpers to limit the number of threads used in the threadpool-backed
of common native libraries used for scientific computing and data science
(e.g. BLAS and OpenMP).

Fine control of the underlying thread-pool size can be useful in workloads
that involve nested parallelism so as to mitigate oversubscription issues.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.md CHANGES.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1.1
- Demodernized packaging.

* Fri Mar 14 2025 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.0 -> 3.6.0.

* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.4.0 -> 3.5.0.

* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.1.0 -> 3.4.0.

* Wed Mar 02 2022 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.2.0 -> 3.1.0.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.
- Enabled tests.

* Sat Jul 17 2021 Michael Shigorin <mike@altlinux.org> 2.1.0-alt2
- added explicit BR: python3-module-pip

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
