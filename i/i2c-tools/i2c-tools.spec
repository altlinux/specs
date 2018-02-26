Name: i2c-tools
Version: 3.0.3
Release: alt1

Summary: I2C tools
License: GPL
Group: System/Kernel and hardware
Url: http://www.lm-sensors.org

Conflicts: lm_sensors < 3

Source: %name-%version-%release.tar

%description
%name package contains a heterogeneous set of I2C tools for Linux:
a bus probing tool, a chip dumper, register-level SMBus access helpers,
EEPROM decoding scripts, and EEPROM programming tools.

%prep
%setup

%build
make

%install
make install DESTDIR=%buildroot prefix=%prefix

%files
%doc COPYING README
%_bindir/*
%_sbindir/*
%_man8dir/*

%changelog
* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.3-alt1
- 3.0.3 released

* Sat Mar 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- initial release




