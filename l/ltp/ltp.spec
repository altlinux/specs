# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: ltp
Version: 20210524
Release: alt4

Summary: Linux Test Project
License: GPL-2.0-only
Group: Development/Tools
Url: http://linux-test-project.github.io/
Vcs: https://github.com/linux-test-project/ltp.git

Requires: ltp-alt-lists

Source: %name-%version.tar
BuildRequires: rpm-build-python3
BuildRequires: banner
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

# No Reqs at all, because there is tons of them.
# Idea is - all tests are optional, so we should not provide ready-to-go
# ability to run any tests. Install required dependencies manually just
# for the tests you want to run.
AutoReqProv: off
%add_verify_elf_skiplist /usr/lib/ltp/testcases/*

%description
The Linux Test Project has a goal to deliver test suites to the
open source community that validate the reliability, robustness,
and stability of Linux.

The LTP testsuite contains a collection of tools for testing the
Linux kernel and related features. Our goal is to improve the Linux
kernel and system libraries by bringing test automation to the testing
effort. Interested open source contributors are encouraged to join.

Testing Linux, one syscall at a time (tm).

%package open-posix-testsuite
Summary: Open POSIX Test Suite
Group: Development/Tools
AutoReqProv: off

%description open-posix-testsuite
The POSIX Test Suite is an open source test suite with the goal of
performing conformance, functional, and stress testing of the IEEE
1003.1-2001 System Interfaces specification in a manner that is
agnostic to any given implementation.

%package realtime-testsuite
Summary: Testsuite for real-time Linux
Group: Development/Tools
AutoReqProv: off

%description realtime-testsuite
Realtime tests is an open-source testsuite for testing real-time Linux.
This testsuite is maintained by the IBM Real-Time team.

%prep
%setup

# /usr/include/sys/wait.h:88:16: error: variable 'wait' redeclared as function
#    88 | extern __pid_t wait (int *__stat_loc);
# nptl01.c:58:17: note: previously declared here
#    58 | pthread_mutex_t wait;
# lto1: fatal error: errors during merging of translation units
%define optflags_lto %nil
# From LTP's travis.
%add_optflags -Werror=implicit-function-declaration -fno-common
# Just reduce amount of warnings for too old code.
%add_optflags -Wno-unused-parameter -Wno-unused-result -Wno-old-style-declaration
%build
%autoreconf
%configure --prefix=/usr/lib/ltp
banner ltp
%make_build --output-sync=none
banner posix
%make_build --output-sync=none -C testcases/open_posix_testsuite
banner rt
cd testcases/realtime
%autoreconf
%configure --prefix=/usr/lib/realtime_testsuite
%make_build
cd ../..

%install
%makeinstall_std -s -j%__nprocs --output-sync=none
mkdir -p %buildroot/usr/lib/openposix_testsuite/bin
%makeinstall_std -s --output-sync=none -C testcases/open_posix_testsuite prefix=/usr/lib/openposix_testsuite
%makeinstall_std -s --output-sync=none -C testcases/realtime prefix=/usr/lib/realtime_testsuite
find %buildroot/usr/lib/{ltp,openposix_testsuite,realtime_testsuite} -perm /g+w | xargs chmod g-w
# Create output dirs (will have tmp-like permissions).
mkdir %buildroot/usr/lib/ltp/{output,results}
# EZ-Lanucher for LTP.
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
uname04

%post
if [ -d /.host -a -d /.in -a -d /.out ]; then
	chmod 1777 /usr/lib/ltp/{output,results}
fi

%files
%doc COPYING README.*
/usr/lib/ltp
%_bindir/runltp
%_bindir/execltp
%_man1dir/*.1.*
%_man3dir/*.3.*

%files open-posix-testsuite
%doc testcases/open_posix_testsuite/{AUTHORS,README,COPYING,NEWS,QUICK-START}
%doc testcases/open_posix_testsuite/Documentation
/usr/lib/openposix_testsuite

%files realtime-testsuite
%doc testcases/realtime/{00_Descriptions.txt,README,COPYING,doc}
/usr/lib/realtime_testsuite

%changelog
* Thu Aug 26 2021 Vitaly Chikunov <vt@altlinux.org> 20210524-alt4
- spec: Disable build with LTO.

* Fri Jul 23 2021 Vitaly Chikunov <vt@altlinux.org> 20210524-alt3
- Move ALT specific lists into ltp-alt-lists.

* Tue Jul 06 2021 Vitaly Chikunov <vt@altlinux.org> 20210524-alt2
- Add testcases list kernel-alt-vm and skiplist-alt-vm.

* Mon May 31 2021 Vitaly Chikunov <vt@altlinux.org> 20210524-alt1
- Update to 20210524.
- spec: Split into multiple packages.

* Sat May 01 2021 Vitaly Chikunov <vt@altlinux.org> 20210121-alt2
- spec: Disable AutoReqProv.

* Sun Jan 24 2021 Vitaly Chikunov <vt@altlinux.org> 20210121-alt1
- Update to 20210121.

* Thu Oct 29 2020 Vitaly Chikunov <vt@altlinux.org> 20200930-alt1
- Update to 20200930.
- spec: Pre-create output directories.

* Mon Aug 31 2020 Vitaly Chikunov <vt@altlinux.org> 20200515-alt2
- Enable Open Posix Testsuite, Realtime Testsuite, and more LTP tests.

* Sun May 17 2020 Vitaly Chikunov <vt@altlinux.org> 20200515-alt1
- Update to 20200515.

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt2
- Reduce amount of requires for tests.

* Tue Sep 03 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt1
- Initial build of LTP.
