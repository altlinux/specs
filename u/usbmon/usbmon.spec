Name: usbmon
Version: 6.1
Release: alt1

Summary: A basic front-end to usbmon
Group: System/Base
License: GPLv2

Url: http://people.redhat.com/zaitcev/linux/

Packager: Denis Baranov <baraka@altlinux.org>

Source: http://people.redhat.com/zaitcev/linux/%name-%version.tar

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
* Fri Dec 20 2019 Grigory Ustinov <grenka@altlinux.org> 6.1-alt1
- Build new version.

* Sat Aug 22 2015 Vitaly Lipatov <lav@altlinux.ru> 6-alt1
- new version 6 (with rpmrb script)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 01 2010 Denis Baranov <baraka@altlinux.org> 5.4-alt1
- Initial build for ALTLinux
