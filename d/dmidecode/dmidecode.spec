Name: dmidecode
Version: 2.11
Release: alt1

Summary: Dmidecode is a tool for dumping a computer's DMI table
License: GPLv2+
Group: System/Kernel and hardware

URL: http://www.nongnu.org/dmidecode/
Source0: http://download.savannah.gnu.org/releases/dmidecode/dmidecode-%version.tar.bz2

%description
dmidecode reports information about x86 hardware as described in the system BIOS
according to the SMBIOS/DMI standard. This information typically includes system
manufacturer, model name, serial number, BIOS version, asset tag as well as a
lot of other details of varying level of interest and reliability depending on
the manufacturer.

This will often include usage status for the CPU sockets, expansion slots (e.g.
AGP, PCI, ISA) and memory module slots, and the list of I/O ports (e.g. serial,
parallel, USB).

%prep
%setup

%build
subst 's/-O./%optflags/' Makefile
%make_build

%install
%make_install DESTDIR=%buildroot prefix=/usr install-bin install-man

%files
%_sbindir/*
%_man8dir/*

%changelog
* Tue Jan 25 2011 Victor Forsiuk <force@altlinux.org> 2.11-alt1
- 2.11

* Tue Nov 25 2008 Victor Forsyuk <force@altlinux.org> 2.10-alt1
- 2.10

* Mon Mar 19 2007 Victor Forsyuk <force@altlinux.org> 2.9-alt1
- 2.9

* Mon Feb 06 2006 Victor Forsyuk <force@altlinux.ru> 2.8-alt1
- 2.8
- Build with default optflags and parallel make.
- More informative description.

* Tue Nov 30 2004 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version

* Tue Apr 20 2004 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- updated to 2.4
- tool renamed back to dmidecode

* Tue Oct 28 2003 Rider <rider@altlinux.ru> 2.3-alt1
- first build for Sisyphus
