%define _unpackaged_files_terminate_build 1
%define pypi_name remote-pdb
%define module_name remote_pdb

# Tests are broken - https://github.com/ionelmc/python-remote-pdb/pull/27#issuecomment-705780493
%def_without check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: Remote vanilla PDB (over TCP sockets)
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/remote-pdb/
Vcs: https://github.com/ionelmc/python-remote-pdb

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: /proc
BuildRequires: rpm-build-vm
BuildRequires: /dev/kvm
%add_pyproject_deps_check_filter pytest-travis-fold
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Remote vanilla PDB (over TCP sockets) done right: no extras, proper handling
around connection failures and CI. Based on pdbx.

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
vm-run '%pyproject_run_pytest'

%files
%doc README.rst CHANGELOG.rst LICENSE
%python3_sitelibdir/__pycache__/%{module_name}*
%python3_sitelibdir/%module_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 30 2023 Vladislav Glinkin <smasher@altlinux.org> 2.1.0-alt1
- Initial build for ALT

