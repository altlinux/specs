# rt-tests is taken by perl tests for RT
Name:     trace-cmd
Version:  2.8.3
Release:  alt1

Summary:  A front-end for Ftrace Linux kernel internal tracer
License:  GPL-2.0-or-later and LGPL-2.1
Group:    System/Kernel and hardware
# git://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git
Url:      https://lwn.net/Articles/410200/

BuildRequires: asciidoc xmlto

# ExclusiveArch: %ix86 x86_64
Source:   %name-%version.tar

%description
The trace-cmd(1) command interacts with the Ftrace tracer that is built inside
the Linux kernel. It interfaces with the Ftrace specific files found in the
debugfs file system under the tracing directory.

%prep
%setup

%build
export CFLAGS="%optflags -D_FORTIFY_SOURCE=2 -fstack-protector-strong -fstack-check"
%make_build prefix=/usr V=1 all doc

%install
%makeinstall_std prefix=/usr install install_doc # install_libs

# Why these installed by trace-cmd?
rm -rf %buildroot/usr/share/kernelshark
rm -f  %buildroot/usr/share/man/man1/kernelshark.1.xz

%files
%doc COPYING COPYING.LIB DCO README
/usr/bin/trace-cmd
/etc/bash_completion.d/trace-cmd.bash
/usr/lib/trace-cmd
%_man1dir/*
%_man5dir/*
# /usr/lib/libtrace*.so
# /usr/include/trace-cmd
# /usr/share/kernelshark

%changelog
* Sat Sep 07 2019 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt1
- First build of trace-cmd. (Experimental).
