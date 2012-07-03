Name: ltsp-usermode
Version: 0.1
Release: alt0.1
Summary: LTSP usermode bindings for reboot, halt and poweroff
License: GPL2
Group: System/Configuration/Boot and Init
Source0: ltsp-usermode-reboot.sh
Source1: ltsp-usermode-poweroff.sh
BuildArch: noarch
Conflicts: SysVinit-usermode
Requires: ltspinfo


%description
This package contains LTSP usermode bindings for reboot, halt and
poweroff.


%install
install -d -m 0755 %buildroot{%_bindir,%_sysconfdir/X11/wmsession.d}
install -m 0755 %SOURCE0 %buildroot%_bindir/reboot
install -m 0755 %SOURCE1 %buildroot%_bindir/poweroff
ln -sf reboot %buildroot%_bindir/halt


%files
%_bindir/*


%changelog
* Wed Jun 27 2007 Led <led@altlinux.ru> 0.1-alt0.1
- initial build
