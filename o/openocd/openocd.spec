Name: openocd
Version: 0.10.0
Release: alt0_rc1
Summary: Debugging, in-system programming and boundary-scan testing for embedded devices

Group: Development/Tools
License: GPLv2
Url: http://sourceforge.net/projects/openocd
Source: %name-%version-rc1.tar
Source10: libjaylink.tar

BuildRequires: chrpath libftdi1-devel jimtcl-devel libhidapi-devel libusb-compat-devel texinfo

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system
programming and boundary-scan testing for embedded devices. Various
different boards, targets, and interfaces are supported to ease
development time.

Install OpenOCD if you are looking for an open source solution for
hardware debugging.

%prep
%setup -n %name-%version-rc1
tar -xf %SOURCE10 -C src/jtag/drivers

%build
%autoreconf
# FIXME   --enable-werror
%configure \
  --disable-werror \
  --disable-doxygen-html \
  --disable-internal-jimtcl \
  --enable-aice \
  --enable-amtjtagaccel \
  --enable-arm-jtag-ew \
  --enable-armjtagew \
  --enable-at91rm9200 \
  --enable-bcm2835gpio \
  --enable-buspirate \
  --enable-cmsis-dap \
  --enable-dummy \
  --enable-ep93xx \
  --enable-ft2232_libftdi \
  --enable-ftdi \
  --enable-gw16012 \
  --enable-jlink \
  --enable-jtag_vpi \
  --enable-opendous \
  --enable-openjtag \
  --enable-osbdm \
  --enable-parport \
  --enable-parport_ppdev \
  --enable-presto \
  --enable-remote-bitbang \
  --enable-rlink \
  --enable-stlink \
  --enable-sysfsgpio \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster \
  --enable-usb-blaster-2 \
  --enable-usb_blaster_libftdi \
  --enable-usbprog \
  --enable-vsllink \
  CROSS=
%make_build

%install
%makeinstall_std
#chrpath --delete %buildroot/%_bindir/openocd
mkdir -p %buildroot%_sysconfdir/udev/rules.d/
install -m644 \
	contrib/*.rules \
	src/jtag/drivers/libjaylink/contrib/*.rules \
	%buildroot%_sysconfdir/udev/rules.d/

%files
%doc AUTHORS BUGS ChangeLog HACKING NEWS* NEWTAPS
%doc README TODO
%doc %_datadir/%name/contrib
%_sysconfdir/udev/rules.d/*
%dir %_datadir/%name
%_datadir/%name/scripts
%_datadir/%name/OpenULINK
%_bindir/%name
%_infodir/%name.info*
%_mandir/man1/*

%changelog
* Thu Jan 05 2017 Ildar Mulyukov <ildar@altlinux.ru> 0.10.0-alt0_rc1
- new version
- minor cleanups and additions
- fixes #32962

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1.1
- NMU: added BR: texinfo

* Thu Nov 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.0-alt1
- Updated to v0.9.0.

* Mon May 05 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.0-alt1.git8fa67bd
- Updated to v0.8.0-1-g8fa67bd.

* Sat Sep 21 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.0-alt1.git1304b27
- New version (1304b27).

* Wed Apr 10 2013 Andrey Kotoff <kotbegemot@altlinux.org> 0.6.0-alt1.git74db7f9
- Initial build.
