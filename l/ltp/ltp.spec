# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: ltp
Version: 20200515
Release: alt2

Summary: Linux Test Project
License: GPL-2.0-only
Group: Development/Tools
Url: http://linux-test-project.github.io/
Vcs: https://github.com/linux-test-project/ltp.git

Source: %name-%version.tar
BuildRequires: libacl-devel
BuildRequires: libaio-devel
BuildRequires: libcap-devel
BuildRequires: libkeyutils-devel
BuildRequires: libmm-devel
%ifnarch armh
BuildRequires: libnuma-devel
%endif
BuildRequires: libselinux-devel
BuildRequires: libssl-devel
BuildRequires: libxfs-devel

# No reqs at all, becasue there is tons of garbage.
AutoReq: off
%add_verify_elf_skiplist /usr/lib/ltp/testcases/*

%description
The Linux Test Project has a goal to deliver test suites to the open source
community that validate the reliability, robustness, and stability of Linux.

The LTP testsuite contains a collection of tools for testing the Linux kernel
and related features. Our goal is to improve the Linux kernel and system
libraries by bringing test automation to the testing effort. Interested open
source contributors are encouraged to join.

Testing Linux, one syscall at a time.

%prep
%setup

%add_optflags -Werror=implicit-function-declaration -fno-common
%add_optflags -Wno-unused-parameter -Wno-unused-result -Wno-old-style-declaration
%build
%autoreconf
%configure \
	--prefix=/usr/lib/ltp \
	--with-open-posix-testsuite \
	--with-realtime-testsuite
%make_build --output-sync=none

%install
%makeinstall_std -j%__nprocs --output-sync=none
find %buildroot/usr/lib/ltp -perm /g+w | xargs chmod g-w

# EZ-Lanucher.
mkdir -p %buildroot/%_bindir
cat > %buildroot/%_bindir/runltp <<-EOF
	#!/bin/sh
	exec /usr/lib/ltp/runltp "\$@"
EOF
chmod a+x %buildroot/%_bindir/runltp

%check
PATH=%buildroot/usr/lib/ltp/testcases/bin:$PATH
uname01
uname02
uname03
uname04

%files
%doc COPYING README.*
/usr/lib/ltp
%_bindir/runltp
%_bindir/execltp
%_man1dir/*.1.*
%_man3dir/*.3.*

%changelog
* Mon Aug 31 2020 Vitaly Chikunov <vt@altlinux.org> 20200515-alt2
- Enable Open Posix Testsuite, Realtime Testsuite, and more LTP tests.

* Sun May 17 2020 Vitaly Chikunov <vt@altlinux.org> 20200515-alt1
- Update to 20200515.

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt2
- Reduce amount of requires for tests.

* Tue Sep 03 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt1
- Initial build of LTP.
