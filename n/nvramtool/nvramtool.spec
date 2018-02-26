Name: nvramtool
Version: 2.1
Release: alt1

Summary: coreboot utility program
Group: System/Kernel and hardware
License: GPL

Url: http://www.coreboot.org/Nvramtool
Source: %name.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

%description
nvramtool is a utility for reading/writing coreboot parameters
and displaying information from the coreboot table.

At boot time, coreboot places a table (known as the coreboot
table) in low physical memory.  The contents of this table are
preserved even after coreboot transfers control to the kernel and
the kernel initializes itself.  The coreboot table contains
various system information such as the type of mainboard in use.
It also specifies locations in the CMOS (nonvolatile RAM) where
the coreboot parameters are stored.

%prep
%setup -n %name

%build
%make

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.8 %buildroot%_man8dir/%name.8

%files
%doc ChangeLog README
%doc README
%_bindir/%name
%_man8dir/%name.8*

%changelog
* Mon Mar 28 2011 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- built for Sisyphus
  + based on Clustrx package by Eugene Ostapets
