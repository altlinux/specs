# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    drgn
Version: 0.0.21
Release: alt1
Summary: Scriptable debugger library
License: GPL-3.0-or-later
Group:   Development/Debuggers
URL:     https://drgn.readthedocs.io
Vcs:     https://github.com/osandov/drgn
# Docs:  https://drgn.readthedocs.io/en/latest/
# Press: https://lwn.net/Articles/789641/
# Conf:  https://linuxplumbersconf.org/event/4/contributions/440/
# Refs:  https://www.kernel.org/doc/html/latest/bpf/drgn.html
Provides: python-module-drgn

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: bzip2-devel
BuildRequires: flex
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libgomp-devel
BuildRequires: libkdumpfile-devel
BuildRequires: liblzma-devel
BuildRequires: libstdc++-devel
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc}}
# Note: Bundled with own version of elfutils.

%description
drgn (pronounced "dragon") is a debugger with an emphasis on programmability.
drgn exposes the types and variables in a program for easy, expressive
scripting in Python. For example, you can debug the Linux kernel.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
test -d /proc/self
# Build-in tests (require /proc)
%__python3 setup.py test

# Simple test
export PYTHONPATH=%buildroot%python3_sitelibdir
%buildroot%_bindir/drgn --version

%files
%doc COPYING README.rst
%_bindir/drgn
%python3_sitelibdir/drgn*
%python3_sitelibdir/_drgn.*

%changelog
* Wed Nov 23 2022 Vitaly Chikunov <vt@altlinux.org> 0.0.21-alt1
- Update to v0.0.21 (2022-10-12).

* Sun Dec 26 2021 Vitaly Chikunov <vt@altlinux.org> 0.0.16-alt1
- Updated to v0.0.16 (2021-12-09).
- Built on all architectures.

* Sun Jun 20 2021 Vitaly Chikunov <vt@altlinux.org> 0.0.13-alt1
- Update to v0.0.13 (2021-06-07) -4-gc4b174a (2021-06-09).

* Thu Feb 18 2021 Vitaly Chikunov <vt@altlinux.org> 0.0.9-alt1
- Update to v0.0.9 (2021-02-17).

* Thu Dec 10 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.8-alt1
- Update to v0.0.8 (2020-11-11) -3-g5975d19 (2020-10-28).

* Tue Jul 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.7-alt1
- Update to v0.0.7 (2020-07-27).

* Wed Jun 17 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.5-alt1
- First import of v0.0.5 (2020-05-26).
