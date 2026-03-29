%define _unpackaged_files_terminate_build 1
%define pypi_name remote-pdb
%define module_name remote_pdb

# Tests are broken - https://github.com/ionelmc/python-remote-pdb/pull/27#issuecomment-705780493
%def_without check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1.1

Summary: Remote vanilla PDB (over TCP sockets)
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/remote-pdb/
Vcs: https://github.com/ionelmc/python-remote-pdb

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-process-tests
BuildRequires: python3-module-pytest

BuildRequires: /proc
BuildRequires: rpm-build-vm
BuildRequires: /dev/kvm
%endif

%description
Remote vanilla PDB (over TCP sockets) done right: no extras, proper handling
around connection failures and CI. Based on pdbx.

%prep
%setup

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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.1
- Demodernized packaging.

* Wed Aug 30 2023 Vladislav Glinkin <smasher@altlinux.org> 2.1.0-alt1
- Initial build for ALT

