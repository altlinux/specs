Name: livecd-save-nfs
Version: 0.3
Release: alt4

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


%files 
%_initdir/livecd-save-nfs


%changelog
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
