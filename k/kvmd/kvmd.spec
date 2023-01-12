Name: kvmd
Version: 3.191
Release: alt2

Summary: The PiKVM daemon
License: GPLv3
Group: System/Servers
Url: https://pikvm.org/

Requires: kvmd-janus
Requires: ustreamer
Requires: ustreamer-plugin-janus
Requires: nginx
Requires: openssl
Requires: ipmitool
Requires: iptables
Requires: dnsmasq
Requires: v4l-utils
Requires: sudo

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%define _sysusersdir /lib/sysusers.d

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_udevrulesdir %buildroot%_sysconfdir

install -pm0644 -D configs/os/sysctl.conf %buildroot%_sysctldir/kvmd.conf
install -pm0644 -D configs/os/sysusers.conf %buildroot%_sysusersdir/kvmd.conf
install -pm0644 -D configs/os/tmpfiles.conf %buildroot%_tmpfilesdir/kvmd.conf
install -pm0644 -D configs/os/services/kvmd.service %buildroot%_unitdir/kvmd.service
install -pm0644 configs/os/services/kvmd-*.service %buildroot%_unitdir

cp -at %buildroot%_udevrulesdir  configs/os/udev/*.rules

cp -at %buildroot%_sysconfdir configs/kvmd
cp -at %buildroot%_sysconfdir/kvmd configs/janus configs/nginx
mkdir -p %buildroot%_sysconfdir/kvmd/override.d
mkdir -p %buildroot%_sysconfdir/kvmd/vnc/ssl
ln -srv %buildroot%_sysconfdir/kvmd/main/v4mini-hdmi-rpi4.yaml \
	%buildroot%_sysconfdir/kvmd/main.yaml

mkdir -p %buildroot%_datadir/kvmd
cp -at %buildroot%_datadir/kvmd extras hid contrib/keymaps web

install -pm0755 scripts/kvmd-gencert %buildroot%_bindir

install -pm0600 -D configs/os/sudoers/v4mini-hdmi %buildroot%_sysconfdir/sudoers.d/kvmd
rm -v %buildroot%_unitdir/kvmd-bootconfig.service
rm -v %buildroot%_unitdir/kvmd-certbot.service

%files
%_sysctldir/*.conf
%_sysusersdir/*.conf
%_tmpfilesdir/*.conf
%_unitdir/*.service
%_udevrulesdir/*.rules

%_sysconfdir/sudoers.d/kvmd

%_sysconfdir/kvmd

%_bindir/kvmd*

%_datadir/kvmd

%python3_sitelibdir/kvmd
%python3_sitelibdir/kvmd-%version.dist-info

%changelog
* Thu Jan 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.191-alt2
- use kvmd-janus fork

* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.191-alt1
- 3.191 released

* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.189-alt1
- initial
