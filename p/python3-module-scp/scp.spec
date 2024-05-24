%define _unpackaged_files_terminate_build 1
%define pypi_name scp
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.15.0
Release: alt1
Summary: scp module for paramiko
License: LGPL-2.1-or-later
Group: Development/Python3
Url: https://pypi.org/project/scp
Vcs: https://github.com/jbardin/scp.py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: openssh-server
BuildRequires: openssh-clients
%endif

%description
The scp.py module uses a paramiko transport to send and recieve files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export SCPPY_PORT=10022
./.ci/setup_ssh.sh
%pyproject_run -- python test.py

%files
%doc README.rst
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.cpython*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1
- 0.14.5 -> 0.15.0.

* Tue Apr 09 2024 Stanislav Levin <slev@altlinux.org> 0.14.5-alt1
- 0.13.6 -> 0.14.5.

* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.6-alt1.1
- NMU: moved on modern pyproject macros.

* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.13.6-alt1
- Initial build for Sisyphus.
