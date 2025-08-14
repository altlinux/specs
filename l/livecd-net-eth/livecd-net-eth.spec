Name: livecd-net-eth
Version: 0.5.4
Release: alt1

Summary: Try to autoconfigure ethernet interfaces
License: GPL-2.0-or-later
Group: System/Configuration/Networking

Url: http://www.altlinux.org/etcnet
Source0: %name-%version.tar

BuildArch: noarch

%description
This package might be useful for livecd images or virtual machines
when it's required to autoconfigure ethernet interfaces via DHCP.

%prep
%setup

%build

%install
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm755 %name.sh %buildroot%_prefix/libexec/%name
install -pDm644 %name.service %buildroot%_unitdir/%name.service

%files
%_initdir/%name
%_prefix/libexec/%name
%_unitdir/%name.service

%preun
%preun_service %name

%changelog
* Thu Aug 14 2025 Anton Midyukov <antohami@altlinux.org> 0.5.4-alt1
- livecd-net-eth.service: add RemainAfterExit=yes

* Mon Aug 11 2025 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1
- livecd-net-eth.sh: do not confugure networkd interface as dhcp if not link
- livecd-net-eth.service: do not install to multi-user.target

* Fri May 30 2025 Anton Midyukov <antohami@altlinux.org> 0.5.2-alt1
- livecd-net-eth.sh: do not override global variables in a cycle
- livecd-net-eth.sh: more global variable, fix setup_networkd function
- livecd-net-eth.sh: configure etcnet interface as static, if link is
  not detected
- livecd-net-eth.sh: set shebang to bash

* Wed May 28 2025 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt3
- add %%preun_service
- Revert "livecd-net-eth.init: do not set DHCP_TIMEOUT=7"
- Separate script livecd-net-eth.sh from livecd-net-eth.init

* Tue May 27 2025 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt2
- livecd-net-eth.init: fix typo

* Mon May 26 2025 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt1
- livecd-net-eth.init: 
  + setup NetworkManager(etcnet) instead NetworkManager(native)
  + setup stage1 network interfaces as etcnet
  + set HOSTNAME from stage1 settings
  + do not set DHCP_TIMEOUT=7

* Wed Mar 19 2025 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- livecd-net-eth.init: refactoring for compatibility witn alterator-net-eth
- livecd-net-eth.init: create configs of interface for en* only
- convert License tag to SPDX-format
- drop Packager tag

* Sat Sep 04 2021 Anton Midyukov <antohami@altlinux.org> 0.4.4-alt1
- livecd-net-eth.init: shift startup of the service from 05 to 07
- livecd-net-eth.service: fix dependencies

* Sat Feb 15 2020 Anton Midyukov <antohami@altlinux.org> 0.4.3-alt1
- Do not configure wlan interfaces

* Thu Sep 15 2016 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- increase DHCP timeout from 3 to 7 seconds (closes: #32397)

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- added the missing space (cosmetic fix)

* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- do not touch:
  + networking configuration resulting from propagator/netboot;
  + packaged default/options-eth configuration file

* Sat Feb 01 2014 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- DHCP timeout set to 3 seconds (thanks msp@ for the question)

* Mon Feb 11 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- resolv.conf (aufs) related workaround

* Fri Feb 08 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-online-repo, livecd-setlocale)

