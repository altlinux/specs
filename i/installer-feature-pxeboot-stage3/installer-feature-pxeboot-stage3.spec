Name: installer-feature-pxeboot-stage3
Version: 0.3
Release: alt1

Summary: Installer stage3 PXE boot server hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch
Requires: installer-common-stage3, rpcbind, tftp-server-xinetd, xinetd

%description
This package contains PXE boot server tuning hook for installer stage3.

%install
mkdir -p %buildroot

%post
unset DURING_INSTALL

sed -i '/^[[:space:]]*in.tftpd:/d' /etc/hosts.allow
echo 'in.tftpd: ALL' >>/etc/hosts.allow

sed -i 's/^[[:space:]]*only_from[[:space:]]*=[[:space:]]*127.0.0.1/#&/' /etc/xinetd.conf
chkconfig xinetd on
chkconfig tftp on

control rpcbind server

%files

%changelog
* Sun Nov 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- use rpcbind instead portmap

* Wed Apr 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Rewritten from stage2 to stage3.

* Tue Apr 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- use control to switch portmap service state

* Mon Mar 31 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- noarch

* Tue Mar 11 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release based on 06-pxe.sh common to several installer-*
  packages -- file location is the same thus this package conflicts
  with their current versions

