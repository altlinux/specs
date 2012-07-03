Name: livecd-fstab
Version: 0.1
Release: alt3

Summary: Populate /etc/fstab with no-removable devices
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch
PreReq: service chkconfig

%description
Populate /etc/fstab with no-removable devices

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 %name/%name %buildroot%_initdir/%name

%files 
%_initdir/%name

%changelog
* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt3
- At start, restore /etc/fstab file from squashfs image

* Tue May 26 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- Start after haldaemon

* Tue May 26 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- First build for ALT Linux
