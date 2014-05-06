Name: openocd
Version: 0.8.0
Release: alt1.git8fa67bd
Summary: Debugging, in-system programming and boundary-scan testing for embedded devices

Group: Development/Tools
License: GPLv2
Url: http://sourceforge.net/projects/openocd
Source: %name-%version.tar
Source10: git2cl.tar
Patch1: openocd-jimtcl0_75.patch

BuildRequires: chrpath libftdi-devel jimtcl-devel

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
%patch1 -p0

%build
%autoreconf
%configure \
  --enable-maintainer-mode \
  --enable-werror \
  --enable-static \
  --enable-shared \
  --enable-aice \
  --enable-amtjtagaccel \
  --enable-arm-jtag-ew \
  --enable-armjtagew \
  --enable-at91rm9200 \
  --enable-buspirate \
  --enable-cmsis-dap \
  --disable-doxygen-html \
  --enable-dummy \
  --enable-ep39xx \
  --enable-ft2232_libftdi \
  --enable-ftdi \
  --enable-gw16012 \
  --disable-internal-jimtcl \
  --enable-ioutil \
  --enable-jlink \
  --enable-jtag_vpi \
  --enable-oocd_trace \
  --enable-opendous \
  --enable-openjtag_ftdi \
  --enable-osbdm \
  --enable-parport \
  --enable-parport_ppdev \
  --enable-presto_libftdi \
  --enable-remote-bitbang \
  --enable-rlink \
  --enable-stlink \
  --enable-sysfsgpio \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster-2 \
  --enable-usb_blaster_libftdi \
  --enable-usbprog \
  --enable-vsllink \
  CROSS=
%make_build

%install
make install DESTDIR=%buildroot INSTALL="install -p"
%makeinstall_std
#chrpath --delete %buildroot/%_bindir/openocd

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
* Mon May 05 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.0-alt1.git8fa67bd
- Updated to v0.8.0-1-g8fa67bd.

* Sat Sep 21 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.0-alt1.git1304b27
- New version (1304b27).

* Wed Apr 10 2013 Andrey Kotoff <kotbegemot@altlinux.org> 0.6.0-alt1.git74db7f9
- Initial build.
