Name: ltp
Version: 20180926
Release: alt2.git3ceb9157b
Summary: Linux Test Project
License: GPLv2
Group: System/Kernel and hardware
Url: http://linux-test-project.github.io/

Packager: Oleg Solovyov <mcpain@altlinux.org>

Source: %name-%version.tar.gz
Patch: alt-use-libexec.patch

%description
Linux Test Project is a joint project started by SGI, OSDL and Bull developed
and maintained by IBM, Cisco, Fujitsu, SUSE, Red Hat, Oracle and others.
The project goal is to deliver tests to the open source community that validate
the reliability, robustness, and stability of Linux.

The LTP testsuite contains a collection of tools for testing the Linux kernel
and related features. Our goal is to improve the Linux kernel and system
libraries by bringing test automation to the testing effort. Interested open
source contributors are encouraged to join.

%prep
%setup
%patch -p1

%build
make autotools
./configure CFLAGS=""
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d/
echo "%_prefix/libexec/ltp/testcases/data/ldd01" > %buildroot%_sysconfdir/ld.so.conf.d/%name-%_arch.conf

mkdir -p %buildroot%_bindir/
cd %buildroot%_prefix/
ln -s ../libexec/ltp/testcases/bin/oom01 bin/

%files
%_sysconfdir/ld.so.conf.d/%name-%_arch.conf
%_prefix/libexec/ltp/
%_bindir/oom01

%changelog
* Mon Dec 17 2018 Oleg Solovyov <mcpain@altlinux.org> 20180926-alt2.git3ceb9157b
- disable debuginfo

* Mon Dec 03 2018 Oleg Solovyov <mcpain@altlinux.org> 20180926-alt1.git3ceb9157b
- first build for ALT

