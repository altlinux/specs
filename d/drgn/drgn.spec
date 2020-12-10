# SPDX-License-Identifier: GPL-2.0-only

Name:    drgn
Version: 0.0.8
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

Source: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires(pre): rpm-build-python3
BuildRequires: git-core
BuildRequires: flex
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: liblzma-devel
BuildRequires: libgomp-devel
BuildRequires: libstdc++-devel
# BuildRequires: libkdumpfile
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc}}
# Note: Bundled with own version of elfutils.

%description
drgn (pronounced "dragon") is a debugger with an emphasis on programmability.
drgn exposes the types and variables in a program for easy, expressive
scripting in Python. For example, you can debug the Linux kernel.

%prep
%setup

%build
git init # Fool it to believe it's installing from the git
sed -i '/local_version.*unknown/s/+unknown/-%release/' setup.py
%python3_build

%install
%python3_install

%check
# Build-in tests (require /proc)
%__python3 setup.py test

# Simple test
export PYTHONPATH=%buildroot%python3_sitelibdir
%buildroot%_bindir/drgn --version

%files
%_bindir/drgn
%python3_sitelibdir/drgn*.egg-info
%python3_sitelibdir/drgn
%python3_sitelibdir/_drgn.*

%changelog
* Thu Dec 10 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.8-alt1
- Update to v0.0.8 (2020-11-11) -3-g5975d19 (2020-10-28).

* Tue Jul 28 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.7-alt1
- Update to v0.0.7 (2020-07-27).

* Wed Jun 17 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.5-alt1
- First import of v0.0.5 (2020-05-26).
