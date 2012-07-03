Name: memmapper
Version: 1.42
Release: alt1

Summary: mmapper - access every resource attached to the machine
License: GPLv3
Group: System/Configuration/Hardware

URL: http://sourceforge.net/project/memmapper/
Source: http://download.sourceforge.net/memmapper/%name-%version.tar.gz
Patch1: memmapper-1.42-fixlinking.patch

Obsoletes: mmapper
Provides: mmapper = %version

# Automatically added by buildreq on Wed Oct 06 2010
BuildRequires: libudis86-devel

%description
mmapper allows to access every resource attached to the machine. It can read
and write any physical address on the memory bus, any I/O port and any field of
the PCI space configuration of any peripheral.

%prep
%setup
%patch1 -p1

%build
%make_build disassemble

%install
install -pD -m755 memmapper %buildroot%_sbindir/memmapper

%files
%_sbindir/%name

%changelog
* Sun Oct 31 2010 Victor Forsiuk <force@altlinux.org> 1.42-alt1
- 1.42
- Build with disassembler.

* Mon Sep 22 2008 L.A. Kostis <lakostis@altlinux.ru> 1.21-alt1
- new version.
- renamed to memmapper.

* Sun Apr 20 2008 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt1
- Initial build for ALTLinux.

