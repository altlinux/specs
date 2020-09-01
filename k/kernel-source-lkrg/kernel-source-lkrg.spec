%define module_name lkrg
%define module_version 0.8.1+git20200827.6f700b5

Name: kernel-source-lkrg
Version: %module_version
Release: alt1

Summary:  Linux Kernel Runtime Guard module sources

License: GPL-2.0
Group: Development/Kernel
Url:  https://www.openwall.com/lkrg/

VCS: https://github.com/openwall/lkrg.git
Source: %module_name-%version.tar

ExclusiveArch: i586 x86_64 aarch64
BuildRequires(pre): kernel-build-tools
BuildArch: noarch

%description
Linux Kernel Runtime Guard (LKRG) is a loadable kernel module that performs
runtime integrity checking of the Linux kernel and detection of security
vulnerability exploits against the kernel. As controversial as this concept is,
LKRG attempts to post-detect and hopefully promptly respond to unauthorized
modifications to the running Linux kernel (integrity checking) or to
credentials (such as user IDs) of the running processes (exploit
detection). For process credentials, LKRG attempts to detect the exploit and
take action before the kernel would grant the process access (such as open a
file) based on the unauthorized credentials.

This package contains the LKRG sources.

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %module_name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Sep 01 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1+git20200827.6f700b5-alt1
- Updated to 6f700b5b08b5a0fbc5fa41e1ba1908923a29eca9.

* Thu Jul 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.1-alt1
- Update to 0.8.1 (bugfix release preventing Oops).

* Sun Jun 28 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8-alt1
- Updated to 0.8.

* Thu Jun 04 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt6.gitd57b4c0
- Updated to git commit d57b4c0f0e63d4d88761e098c53280967f2d1aec (fixed
  build with kernel 5.7).

* Fri Apr 17 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt5.git0f7c635
- Updated to git commit 0f7c6350a844c4a65a6860bff1172035e3cccae3 (fixed
  build with kernel 5.6).

* Sat Mar 21 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt4.gitd379e93
- Updated to git commit d379e93c29b4933753a7e769d147c08ea03df63e.

* Thu Feb 06 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt3
- Fixed FTBFS for kernel 5.3+ on aarch64.

* Thu Aug 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt2
- Built for aarch64.

* Mon Jul 22 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1
- Initial build for ALT Sisyphus.

