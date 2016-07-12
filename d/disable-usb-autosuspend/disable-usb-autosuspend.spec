Name:    disable-usb-autosuspend
Version: 1.0
Release: alt1
Summary: Disables autosuspend USB devices
License: Public domain
Group:   System/Kernel and hardware
BuildArch: noarch

%description
%summary.

%install
mkdir -p %buildroot%_sysconfdir/modprobe.d
echo "options usbcore autosuspend=-1" > %buildroot%_sysconfdir/modprobe.d/%name.conf

%files
%_sysconfdir/modprobe.d/%name.conf

%changelog
* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus (thanks Speccyfighter)
