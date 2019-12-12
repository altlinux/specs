%def_enable snapshot
%def_enable check
%define _localstatedir %_var
%define git g9af2b12
%define _group usbmux

Name: usbmuxd
Version: 1.1.1
Release: alt0.3.g%git

Summary: Daemon for communicating with Apple's iPod Touch and iPhone
Group: System/Servers
License: GPLv3+
Url: http://www.libimobiledevice.org/

%if_disabled snapshot
Source: http://www.libimobiledevice.org/downloads/%name-%version.tar.bz2
%else
# VCS: https://github.com/libimobiledevice/usbmuxd.git
Source: %name-%version.tar
%endif

%define plist_ver 1.11
%define usb_ver 1.0.9
%define imobiledevice_ver 1.2.1

BuildRequires: gcc-c++ cmake
BuildRequires: libplist-devel >= %plist_ver
BuildRequires: libusb-devel >= %usb_ver
BuildRequires: libimobiledevice-devel >= %imobiledevice_ver
BuildRequires: libudev-devel systemd-devel

%description
usbmuxd (USB Multiplex Daemon) is a daemon used for communicating with
Apple's iPod Touch and iPhone devices. It allows multiple services on
the device to be accessed simultaneously.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make check

%pre
/usr/sbin/groupadd -rf %_group ||:
/usr/sbin/useradd -M -r -s /dev/null -c "USB Multiplex Daemon" \
	-d %_localstatedir/empty -g %_group %_group &>/dev/null ||:

%files
%_sbindir/usbmuxd
/lib/udev/rules.d/39-%name.rules
%_unitdir/%name.service
%_man8dir/%name.*
%doc AUTHORS README* NEWS

%changelog
* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt0.3.gg9af2b12
- updated to 1.1.0-66-g9af2b12
- %%check section

* Fri Jun 22 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1.1-alt0.2.g08d9ec0
- Add usbmux user.

* Fri Jun 22 2018 L.A. Kostis <lakostis@altlinux.ru> 1.1.1-alt0.1.g08d9ec0
- 1.1.0-43-g08d9ec0

* Thu Oct 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt4
- rebuilt with _localstatedir=%%_var

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt3
- rebuilt for new gcc, python, cython etc.

* Mon Feb 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt2
- rebuilt against libimobiledevice.so.6

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt2
- rebuilt for debuginfo

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sun Mar 14 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.rc2
- first build for Sisyphus

