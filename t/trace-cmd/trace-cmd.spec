# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name:     trace-cmd
Version:  2.9.1
Release:  alt1

Summary:  A front-end for Ftrace Linux kernel internal tracer
License:  GPL-2.0 and LGPL-2.1
Group:    System/Kernel and hardware
Url:      https://trace-cmd.org/
Vcs:      https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git
# List:   https://lore.kernel.org/linux-trace-devel/
# List:   https://lore.kernel.org/linux-trace-users/
# Bugs:   https://bugzilla.kernel.org/buglist.cgi?component=Trace-cmd%%2FKernelshark&product=Tools
#
# Poorly documented.
# Presentation: https://lwn.net/Articles/410200/ (2010)
# Article: http://wrightrocket.blogspot.com/2019/07/linux-performance-tool-trace-cmd.html

Source:   %name-%version.tar
BuildRequires: asciidoc
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:BuildRequires: CUnit-devel rpm-build-vm}}

%description
The trace-cmd(1) command interacts with the Ftrace tracer that is built inside
the Linux kernel. It interfaces with the Ftrace specific files found in the
debugfs file system under the tracing directory.

%prep
%setup
sed -i s/not-a-git-repo/%version-%release/ scripts/utils.mk

%build
export CFLAGS="%optflags -D_FORTIFY_SOURCE=2 -fstack-protector-strong -fstack-check"
%make_build all doc

# No -j for these two:
%{?!_without_check:%{?!_disable_check:%make libs test}}

%install
%makeinstall \
	etcdir=%buildroot%_sysconfdir \
	install install_doc
# Note: Aren't installed: libs, python, gui (KernelShark)

%check
# Basic tests
%buildroot%_bindir/trace-cmd | grep version
%buildroot%_bindir/trace-cmd options

# Internal unit tests
export LD_LIBRARY_PATH=$PWD/lib/tracefs:$PWD/lib/traceevent:$PWD/lib/trace-cmd
vm-run --cpu=2 '
  set -xe
  utest/trace-utest
  PATH=%buildroot%_bindir:$PATH
  trace-cmd record -p function -l exit'*' true
  trace-cmd report'

%files
%doc COPYING COPYING.LIB DCO README
%_bindir/trace-cmd
%_sysconfdir/bash_completion.d/trace-cmd.bash
%_man1dir/*.1*
%_man5dir/*.5*
%_libdir/traceevent

%changelog
* Thu Jul 23 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt1
- Update to trace-cmd-v2.9.1 (2020-07-22).

* Mon Jul 20 2020 Vitaly Chikunov <vt@altlinux.org> 2.9-alt1
- Import of trace-cmd-v2.9 (2020-07-17).
- Add some testing into %%check section.

* Sat Sep 07 2019 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt1
- First build of trace-cmd. (Experimental).
