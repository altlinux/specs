%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _udevrulesdir /lib/udev/rules.d

Name: ponyprog
Version: 3.1.4
Release: alt2

Summary: Serial device programmer
License: GPL-2.0
Group: Engineering
Url: https://github.com/lancos/ponyprog

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: libftdi1-devel

%description
PonyProg is a serial device programmer software with a user friendly GUI
framework available for Windows and Linux. It's purpose is reading and
writing every serial device. With PonyProg and SI-Prog you can program
Wafercard for SAT, eeprom within GSM, TV or CAR-RADIO. Furthermore it
can be used as a low cost starter kit for PIC and AVR.

Ponyprog supports AVR, SPI eeprom, AVR micro, 12C bus 8bit eeprom,
PIC 16 micro, PIC 12 micro, AT89S micro and SDE2506 eeprom family chips.
You can open any HEX, e2p, mot, csm, rom, eep, bin files and burn them
to uC or PIC. You can even backup the old program on the chip using
Ponyprog. Ponyprog enables the user to write, verify and erase data
on the microchip.

Also setting fuse bits and locks using Ponyprog is possible.
You can save any HEX file to BIN file or eep file, BIN file to HEX
file or MOT file and vice versa so you can use Ponyprog as converter
too. Ponyprog offers serial or parallel port programming for uC's.
You can even change polarity of control lines without touching the
wires using I/O port setup.

%prep
%setup -a1
%patch -p1
sed -i "s|Categories=.*|Categories=Qt;Development;Electronics;|" desktop/ponyprog.desktop

%build
%cmake \
       -DUDEV_INSTALL_DIR=%_udevrulesdir
%cmake_build

%install
%cmake_install

# install scalable icon
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps/
cp -v icons/ponyprog.svg %buildroot%_iconsdir/hicolor/scalable/apps/

%files
%doc README.md Screenshot.png
%_bindir/ponyprog
%_udevrulesdir/90-ponyprog.rules
%_desktopdir/ponyprog.desktop
%_iconsdir/ponyprog.png
%_iconsdir/hicolor/scalable/apps/ponyprog.svg
%dir %_datadir/doc/ponyprog
%_datadir/doc/ponyprog/*
%dir %_datadir/ponyprog
%_datadir/ponyprog/*

%changelog
* Thu May 28 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.4-alt2
- Applied repocop fix for sisyphus_check.
- Place package in Engineering group.

* Wed May 27 2026 Nikolay Strelkov <snk@altlinux.org> 3.1.4-alt1
- Initial build for Sisyphus
