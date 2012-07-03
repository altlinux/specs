Summary: usb-modeswitch is  a mode switching tool for controlling "flip flop" (multiple device) USB gear. 
Name: usb-modeswitch 
Version: 1.1.8
Release: alt1
License: GPL

Group:  System/Configuration/Hardware
URL: http://www.draisberghof.de/usb_modeswitch/
Source0: %name-%version.tar

Requires: usb-modeswitch-data
BuildRequires: tcl libusb-compat-devel 
Provides: usb_modeswitch
Obsoletes: usb_modeswitch

%add_findreq_skiplist /usr/sbin/usb_modeswitch_dispatcher
%add_findprov_skiplist /usr/sbin/usb_modeswitch_dispatcher

%description
USB_ModeSwitch is (surprise!) a mode switching tool for controlling
"flip flop" (multiple device) USB gear.
Several new USB devices (especially high-speed wireless WAN stuff, there
seems to be a chipset from Qualcomm offering that feature) have their
MS Windows drivers onboard; when plugged in for the first time they act
like a flash storage and start installing the driver from there.
After that (and on every consecutive plugging) this driver switches the
mode internally, the storage device vanishes (in most cases), and a new
device (like a USB modem) shows up. The WWAN gear maker Option calls
that feature "ZeroCD (TM)".

Needed for MTS (and others) branded e1550 modems.

%prep

%setup -q

%build
%make

%install
DESTDIR=%buildroot make install

%files
%doc ChangeLog README device_reference.txt 
/usr/sbin/*
%_man1dir/*
/etc/*
/lib/udev/*


%changelog
* Fri Jul 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.8-alt1
- 1.1.8 by manowar@

* Mon Feb 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.5-alt2
- 1.1.5

* Mon Sep 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.4-alt2
- dependence on usb-modeswitch-data added
- provides & obsoletes

* Fri Sep 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.4-alt1
- first build

