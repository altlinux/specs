%define soname 1
Name: flashrom
Version: 1.3.0
Release: alt1

Summary: Universal flash programming utility
License: GPLv2
Group: System/Kernel and hardware

Url: http://flashrom.org/Flashrom
# Homepage: http://www.flashrom.org
# https://review.coreboot.org/flashrom.git
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libftdi1-devel libpci-devel zlib-devel libusb-devel
BuildRequires: libjaylink-devel libcmocka-devel
BuildRequires: gcc meson

%description
flashrom is a tool for identifying, reading, writing,
verifying and erasing flash chips. It's often used to flash
BIOS/EFI/coreboot/firmware/optionROM images in-system using a
supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices
which can program flash chips.

It supports a wide range of DIP32, PLCC32, DIP8, SO8/SOIC8,
TSOP32/40/48, and BGA chips, which use various protocols such as
LPC, FWH, parallel flash, or SPI.

The tool can be used to flash BIOS/firmware images for example --
be it proprietary BIOS images or coreboot (previously known as
LinuxBIOS) images.

It can also be used to read the current existing BIOS/firmware
from a flash chip.

%package -n libflashrom%soname
Summary: Shared library for %name
Group: System/Libraries
Requires: %name = %EVR

%description -n libflashrom%soname
Shared library for %name.

flashrom is a tool for identifying, reading, writing,
verifying and erasing flash chips. It's often used to flash
BIOS/EFI/coreboot/firmware/optionROM images in-system using a
supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices
which can program flash chips.

It supports a wide range of DIP32, PLCC32, DIP8, SO8/SOIC8,
TSOP32/40/48, and BGA chips, which use various protocols such as
LPC, FWH, parallel flash, or SPI.

The tool can be used to flash BIOS/firmware images for example --
be it proprietary BIOS images or coreboot (previously known as
LinuxBIOS) images.

It can also be used to read the current existing BIOS/firmware
from a flash chip.


%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
Files for development with %{name}.

%prep
%setup
%patch0 -p1

%build
echo "VERSION = %version" >versioninfo.inc
echo "MAN_DATE = `date '+%%Y-%%m-%%d'`">>versioninfo.inc
sed -e 's/MODE="[0-9]*", GROUP="plugdev"/TAG+="uaccess"/g' util/flashrom_udev.rules -i
%meson \
%ifarch %{ix86} x86_64
  -Dprogrammer=[\'auto\',\'jlink_spi\']
%endif
%meson_build

%install
%meson_install
install -D -p -m 0644 util/flashrom_udev.rules %buildroot/%_udevrulesdir/60_flashrom.rules
rm -f %buildroot%_libdir/libflashrom.a

%files
%doc README
%_udevrulesdir/60_flashrom.rules
%_sbindir/*
%_man8dir/*

%files -n libflashrom%soname
%_libdir/libflashrom.so.%{soname}*

%files -n libflashrom-devel
%_libdir/libflashrom.so
%_includedir/libflashrom.h
%_pkgconfigdir/flashrom.pc

%changelog
* Fri Mar 17 2023 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt1
- 1.3.0.

* Wed Nov 17 2021 Anton Farygin <rider@altlinux.ru> 1.3-alt2
- added the shared library and its devel package
- migrated to meson in build and install sections

* Tue Jul 13 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.3-alt1
- Update to latest stable branch 1.3.x

* Tue Jul 13 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt2
- Fix building on aarch64 (Closes: 40470)

* Tue Jun 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt1
- The first and hopefully not the last release of 2020
- Support MT25QU256 for Baikal-M firmware

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.0 -> 1.1

* Fri May 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Updated to upstream version 1.0.

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.9-alt2
- Updated build dependencies.

* Thu Mar 17 2016 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- new version (watch file uupdate)

* Mon Mar 02 2015 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- new version (watch file uupdate)

* Sat Aug 17 2013 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- new version (watch file uupdate)
- added FTDI support

* Thu Aug 23 2012 Michael Shigorin <mike@altlinux.org> 0.9.6.1-alt1
- new version (watch file uupdate)

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.9.5.2-alt1
- 0.9.5.2

* Fri Mar 02 2012 Michael Shigorin <mike@altlinux.org> 0.9.5.1-alt1
- 0.9.5.1

* Sat Oct 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1
- new version (uupdate from watch file)

* Sat Jan 24 2009 Led <led@altlinux.ru> 0.0-alt0.1
- initial build
