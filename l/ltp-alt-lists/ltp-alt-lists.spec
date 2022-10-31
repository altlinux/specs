# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ltp-alt-lists
Summary: ALT specific testcase and skiplist for LTP
Version: 16
Release: alt1
License: GPL-2.0-only
Group: Development/Tools
Url: https://git.altlinux.org/gears/l/ltp-alt-lists.git

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: ltp-testsuite

%description
%summary.

Package is created to update lists without rebuilding LTP.

%prep
%setup

%install
mkdir -p %buildroot/usr/lib/ltp/runtest

# Create ALT specific testcases list.
# Run example: vm-run runltp -S skiplist-alt-vm -f kernel-alt-vm
(
  cd /usr/lib/ltp/runtest
  cat \
	syscalls \
	syscalls-ipc \
	crypto \
	connectors \
	containers \
	fs_readonly \
	ima \
	kernel_misc \
	net.features \
	numa \
	pty \
	uevent \
) >> kernel-alt-vm

install -p -m644 kernel-alt-vm   %buildroot/usr/lib/ltp/runtest/
install -p -m644 skiplist-alt-vm %buildroot/usr/lib/ltp/

%files
/usr/lib/ltp/skiplist-alt-vm
/usr/lib/ltp/runtest/kernel-alt-vm

%changelog
* Mon Oct 31 2022 Vitaly Chikunov <vt@altlinux.org> 16-alt1
- Update skiplist for kernel-image-rt-5.10.152-alt1.rt75.

* Wed Oct 26 2022 Vitaly Chikunov <vt@altlinux.org> 15-alt1
- Skip tests that timeout testing kernel-image-std-debug on armh.

* Tue Oct 11 2022 Vitaly Chikunov <vt@altlinux.org> 14-alt2
- Remove circular dependency on ltp package.

* Thu Oct 06 2022 Vitaly Chikunov <vt@altlinux.org> 14-alt1
- Skiplist additions because of armh: epoll01, ioctl01_02, request_key03,
  sendmsg03.

* Tue Oct 04 2022 Vitaly Chikunov <vt@altlinux.org> 13-alt1
- Skiplist update for ltp-20220930-alt1.

* Fri Jul 08 2022 Vitaly Chikunov <vt@altlinux.org> 12-alt1
- Skip keyctl02 due to failure of kernel-image-un-def-5.18.10-alt1 on armh.
- Skip madvise06 that failed on beekeeper for kernel-image-rt-5.10.120-alt1.rt70.
- Skip inotify11 that failed on beekeeper for kernel-image-un-def-1:5.18.8-alt1.

* Fri Jun 24 2022 Vitaly Chikunov <vt@altlinux.org> 11-alt1
- Skip long running pty0{6,7} tests.

* Wed Jun 22 2022 Vitaly Chikunov <vt@altlinux.org> 10-alt1
- Skip getrusage04 (due to armh failures).

* Mon Jun 20 2022 Vitaly Chikunov <vt@altlinux.org> 9-alt1
- Skip ENOSYS tests for xenomai-4.19.246.

* Sat Jun 18 2022 Vitaly Chikunov <vt@altlinux.org> 8-alt1
- Skip futex_waitv0{1,2,3} and waitid10 (after ltp update).

* Sat Jun 18 2022 Vitaly Chikunov <vt@altlinux.org> 7-alt1
- Skip 2 tests (ppoll01, pread02_64) failed on i586 in ALT beekeeper.

* Wed Jun 15 2022 Vitaly Chikunov <vt@altlinux.org> 6-alt1
- Skip failing (set_mempolicy05) test on i586.

* Wed Jun 15 2022 Vitaly Chikunov <vt@altlinux.org> 5-alt1
- Skip failing tests on i586 and armh.

* Mon Jun 13 2022 Vitaly Chikunov <vt@altlinux.org> 4-alt1
- Disable userns tests.

* Sat Nov 13 2021 Vitaly Chikunov <vt@altlinux.org> 3-alt1
- Skip fanout01 (too slow).

* Tue Sep 28 2021 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Skip new tests after ltp-20210927 release.

* Fri Jul 23 2021 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
