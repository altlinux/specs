# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ltp
Version: 20200515
Release: alt1

Summary: Linux Test Project
License: GPL-2.0-only
Group: Development/Tools
Url: http://linux-test-project.github.io/
# Git: https://github.com/linux-test-project/ltp
Source: %name-%version.tar

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

%build
%autoreconf
./configure --prefix=/usr/lib/ltp
%make_build -s

%install
%makeinstall_std -s
find %buildroot/usr/lib/ltp -perm /g+w | xargs chmod g-w

# EZ-Lanucher.
mkdir -p %buildroot/%_bindir
cat > %buildroot/%_bindir/runltp <<-EOF
	#!/bin/sh
	exec /usr/lib/ltp/runltp "\$@"
EOF
chmod a+x %buildroot/%_bindir/runltp

# Make man manable.
mkdir -p %buildroot/usr/share
mv %buildroot/usr/lib/ltp/share/man %buildroot/usr/share/man

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
%_man1dir/*.1.*
%_man3dir/*.3.*

%changelog
* Sun May 17 2020 Vitaly Chikunov <vt@altlinux.org> 20200515-alt1
- Update to 20200515.

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt2
- Reduce amount of requires for tests.

* Tue Sep 03 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt1
- Initial build of LTP.
