%define modprobedir %_sysconfdir/modprobe.d

Name: nouveau-blacklist
Version: 0.1.0
Release: alt1

Summary: Blacklist nouveau module
License: ALT-Public-Domain
Group: System/Kernel and hardware
Url: https://git.altlinux.org/people/qualimock/packages/nouveau-blacklist.git
VCS: https://git.altlinux.org/people/qualimock/packages/nouveau-blacklist.git

BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%modprobedir
echo -e 'blacklist nouveau\n' > %buildroot%modprobedir/%name.conf

%files
%attr(0644,root,root) %config(noreplace) %modprobedir/%name.conf

%changelog
* Thu Jul 03 2025 Alexey Volkov <qualimock@altlinux.org> 0.1.0-alt1
- initial build for ALT
