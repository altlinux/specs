# Spec file for br2684ctl utility

%define version 20040226
%define release alt1

Name: br2684ctl
 
Version: %version
Release: %release
    
Summary: utility for configuring RFC 2684 ATM/Ethernet bridging

License: GPLv2
Group: System/Kernel and hardware
URL: http://home.sch.bme.hu/~cell/br2684/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: br2684ctl_20040226.orig.tar.gz
Source1: Makefile
Source2: README.ALT
Patch0: br2684ctl.c.diff
Patch1: br2684ctl.8.diff

AutoReqProv: yes
BuildPreReq: libatm-devel glibc-kernheaders

%description
ATM bridging is a way to extend Ethernet over an ATM network and
is mainly used for  DSL connections.  This package  contains the
user space utility needed to configure the kernel driver br2684. 

This package is needed if you own an USB DSL modem and your 
connection uses one of these protocols:  RFC  1483  bridged 
(RFC 2684 bridged), PPP over Ethernet (PPPoE).

%prep
%setup -n %name-%version.orig
%patch0 -p1
%patch1

cp -- %SOURCE1 Makefile
cp -- %SOURCE2 README.ALT

mv -f -- COPYING COPYING.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%make_build

%install
mkdir -p -- %buildroot%_sbindir
mkdir -p -- %buildroot%_man8dir
install -m 0750 -- %name %buildroot%_sbindir/
install -m 0644 -- %name.8 %buildroot%_man8dir/

%files
%doc README.ALT
%doc --no-dereference COPYING
%_sbindir/%name
%_mandir/man8/*

%changelog
* Mon Jan 08 2007 Nikolay A. Fetisov <naf@altlinux.ru> 20040226-alt1
- Initial build for ALT Linux Sisyphus

* Tue May 30 2006 Nikolay A. Fetisov <naf@altlinux.ru> 20040226-alt0
- Initial build

