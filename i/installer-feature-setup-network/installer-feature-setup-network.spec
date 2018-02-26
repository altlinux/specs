Name: installer-feature-setup-network
Version: 0.22
Release: alt1

Summary: Installer network autosetup hooks
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains network autosetup hooks for installer.

%package stage2
Summary: Installer stage2 network autosetup hook
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage2 hostinfo iproute2

%description stage2
This package contains network autosetup hook for installer stage2.

%package stage3
Summary: Installer stage3 network autosetup hooks
License: GPL
Group: System/Configuration/Other
Requires: installer-common-stage3 alterator-net-eth chkconfig etcnet

%description stage3
This package contains network autosetup hooks for installer stage3.

%prep
%setup

%install
%define hookdir %_datadir/install2
mkdir -p %buildroot%hookdir/{initinstall,preinstall,postinstall}.d
install -pm755 2*.sh %buildroot%hookdir/initinstall.d/
install -pm755 3*.sh %buildroot%hookdir/preinstall.d/
install -pm755 4*.sh %buildroot%hookdir/postinstall.d/

%files stage2
%hookdir/initinstall.d/*
%hookdir/postinstall.d/*
%hookdir/preinstall.d/31*

%files stage3
%hookdir/preinstall.d/30*

%changelog
* Wed May 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.22-alt1
- move setup networkmanager after setup systemd

* Mon Nov 08 2010 Anton Farygin <rider@altlinux.ru> 0.21-alt1
- do not create bridges if ifaddbr not exits in installer

* Wed Mar 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.20-alt1
- dhcp timeout setup fixed

* Sat Feb 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.19-alt1
- DHCP_TIMEOUT set to 60 seconds

* Mon Jul 06 2009 Dmitry V. Levin <ldv@altlinux.org> 0.18-alt1
- 30-setup-network.sh: Honor $DOMAINNAME.

* Wed May 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt1
- Updated all scripts to use alterator-net-functions.
- 30-setup-network.sh: Save iface TYPE and HOST.

* Wed Apr 29 2009 Dmitry V. Levin <ldv@altlinux.org> 0.16-alt1
- 30-setup-network.sh: Treat "localhost" the same way as "localhost.localdomain".

* Wed Apr 22 2009 Dmitry V. Levin <ldv@altlinux.org> 0.15-alt1
- 25-setup-dhcp.sh: Bridgify all eth ifaces.
- *.sh: Fixed typo in netdev_find_bridge().

* Thu Apr 16 2009 Dmitry V. Levin <ldv@altlinux.org> 0.14-alt1
- 30-setup-network.sh: Use alterator-net-eth to configure static interfaces.

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 0.13-alt1
- preinstall.d/30-setup-network.sh: Enabled for network install as well.

* Thu Apr 09 2009 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt1
- Moved dhcp autosetup to initinstall stage.
- Reverted to default dhcp timeout.

* Wed Apr 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.11-alt1
- Rewritten from stage2 to stage3.
- Decreased dhcp timeout.
- Hopefully fixed coexistance with 70-net-eth.sh from alterator-net-eth.

* Fri Apr 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt1
- setting DHCP_ARGS fixed, dhcp timeout decreased

* Wed Apr 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- try to make more consistent configs, more shell_config_set usage

* Thu Mar 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- switched to shell-config usage

* Mon Mar 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- added '-p' for dhcpcd for not drop network and freeze NFS root

* Mon Mar 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- added setting NM_CONTROLLED=yes in all interfaces directories

* Thu Mar 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- NetworkManager for all if exists

* Wed Mar 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- fixed hostname generation during network installation

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- added generation hostname from IP when network is up but there is no backresolve

* Thu Feb 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- added querying hostname via DNS

* Wed Feb 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build

