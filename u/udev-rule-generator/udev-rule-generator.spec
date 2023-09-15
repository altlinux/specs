Name: udev-rule-generator
Epoch: 2
Version: 1.6
Release: alt2
Summary: Common package for udev rule generator
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Hardware
License: GPLv2+
PreReq: udev >= 1:238-alt4
BuildArch: noarch

Requires: udevd-final >= 1.0

Source: %name-%version.tar

%description
This package contains common files for udev-rule-generator:
 - udev-rule-generator SysV init script
 - udev-rule-generator systemd unit
 - rule_generator.functions

%package cdrom
Summary: CD rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
PreReq: udev-rules
PreReq: %name = %EVR

%description cdrom
This package contains CD rule generator for udev

%package net
Summary: Net rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
PreReq: udev-rules
PreReq: %name = %EVR

%description net
This package contains Net rule generator for udev

%prep
%setup

%build

%install
mkdir -p %buildroot{%_initdir,%_unitdir,{%_sysconfdir,/lib}/udev/rules.d,%_sysconfdir/sysconfig}
install -p -m755 udev-rule-generator.init %buildroot%_initdir/udev-rule-generator
install -p -m644 udev-rule-generator.service %buildroot%_unitdir/udev-rule-generator.service

# Create ghost files
#touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-net.rules
#touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-cd.rules

# udev rule generator
install -p -m644 rule_generator.functions %buildroot/lib/udev/
install -p -m755 write_net_rules %buildroot/lib/udev/
install -p -m644 udev-rule-generator.sysconfig %buildroot%_sysconfdir/sysconfig/udev-rule-generator
install -p -m644 75-persistent-net-generator.rules %buildroot/lib/udev/rules.d/
install -p -m755 write_cd_rules %buildroot/lib/udev/
install -p -m644 75-cd-aliases-generator.rules %buildroot/lib/udev/rules.d/
#ln -s /dev/null %buildroot%_sysconfdir/udev/rules.d/80-net-setup-link.rules

%preun
%preun_service udev-rule-generator

%post cdrom
%post_service udev-rule-generator

%post net
ln -sf /dev/null %_sysconfdir/udev/rules.d/80-net-setup-link.rules
%post_service udev-rule-generator

%preun net
rm -f %_sysconfdir/udev/rules.d/80-net-setup-link.rules

%files
/lib/udev/rule_generator.functions
%_initdir/udev-rule-generator
%_unitdir/udev-rule-generator.service

%files cdrom
#config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-cd.rules
/lib/udev/rules.d/75-cd-aliases-generator.rules
/lib/udev/write_cd_rules

%files net
#config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-net.rules
#_sysconfdir/udev/rules.d/80-net-setup-link.rules
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/sysconfig/udev-rule-generator
/lib/udev/rules.d/75-persistent-net-generator.rules
/lib/udev/write_net_rules

%changelog
* Fri Sep 15 2023 Sergey Y. Afonin <asy@altlinux.org> 2:1.6-alt2
- used UPDATE_NET_RULES=yes by default
  https://bugzilla.altlinux.org/show_bug.cgi?id=29282#c40

* Tue Aug 29 2023 Anton Midyukov <antohami@altlinux.org> 2:1.6-alt1
- replace udevd-final service to separate package udevd-final

* Wed Aug 23 2023 Sergey Y. Afonin <asy@altlinux.org> 2:1.5-alt1
- used "ether" by default again
- workaround for ALT #47262:
  + ghost rules are not packaged in /etc/udev/rules.d
  + the stub file /etc/udev/rules.d/80-net-setup-link.rules is created in a post script

* Sun Apr 26 2020 Sergey Y. Afonin <asy@altlinux.org> 2:1.4-alt1
- renamed sysconfig/write_net_rules to sysconfig/udev-rule-generator
- renaming interfaces if 70-persistent-net.rules recently changed (ALT #32166)
- added the ability to update persistent-net.rules (ALT #29282)

* Wed Sep 25 2019 Anton Midyukov <antohami@altlinux.org> 2:1.3-alt1
- run udevd-final before raising the network

* Thu Aug 29 2019 Sergey Y. Afonin <asy@altlinux.org> 2:1.2-alt1
- returned "eth" by default in write_net_rules (problems with
  the "ether" name detected in some applications)
- added sysconfig/write_net_rules

* Tue Aug 20 2019 Sergey Y. Afonin <asy@altlinux.org> 2:1.1-alt1
- changed /var/lock to /run/lock (antohami@altlinux, ALT #35889)
- changed "eth" to "ether" in generated rules (ALT #32167)

* Fri Apr 06 2018 Alexey Shabalin <shaba@altlinux.ru> 2:1-alt2
- update post and preun scripts

* Sat Mar 31 2018 Alexey Shabalin <shaba@altlinux.ru> 2:1-alt1
- Initial build

