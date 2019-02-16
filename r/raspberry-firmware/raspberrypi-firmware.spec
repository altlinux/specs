%set_verify_elf_method no

Summary: bootloader and GPU firmware for Raspberry Pi
Name: raspberry-firmware
Version: 20190213
Release: alt1
Url: https://github.com/raspberrypi/firmware
License: distributable
Group: System/Kernel and hardware

ExclusiveArch: %arm aarch64

Source0: https://github.com/raspberrypi/firmware/raw/next/boot/bootcode.bin
Source1: https://github.com/raspberrypi/firmware/raw/next/boot/fixup.dat
Source2: https://github.com/raspberrypi/firmware/raw/next/boot/fixup_cd.dat
Source3: https://github.com/raspberrypi/firmware/raw/next/boot/fixup_db.dat
Source4: https://github.com/raspberrypi/firmware/raw/next/boot/fixup_x.dat
Source5: https://github.com/raspberrypi/firmware/raw/next/boot/start.elf
Source6: https://github.com/raspberrypi/firmware/raw/next/boot/start_cd.elf
Source7: https://github.com/raspberrypi/firmware/raw/next/boot/start_db.elf
Source8: https://github.com/raspberrypi/firmware/raw/next/boot/start_x.elf
Source9: https://github.com/raspberrypi/firmware/raw/next/boot/LICENCE.broadcom

Requires: u-boot-rpi3

%description
%summary

%install
%ifarch %arm
%define target %_datadir/u-boot/rpi_3_32b
%endif

%ifarch aarch64
%define target %_datadir/u-boot/rpi_3
%endif

%__install -d %buildroot/%target
%__install -m644 %SOURCE0 %buildroot/%target
%__install -m644 %SOURCE1 %buildroot/%target
%__install -m644 %SOURCE2 %buildroot/%target
%__install -m644 %SOURCE3 %buildroot/%target
%__install -m644 %SOURCE4 %buildroot/%target
%__install -m644 %SOURCE5 %buildroot/%target
%__install -m644 %SOURCE6 %buildroot/%target
%__install -m644 %SOURCE7 %buildroot/%target
%__install -m644 %SOURCE8 %buildroot/%target
%__install -d %buildroot/%_docdir/%name
%__install -m644 %SOURCE9 %buildroot/%_docdir/%name

echo 'enable_uart=1' > %buildroot/%target/config.txt

%files
%target/*
%doc %_docdir/%name

%changelog
* Sat Feb 16 2019 Anton Midyukov <antohami@altlinux.org> 20190213-alt1
- Initial build
