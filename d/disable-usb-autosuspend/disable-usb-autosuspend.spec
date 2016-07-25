Name:    disable-usb-autosuspend
Version: 1.1
Release: alt1
Summary: Disables autosuspend USB devices
License: Public domain
Group:   System/Kernel and hardware
BuildArch: noarch

Requires(post): make-initrd

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/modprobe.d
echo "options usbcore autosuspend=-1" > %buildroot%_sysconfdir/modprobe.d/%name.conf

%post
# 1. check $DURING_INSTALL and do not make-initrd if system install
# 2. check sys filesystem mounted by mountpoint -q /sys
mountpoint -q /sys
[ $? -ne 0 -o -n "$DURING_INSTALL" ] || /usr/sbin/make-initrd

%files
%_sysconfdir/modprobe.d/%name.conf

%changelog
* Mon Jul 25 2016 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Recreate initrd in post install stage

* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus (thanks Speccyfighter)
