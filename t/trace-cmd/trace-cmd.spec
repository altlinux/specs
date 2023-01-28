# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# Python plugin support (not the API).
# Also requires `unresolved=normal`
%def_without python

Name:     trace-cmd
Version:  3.1.2
Release:  alt2

Summary:  A front-end for Ftrace Linux kernel internal tracer
License:  GPL-2.0 and LGPL-2.1
Group:    Development/Debug
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
%if_with python
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
# else: 'python-dev is not installed, not compiling python plugins'
%endif
BuildRequires: asciidoc
BuildRequires: banner
BuildRequires: chrpath
BuildRequires: libaudit-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel
BuildRequires: libzstd-devel
BuildRequires: swig
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:BuildRequires: CUnit-devel rpm-build-vm}}

%description
The trace-cmd(1) command interacts with the Ftrace tracer that is built inside
the Linux kernel. It interfaces with the Ftrace specific files found in the
debugfs file system under the tracing directory.

%package -n libtracecmd
# Libtracecmd which is compiled from the same source have different upstream
# version numbering. But we cannot set version for sub-package.
Summary: trace-cmd libraries
Group: System/Libraries
Conflicts: trace-cmd-libs < 2.9.6-alt1

%description -n libtracecmd
%summary.

%package -n libtracecmd-devel
Summary: Development headers of libtracecmd
Group: Development/C
Requires: libtracecmd = %EVR

%description -n libtracecmd-devel
%summary.

%package -n python3-module-tracecmd
Summary: Python plugin support for libtracecmd
Group: Development/Python3
Requires: libtracecmd = %EVR
Provides: python3(tracecmd)
Obsoletes: trace-cmd-python3 < 2.9.6-alt1

%description -n python3-module-tracecmd
%summary.

%prep
%setup
sed -i s/not-a-git-repo/%version-%release/ scripts/utils.mk
sed -i 's!\(BASH_COMPLETE_DIR\) .*!\1 = %_datadir/bash-completion/completions/!' Makefile

# XXX: Temporary fix Makefiles for make 4.4 or they will infinite loop.
sed -i '/ = .*shell/s/=/:=/' Makefile

%build
%define optflags_lto %nil
%add_optflags -Wno-unused-result %(getconf LFS_CFLAGS)
export CFLAGS="%optflags -D_GNU_SOURCE"
# If libtracecmd.so is parallel-built together with all_cmd, libtracecmd.so
# will miss some functions that will be mis-linked to trace-cmd instead.
%make_build prefix=%_prefix libdir=%_libdir V=1 \
	libtracecmd.so
%make_build prefix=%_prefix libdir=%_libdir V=1 \
	PYTHON_VERS=python3 \
	all_cmd \
	doc
%{?!_without_check:%{?!_disable_check:make test}}
chrpath --delete tracecmd/trace-cmd lib/trace-cmd/libtracecmd.so

%install
banner install
export CFLAGS="%optflags -D_GNU_SOURCE"
%makeinstall_std prefix=%_prefix libdir=%_libdir V=1 \
	PYTHON_VERS=python3 \
	install \
	install_libs \
	install_doc
# Duplicating man pages.
rm -rf %buildroot%_datadir/doc/libtracecmd-doc
# GUI script not belonging to the module, requiring gobject and gtk.
rm -f %buildroot%python3_sitelibdir/%name/event-viewer.py
# There are already man pages.
rm %buildroot%_datadir/doc/%name/*.html

%check
# Basic tests
%buildroot%_bindir/trace-cmd | grep version.%version..%version-%release
%buildroot%_bindir/trace-cmd options

# Internal unit tests
export LD_LIBRARY_PATH=%buildroot%_libdir
vm-run --cpu=2 '
  set -xe
  utest/trace-utest
  PATH=%buildroot%_bindir:$PATH
  trace-cmd record -p function -l exit'*' true
  trace-cmd report'

%files
%doc COPYING README
%_bindir/trace-cmd
%_datadir/bash-completion/completions/trace-cmd.bash
%_man1dir/*.1*
%_man5dir/*.5*

%files -n libtracecmd
%doc COPYING.LIB
%_libdir/libtracecmd.so.*

%files -n libtracecmd-devel
%doc LICENSES/*
%_includedir/trace-cmd
%_libdir/libtracecmd.so
%_libdir/pkgconfig/libtracecmd.pc
%_man3dir/*tracecmd*

%if_with python
%files -n python3-module-tracecmd
%doc Documentation/README.PythonPlugin
%_libdir/%name/python
%endif

%changelog
* Sun Jan 29 2023 Vitaly Chikunov <vt@altlinux.org> 3.1.2-alt2
- spec: Fix ALT beekeeper rebuild under make 4.4.

* Tue Aug 30 2022 Vitaly Chikunov <vt@altlinux.org> 3.1.2-alt1
- Updated to trace-cmd-v3.1.2 (2022-07-14).

* Fri Mar 25 2022 Vitaly Chikunov <vt@altlinux.org> 3.0.3-alt1
- Updated to trace-cmd-v3.0.3 (2022-03-24).

* Thu Mar 24 2022 Vitaly Chikunov <vt@altlinux.org> 3.0.2-alt1
- Updated to trace-cmd-v3.0.2 (2022-03-16).

* Sat Jan 22 2022 Vitaly Chikunov <vt@altlinux.org> 2.9.6-alt1
- Updated to trace-cmd-v2.9.6 (2021-11-10).
- Use external libtraceevent and libtracefs libraries.
- Build libtracecmd package.
- Do not package python module.
- GUI (KernelShark) is not built, to be a separate package.

* Sun Dec 06 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt5
- Enable pkexec (RM#24461) in a way compatible with old cmake (for p9).

* Sat Dec 05 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt4
- Allow connect from pkexec'd process (RM#24461).

* Fri Dec 04 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt3
- Enable pkexec (RM#24461).

* Sun Sep 27 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt2
- Build kernelshark, libs, devel, and python3 packages.

* Thu Jul 23 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt1
- Update to trace-cmd-v2.9.1 (2020-07-22).

* Mon Jul 20 2020 Vitaly Chikunov <vt@altlinux.org> 2.9-alt1
- Import of trace-cmd-v2.9 (2020-07-17).
- Add some testing into %%check section.

* Sat Sep 07 2019 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt1
- First build of trace-cmd. (Experimental).
