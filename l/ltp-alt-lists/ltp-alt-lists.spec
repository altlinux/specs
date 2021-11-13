# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ltp-alt-lists
Summary: ALT specific testcase and skiplist for LTP
Version: 3
Release: alt1
License: GPL-2.0-only
Group: Development/Tools
Url: https://git.altlinux.org/gears/l/ltp-alt-lists.git

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: ltp

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
* Sat Nov 13 2021 Vitaly Chikunov <vt@altlinux.org> 3-alt1
- Skip fanout01 (too slow).

* Tue Sep 28 2021 Vitaly Chikunov <vt@altlinux.org> 2-alt1
- Skip new tests after ltp-20210927 release.

* Fri Jul 23 2021 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
