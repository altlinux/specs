Summary: DFU Atmel USB programmer
Name: dfu-programmer
Version: 0.6.2
Release: alt1
License: GPL
Group: Development/Other
URL: http://dfu-programmer.sourceforge.net
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
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
%_man1dir/*

%changelog
* Wed Dec 25 2013 Grigory Milev <week@altlinux.ru> 0.6.2-alt1
- Initial build for ALTLinux
