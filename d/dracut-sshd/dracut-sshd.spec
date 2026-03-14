# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: dracut-sshd
Version: 0.7.1
Release: alt1
Summary: Provide SSH access to initramfs early user space
License: GPL-3.0-or-later
Group: Security/Networking
Url: https://github.com/gsauthof/dracut-sshd
BuildArch: noarch
Requires: dracut-network
Requires: openssh-server

Source: %name-%version.tar
%define dracutlibdir %prefix/lib/dracut

%description
This Dracut module (dracut-sshd) integrates the OpenSSH sshd into the
initramfs. It allows for remote unlocking of a fully encrypted root
filesystem and remote access to the Dracut emergency shell (i.e. early
userspace).

%prep
%setup
sed -i /crypto-policies/d 46sshd/sshd.service 46sshd/module-setup.sh
# We dont have sd_notify(3) support which appeared since openssh 9.8.
sed -e 's/^Type=notify/Type=simple/' \
	-e 's@^\(ExecStart=/usr/sbin/sshd\) -D@\1 -e -D@' \
	-i 46sshd/sshd.service
# Our sshd keys location.
sed -i 's@/etc/ssh@/etc/openssh@' README.md 46sshd/module-setup.sh

%install
install -Dpm644 46sshd/sshd_config -t %buildroot%_sysconfdir/%name
install -Dpm644 46sshd/{motd,profile,sshd.service} -t %buildroot%dracutlibdir/modules.d/46sshd
install -Dp 46sshd/module-setup.sh -t %buildroot%dracutlibdir/modules.d/46sshd

%files
%define _customdocdir %_docdir/%name
%doc README.md example
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/sshd_config
%dracutlibdir/modules.d/46sshd

%changelog
* Mon Mar 09 2026 Vitaly Chikunov <vt@altlinux.org> 0.7.1-alt1
- Experimental import 0.7.1-13-gee8d159 (2026-03-06).
