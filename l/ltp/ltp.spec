Name: ltp
Version: 20190828
Release: alt1

Summary: Linux Test Project
License: GPL-2.0-or-later
Group: Development/Tools
Url: http://linux-test-project.github.io/
# Git: https://github.com/linux-test-project/ltp
Source: %name-%version.tar

%description
The Linux Test Project has a goal to deliver test suites to the open source
community that validate the reliability, robustness, and stability of Linux.

The LTP testsuite contains a collection of tools for testing the Linux kernel
and related features. Our goal is to improve the Linux kernel and system
libraries by bringing test automation to the testing effort. Interested open
source contributors are encouraged to join.

Testing Linux, one syscall at a time.

%add_verify_elf_skiplist /usr/lib/ltp/testcases/*

%prep
%setup

%build
%autoreconf
./configure --prefix=/usr/lib/ltp
%make_build

%install
%makeinstall_std

%files
/usr/lib/ltp

%changelog
* Tue Sep 03 2019 Vitaly Chikunov <vt@altlinux.org> 20190828-alt1
- Initial build of LTP.
