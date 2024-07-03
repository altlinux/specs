Name:    xrdp-usb
Version: 1.2
Release: alt1

Summary: Infrastructure for redirect USB devices to XRDP session
License: GPL-3.0+ 
Group:   Networking/Remote access
URL:     http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Infrastructure for redirect USB devices to XRDP session contains two packages:
- xrdp-usb-terminal for RDP client
- xrdp-usb-session for session of XRDP server

%package terminal
Summary: Redirect USB devices to XRDP session from RDP client
Group: Networking/Remote access
Requires: usbipd
Requires(post): usbipd
Requires: usbip

%description terminal
%summary

%package session
Summary: Use redirected USB devices in XRDP session
Group: Networking/Remote access
Requires(pre): xrdp
Requires(pre): control
Requires: usbip-client
Requires: usbip

%description session
%summary

%prep
%setup

%install
# For terminal
install -Dpm0400 usbip.sudoers %buildroot%_sysconfdir/sudoers.d/usbip
install -Dpm0644 %name.conf %buildroot%_sysconfdir/%name
install -Dpm0755 usbip-export %buildroot%_bindir/usbip-export
# For session
install -Dpm0755 %name.control %buildroot%_controldir/%name
install -Dpm0755 usbip-attach %buildroot%_sbindir/usbip-attach

%post terminal
SYSTEMCTL=/bin/systemctl
if /sbin/sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1 ; then
    "$SYSTEMCTL" enable --now usbipd
fi

%pre session
%pre_control %name

%post session
%post_control %name -s enabled

%files terminal
%config(noreplace) %_sysconfdir/%name
%attr(400,root,root) %config(noreplace) %_sysconfdir/sudoers.d/usbip
%_bindir/usbip-export

%files session
%config %_controldir/%name
%_sbindir/usbip-attach

%changelog
* Wed Jul 03 2024 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Fix regexp for new xrdp version (thanks Belash Konstanstin).

* Wed Sep 15 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- usbip-export: use sudo in non-interactive mode.

* Mon Sep 13 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
