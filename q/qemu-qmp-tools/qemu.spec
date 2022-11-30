# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: qemu-qmp-tools
Version: 7.1.0
Release: alt1.qmp
Summary: QEMU qmp-shell and other tools
License: GPL-2.0-or-later and MIT
Group: Development/Debug
Url: https://www.qemu.org
Provides: python3-module-qemu
Requires: python3-module-fuse

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%description
Tools for communicating with QEMU Monitor Protocol (QMP) servers.

- qmp-shell: Low-level QEMU shell on top of QMP.
- qom-fuse: QEMU Object Model FUSE filesystem tool.

%prep
%setup

%build
cd python
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
cd python
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%files
%_bindir/qemu-ga-client
%_bindir/qmp-*
%_bindir/qom*
%python3_sitelibdir_noarch/qemu*

%changelog
* Sun Nov 27 2022 Vitaly Chikunov <vt@altlinux.org> 7.1.0-alt1.qmp
- First build v7.1.0 (2022-08-30).
