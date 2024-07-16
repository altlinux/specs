%define _unpackaged_files_terminate_build 1
%define pypi_name cachetools

%def_with check

Name: python3-module-%pypi_name
Version: 5.4.0
Release: alt1
Summary: Extensible memoizing collections and decorators
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cachetools
VCS: https://github.com/tkem/cachetools
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache function
decorator.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/cachetools/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jul 16 2024 Stanislav Levin <slev@altlinux.org> 5.4.0-alt1
- 5.3.3 -> 5.4.0.

* Tue Feb 27 2024 Stanislav Levin <slev@altlinux.org> 5.3.3-alt1
- 5.3.0 -> 5.3.3.

* Thu May 25 2023 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 5.2.0 -> 5.3.0.

* Fri Dec 09 2022 Stanislav Levin <slev@altlinux.org> 5.2.0-alt1
- 3.1.1 -> 5.2.0.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1.1-alt2
- Build for python2 disabled.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20141230.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141230
- Initial build for Sisyphus

