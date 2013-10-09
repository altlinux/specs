Name: openocd
Version: 0.7.0
Release: alt1.git1304b27
Summary: Debugging, in-system programming and boundary-scan testing for embedded devices

Group: Development/Tools
License: GPLv2
Url: http://sourceforge.net/projects/openocd
Source: %name-%version.tar
Source10: git2cl.tar
Source11: jimtcl.tar

BuildRequires: chrpath libftdi-devel tcl

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system
programming and boundary-scan testing for embedded devices. Various
different boards, targets, and interfaces are supported to ease
development time.

Install OpenOCD if you are looking for an open source solution for
hardware debugging.

%prep
%setup
tar -xf %SOURCE10 -C tools
tar -xf %SOURCE11

%build
%autoreconf
%configure \
  --enable-maintainer-mode \
  --enable-werror \
  --enable-static \
  --disable-shared \
  --enable-dummy \
  --enable-ft2232_libftdi \
  --enable-gw16012 \
  --enable-parport \
  --enable-parport_ppdev \
  --enable-presto_libftdi \
  --enable-amtjtagaccel \
  --enable-arm-jtag-ew \
  --enable-oocd_trace \
  --enable-ep39xx \
  --enable-at91rm9200 \
  --disable-doxygen-html \
  --enable-usb_blaster_libftdi \
  --enable-usbprog \
  --enable-jlink \
  --enable-vsllink \
  --enable-rlink \
  --enable-ulink \
  --enable-stlink \
  --enable-ti-icdi \
  --enable-remote-bitbang \
  CROSS=
make

%install
make install DESTDIR=%buildroot INSTALL="install -p"
chrpath --delete %buildroot/%_bindir/openocd

%files
%doc README COPYING AUTHORS ChangeLog NEWS TODO
%doc %_datadir/%name/contrib
%dir %_datadir/%name
%_datadir/%name/scripts
%_datadir/%name/OpenULINK
%_bindir/%name
%_infodir/%name.info*.gz
%_mandir/man1/*

%changelog
* Sat Sep 21 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.0-alt1.git1304b27
- New version (1304b27).

* Wed Apr 10 2013 Andrey Kotoff <kotbegemot@altlinux.org> 0.6.0-alt1.git74db7f9
- Initial build.
