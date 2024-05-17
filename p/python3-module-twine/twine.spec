%define _unpackaged_files_terminate_build 1
%define pypi_name twine
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.1.0
Release: alt1
Summary: Collection of utilities for publishing packages on PyPI
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/twine/
Vcs: https://github.com/pypa/twine
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Twine is a utility for interacting with PyPI.
It provides build system independent uploads of source and binary distribution
artifacts for both new and existing projects.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
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
# some tests rely on colors in output
# (see tests/test_main.py::test_exception_handling)
export TERM=xterm
%pyproject_run_pytest -ra

%files
%doc README.*
%_bindir/*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 17 2024 Stanislav Levin <slev@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Tue May 07 2024 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.0.2 -> 5.0.0.

* Sun Feb 11 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt2
- Fixed FTBFS.

* Tue Mar 28 2023 Anton Vyatkin <toni@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt2
- build for python2 disabled

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.1-alt1
- Updated to upstream releases 1.9.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2.git20140815.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.1-alt2.git20140815
- cleanup buildreqs
- disable check

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140815
- Initial build for Sisyphus

