%define _unpackaged_files_terminate_build 1

%define pypi_name pytest-mpi
%define mod_name pytest_mpi

%def_with check

Name: python3-module-%pypi_name
Version: 0.6
Release: alt1
Summary: Pytest plugin for working with MPI
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pytest-mpi/
Vcs: https://github.com/aragilar/pytest-mpi
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# doc tests
BuildRequires: python3-module-sybil
# mpirun
BuildRequires: openmpi
# required by mpi; plm_rsh_agent: ssh : rsh
BuildRequires: /usr/bin/rsh
%endif

%description
pytest_mpi is a plugin for pytest providing some useful tools
when running tests under MPI, and testing MPI-related code.

%prep
%setup

sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	./src/pytest_mpi/_version.py
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
# mpirun is shipped on /usr/lib64/openmpi/bin/mpirun (x86_64)
export PATH=$PATH:%_libdir/openmpi/bin
%pyproject_run_pytest -ra -Wignore -p pytester --runpytest=subprocess

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 21 2023 Stanislav Levin <slev@altlinux.org> 0.6-alt1
- 0.5 -> 0.6.

* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1
- Initial build for ALT.
