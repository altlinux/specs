Name: lxbios
Version: 2.0.1
Release: alt0.1

Summary: LinuxBIOS utility program

Group: System/Base
License: GPL
Url: http://lxbios.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/lxbios/%name-%version.tar.bz2

%description
This program is a utility for reading/writing LinuxBIOS parameters and
displaying information from the LinuxBIOS table.

At boot time, LinuxBIOS places a table (referred to as the LinuxBIOS table)
in low physical memory.  The contents of this table are preserved even after
LinuxBIOS transfers control to the kernel and the kernel initializes itself.
The LinuxBIOS table contains various system information such as the type of
mainboard in use.  It also specifies locations in the CMOS (nonvolatile RAM)
where the LinuxBIOS parameters are stored.

%prep
%setup -q

%build
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -m755 lxbios %buildroot%_bindir/
cp lxbios.1.gz %buildroot%_man1dir/

%files
%doc ChangeLog README
%_bindir/%name
%_man1dir/*

%changelog
* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.1
- new version 2.0.1 (with rpmrb script)

* Sun Jan 22 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.1
- initial build for ALT Linux Sisyphus

