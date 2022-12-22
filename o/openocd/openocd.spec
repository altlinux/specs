Name: openocd
Version: 0.12.0
Release: alt0.3

Summary: Debugging, in-system programming and boundary-scan testing for embedded devices
License: GPLv2
Group: Development/Tools
Url: http://sourceforge.net/projects/openocd

Source: %name-%version-%release.tar

BuildRequires: capstone-devel jimtcl-devel libftdi1-devel libgpiod-devel libhidapi-devel libjaylink-devel libusb-devel texinfo

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system
programming and boundary-scan testing for embedded devices. Various
different boards, targets, and interfaces are supported to ease
development time.

Install OpenOCD if you are looking for an open source solution for
hardware debugging.

%prep
%setup

%build
%autoreconf
%configure \
  --disable-werror \
  --disable-doxygen-html \
  --disable-internal-jimtcl \
  --disable-internal-libjaylink \
  --enable-amtjtagaccel \
  --enable-at91rm9200 \
  --enable-bcm2835gpio \
  --enable-cmsis-dap \
  --enable-dummy \
  --enable-ep93xx \
  --enable-ft2232_libftdi \
  --enable-ftdi \
  --enable-gw16012 \
  --enable-jlink \
  --enable-jtag_vpi \
  --enable-linuxgpiod \
  --enable-opendous \
  --enable-openjtag \
  --enable-osbdm \
  --enable-parport \
  --enable-parport_ppdev \
  --enable-presto \
  --enable-remote-bitbang \
  --enable-stlink \
  --enable-sysfsgpio \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster \
  --enable-usb-blaster-2 \
  --enable-usb_blaster_libftdi \
  --enable-vsllink \
  CROSS=
%make_build

%install
%makeinstall_std
install -pm644 -D contrib/60-openocd.rules %buildroot%_udevrulesdir/60-openocd.rules

%pre
/usr/sbin/groupadd -r -f plugdev &>/dev/null ||:

%files
%doc AUTHORS BUGS ChangeLog HACKING NEWS* NEWTAPS
%doc README TODO
%doc %_datadir/%name/contrib/libdcc
%_udevrulesdir/*.rules
%_bindir/openocd
%_datadir/openocd
%exclude %_datadir/openocd/contrib
%_infodir/openocd.info*
%_mandir/man1/*

%changelog
* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt0.3
- v0.12.0-rc3

* Mon Oct 31 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt0.2
- v0.12.0-rc2

* Wed Sep 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt0.1
- v0.12.0-rc1

* Tue Aug 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt4
- v0.11.0-808-g9cd714cd1

* Mon Jun 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt3
- v0.11.0-715-g480d4e177

* Fri Mar 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt2
- 0.11.0 released

* Thu Dec 10 2020 Ildar Mulyukov <ildar@altlinux.ru> 0.11.0-alt1.rc1
- new version (git HEAD)

* Wed Sep 11 2019 Ildar Mulyukov <ildar@altlinux.ru> 0.10.0-alt1.git.930.g09eb941cb
- new version (git HEAD)

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
