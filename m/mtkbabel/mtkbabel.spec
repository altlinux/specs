Name: mtkbabel
Version: 0.8
Release: alt1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Program to Operate the i-Blue 747 GPS Data Logger
License: GPL v2 or later
Group: Sciences/Geosciences
Url: http://www.rigacci.org/wiki/doku.php/doc/appunti/hardware/gps_logger_i_blue_747

# see http://sourceforge.net/projects/mtkbabel
Source: %name-%version.tar
# for findreq
BuildRequires: perl-Device-SerialPort perl-TimeDate

BuildArch: noarch

%description
MTKBabel is a Perl program to operate the i-Blue 747 GPS data logger
and Holux M-241 data logger. It should work also with other GPS devices
based on the MediaTek MTK chipset.

The main capabilities are:
  * Command line interface
  * Save data log in GPX and raw binary format
  * If required retrieve all the data, also the old one being overlapped
  * Change logging criteria: time, distance, speed
  * Change log format
  * START/STOP logging
  * Set OVERLAP or STOP method on memory full
  * Erase the internal memory

%prep
%setup -q

%build
%install
install -D -m0755 %name %buildroot%_bindir/%name
install -D -m0644 %name.1 %buildroot%_mandir/man1/%name.1

%files
%doc MtkExtensionsv1.xsd README changelog
%_bindir/*
%doc %_man1dir/*

%changelog
* Sun Jun 14 2009 Grigory Batalov <bga@altlinux.ru> 0.8-alt1
- Built for ALT Linux.

* Fri Jul 11 2008 Dirk Stöcker <opensuse@dstoecker.de> 0.7
- Update to 0.7
* Mon Jun  2 2008 utx@penguin.cz
- Created new package, version 0.6.
