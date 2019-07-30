%define module_name lkrg
%define module_version 0.7

Name: kernel-source-lkrg
Version: %module_version
Release: alt1

Summary:  Linux Kernel Runtime Guard module sources

License: GPL-2.0
Group: Development/Kernel
Url:  https://www.openwall.com/lkrg/

# repacked https://www.openwall.com/lkrg/lkrg-%version.tar.gz
Source: %module_name-%version.tar

ExclusiveArch: i586 x86_64
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
* Mon Jul 22 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7-alt1
- Initial build for ALT Sisyphus.

