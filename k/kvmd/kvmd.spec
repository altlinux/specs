Name: kvmd
Version: 4.217
Release: alt1

Summary: The PiKVM daemon
License: GPLv3
Group: System/Servers
URL: https://pikvm.org/
VCS: https://github.com/pikvm/kvmd

Requires: python3-module-kvmd = %version
Requires: ipmitool
Requires: libxkbcommon
Requires: ustreamer
Requires: ustreamer-plugin-janus

Source: %name-%version.tar

BuildArch: noarch

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_udevrulesdir %buildroot%_sysconfdir

install -pm0644 -D configs/os/sysctl.conf %buildroot%_sysctldir/kvmd.conf
install -pm0644 -D configs/os/sysusers.conf %buildroot%_sysusersdir/kvmd.conf
install -pm0644 -D configs/os/tmpfiles.conf %buildroot%_tmpfilesdir/kvmd.conf
install -pm0644 -D configs/os/services/kvmd.service %buildroot%_unitdir/kvmd.service
install -pm0644 configs/os/services/kvmd-*.service %buildroot%_unitdir

cp -at %buildroot%_udevrulesdir configs/os/udev/*.rules
cp -at %buildroot%_sysconfdir configs/kvmd
cp -at %buildroot%_sysconfdir/kvmd configs/janus configs/nginx

install -pm0600 -D configs/os/sudoers/v4mini-hdmi \
    %buildroot%_sysconfdir/sudoers.d/kvmd

mkdir -p %buildroot%_sysconfdir/kvmd/override.d
mkdir -p %buildroot%_sysconfdir/kvmd/vnc/ssl

install -pm0755 -D -t %buildroot%_bindir \
    scripts/kvmd-{gencert,update-switch}

install -pm0755 -D -t %buildroot%_libexecdir/kvmd \
    scripts/kvmd-{udev-flash-pico,ucamera-prepare}

touch %buildroot%_sysconfdir/kvmd/platform
ln -srv %buildroot%_sysconfdir/kvmd/platform \
    %buildroot%_libexecdir/kvmd/platform

mkdir -p %buildroot%_datadir/kvmd/configs.default
cp -at %buildroot%_datadir/kvmd extras hid contrib/keymaps web
cp -at %buildroot%_datadir/kvmd/configs.default configs/*

rm -v %buildroot%_unitdir/kvmd-bootconfig.service
rm -v %buildroot%_unitdir/kvmd-certbot.service
rm -v %buildroot%_unitdir/kvmd-camera@.service

%files
%_sysctldir/*.conf
%_sysusersdir/*.conf
%_tmpfilesdir/*.conf

%_udevrulesdir/*.rules
%_unitdir/*.service

%_sysconfdir/kvmd
%config(noreplace) %_sysconfdir/kvmd/platform
%_sysconfdir/sudoers.d/kvmd

%_bindir/kvmd-gencert
%_bindir/kvmd-update-switch

%_libexecdir/kvmd/platform
%_libexecdir/kvmd/kvmd-ucamera-prepare
%_libexecdir/kvmd/kvmd-udev-flash-pico

%_datadir/kvmd

%changelog
* Tue Sep 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.217-alt1
- 4.217 released

* Thu Mar 06 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.313-alt2
- fixed breakage with recent v4l-utils

* Mon Mar 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.313-alt1
- 3.313 released

* Mon Sep 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.217-alt1
- 3.217 released

* Tue Jul 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.212-alt2
- fixed build with recent setuptools

* Tue Apr 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.212-alt1
- 3.212 released

* Tue Apr 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.211-alt1
- 3.211 released

* Fri Jan 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.191-alt3
- fixed janus js location

* Thu Jan 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.191-alt2
- use kvmd-janus fork

* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.191-alt1
- 3.191 released

* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.189-alt1
- initial
