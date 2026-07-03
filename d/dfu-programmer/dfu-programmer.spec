Summary: DFU Atmel USB programmer
Name: dfu-programmer
Version: 1.1.0
Release: alt1
License: GPLv2
Group: Development/Other
VCS: https://github.com/dfu-programmer/dfu-programmer
Source0: %name-%version.tar.gz

# Automatically added by buildreq on Wed Dec 25 2013
BuildRequires: libusb-devel ruby ruby-stdlibs

%description
dfu-programmer is an implementation of the Device Firmware Upgrade class
USB driver that enables firmware upgrades for various USB enabled (with the
correct bootloader) Atmel chips.  This program was created because the
Atmel "FLIP" program for flashing devices does not support flashing via USB
on Linux, and because standard DFU loaders do not work for Atmel's chips.

Check out the Atmel website for more information.  They are kind enough to
provide generally correct specifications this implementation is based on.

%prep
%setup

%build
touch ChangeLog
%autoreconf
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS *.txt NEWS *.md test
%_bindir/*
%_man1dir/*

%changelog
* Fri Jul 03 2026 Fr. Br. George <george@altlinux.org> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Wed Dec 25 2013 Grigory Milev <week@altlinux.ru> 0.6.2-alt1
- Initial build for ALTLinux
