%define _unpackaged_files_terminate_build 1
%define oname scp

%def_with check

Name: python3-module-%oname
Version: 0.13.6
Release: alt1.1

Summary: scp module for paramiko
License: LGPL-2.1-or-later
Group: Development/Python3
# Source-git: https://github.com/jbardin/scp.py.git
Url: https://pypi.org/project/scp

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires:
BuildRequires: python3(paramiko)

BuildRequires: /proc
BuildRequires: openssh-server
BuildRequires: openssh-clients
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%py3_requires paramiko

%description
The scp.py module uses a paramiko transport to send and recieve files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
allowlist_externals =
    /usr/bin/pkill
setenv =
    SCPPY_PORT = 10022
commands_pre =
    {toxinidir}/.ci/setup_ssh.sh
commands =
    python test.py
commands_post =
    - pkill -F /tmp/ssh_server/sshd.pid
EOF
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/scp.py
%python3_sitelibdir/__pycache__/scp.cpython*
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.6-alt1.1
- NMU: moved on modern pyproject macros.

* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.13.6-alt1
- Initial build for Sisyphus.
