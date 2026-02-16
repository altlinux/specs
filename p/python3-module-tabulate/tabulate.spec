%define _unpackaged_files_terminate_build 1
%define pypi_name tabulate
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt2
Summary: Pretty-print tabular data
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tabulate/
VCS: https://github.com/astanin/python-tabulate.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Pretty-print tabular data in Python.

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
%pyproject_run_pytest -vra --doctest-modules --ignore benchmark.py

%files
%_bindir/tabulate
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 16 2026 Stanislav Levin <slev@altlinux.org> 0.9.0-alt2
- Fixed FTBFS.

* Tue Nov 08 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.9 -> 0.9.0.

* Mon Feb 14 2022 Stanislav Levin <slev@altlinux.org> 0.8.9-alt1
- 0.8.7 -> 0.8.9 (closes: #41933).

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.8.7-alt1
- 0.7.3 -> 0.8.7.
- Stopped Python2 package build.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.3-alt2
- Fixed build spec with pytest3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus

