Name: carps-cups
Version: 20180305
Release: alt1
License: GPLv3
Group: System/Configuration/Printing

Url: https://github.com/ondrej-zary/carps-cups
Source: %name-%version.tar
Patch: alt-use-destdir.patch

BuildRequires: cups cups-devel

Summary: CUPS driver for Canon CARPS printers
%description
This provides rastertocups filter and PPD files (specified by carps.drv file)
which allows these printers to print from Linux and possibly any other OS
where CUPS is used.

%prep
%setup
%patch -p2

%build
%make

%install
mkdir -p %buildroot%_prefix/lib/cups/filter/
mkdir -p %buildroot%_datadir/cups/{drv,usb}/

%make DESTDIR=%buildroot install

%files
%_prefix/lib/cups/filter/*
%_datadir/cups/drv/*
%_datadir/cups/usb/*

%changelog
* Fri Jun 29 2018 Oleg Solovyov <mcpain@altlinux.org> 20180305-alt1
- Initial build for ALT

