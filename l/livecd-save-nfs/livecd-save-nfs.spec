Name: livecd-save-nfs
Version: 0.4.2
Release: alt1

Summary: tell NetworkManager not touch already UP ifaces
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch
PreReq: service chkconfig

%description
tell NetworkManager not touch already UP ifaces

%prep
%setup -c


%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 livecd-save-nfs/livecd-save-nfs %buildroot%_initdir/livecd-save-nfs 
install -pD -m0644 livecd-save-nfs/livecd-save-nfs.service %buildroot%_unitdir/livecd-save-nfs.service

%preun
%preun_service %name

%files 
%_initdir/livecd-save-nfs
%_unitdir/livecd-save-nfs.service

%changelog
* Wed Sep 01 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.4.2-alt1
- Ignore interfaces which are down or have no carrier (closes: #40800)
- Immediately fork dhcpcd into the background (related: #40800)
- Act only when booted via NFS or CIFS (related: #40800)

* Tue Jul 16 2013 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Fix regexp for interface name.

* Tue Apr 30 2013 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Expicitly set DISABLED=no (closes: #28499).
- Add livecd-save-nfs.service.
- Update for new ethernet devices names.
- Turning on multicast for Avahi purpose (by george@).
- Use --request to disable double IP (by george@) (closes: #27082).

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt4
- reverted ip configuration to 0.3-alt1

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt3
- chkconfig header fixed

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- change dhcpcd -p to DISABLED=no

* Thu Jun 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- run dhcpcd -p on up interface to full configure it

* Fri Jun 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- interface directory creation added

* Fri Jun 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build
