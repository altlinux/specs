Name: usbmon
Version: 5.4
Release: alt1

Summary: A basic front-end to usbmon
Group: System/Base
License: GPLv2

Url: http://people.redhat.com/zaitcev/linux/

Packager: Denis Baranov <baraka@altlinux.org>

Source: %name-%version.tar

%description
The usbmon program collects and prints a trace of USB transactions as they
occur between the USB core and HCDs. Analyzing the trace helps to debug the
kernel USB stack, device firmware, and applications.

%prep
%setup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %buildroot%_man8dir
install -p -m 644 -t %buildroot%_man8dir usbmon.8
mkdir -p %buildroot%_sbindir
install -p -m 755 -t %buildroot%_sbindir usbmon


%files
%doc README COPYING
%_sbindir/usbmon
%_man8dir/usbmon.8*

%changelog
* Wed Dec 01 2010 Denis Baranov <baraka@altlinux.org> 5.4-alt1
- Initial build for ALTLinux

