%define  oname mitogen

Name:    python3-module-%oname
Version: 0.2.9
Release: alt1

Summary: Distributed self-replicating programs in Python

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/dw/mitogen

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: %oname-%version.tar

Patch: remove-compat.patch

%description
Mitogen is a Python library for writing distributed self-replicating programs.

There is no requirement for installing packages, copying files around, writing
shell snippets, upfront configuration, or providing any secondary link to a
remote machine aside from an SSH connection. Due to its origins for use in
managing potentially damaged infrastructure, the remote machine need not even
have free disk space or a writeable filesystem.

It is not intended as a generic RPC framework; the goal is to provide a robust
and efficient low-level API on which tools like Salt, Ansible, or Fabric can be
built, and while the API is quite friendly and comparable to Fabric, ultimately
it is not intended for direct use by consumer software.

The focus is to centralize and perfect the intricate dance required to run
Python code safely and efficiently on a remote machine, while avoiding
temporary files or large chunks of error-prone shell scripts, and supporting
common privilege escalation techniques like sudo, potentially in combination
with exotic connection methods such as WMI, telnet, or console-over-IPMI.

%prep
%setup -n %oname-%version
%patch -p1
rm -r mitogen/compat ansible_mitogen/compat

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/ansible_%oname
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.9-alt1
- Build new version 0.2.9.

* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus.
