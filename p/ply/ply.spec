# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name:    ply
Version: 2.1.1
Release: alt1
Summary: Light-weight Dynamic Tracer for Linux
Group:   Development/Debuggers
License: GPL-2.0-only
Url:     https://wkz.github.io/ply/
Vcs:     https://github.com/iovisor/ply.git
# Author: https://github.com/wkz/ply
# Issues: https://github.com/wkz/ply/issues
# Issues: https://github.com/iovisor/ply/issues

Source0: %name-%version.tar
ExclusiveArch: x86_64 aarch64 armh ppc64le
BuildRequires: flex

%description
A light-weight dynamic tracer for Linux that leverages the kernel's BPF VM in
concert with kprobes and tracepoints to attach probes to arbitrary points in
the kernel.

ply follows the Little Language approach of yore, compiling ply scripts into
Linux BPF programs that are attached to kprobes and tracepoints in the kernel.
The scripts have a C-like syntax, heavily inspired by dtrace(1) and, by
extension, awk(1).

%prep
%setup
sed -i -e '/AC_INIT/c\AC_INIT(ply, %version-%release,' configure.ac
%ifarch armh
  ln -s arm.c ./src/libply/arch/armh.c
%endif
%ifarch ppc64le
  ln -s powerpc.c ./src/libply/arch/powerpc64le.c
%endif

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
LD_LIBRARY_PATH=%buildroot%_libdir %buildroot%_sbindir/ply -v

%pre
config_check() {
  local config i

  for config in /proc/config.gz /boot/config-$(uname -r) ''; do
    test -r $config && break
  done
  test -n "$config" || return
  for i do
    zcat $config | grep -qw "^CONFIG_$i" || return
  done
}
config_check BPF BPF_SYSCALL NET_CLS_BPF NET_ACT_BPF BPF_JIT BPF_EVENTS \
  || echo "Warning: your current kernel does not support BPF tracing"

%files
%_docdir/%name
%_sbindir/ply
%_includedir/ply
%_libdir/libply.*

%changelog
* Sun Jul 12 2020 Vitaly Chikunov <vt@altlinux.org> 2.1.1-alt1
- Initial import of 2.1.1 (2020-04-22) with fixes at 2.1.1-7-g059a266
  (2020-07-15).
