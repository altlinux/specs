%define svndate 20081017

Name:  vrrpd
Version: 1.0
Release: alt2
Epoch: 1

Summary: VRRPd is an implementation of Virtual Router Redundancy Protocol
License: %gpl2plus
Group: Networking/Other
Url: http://sourceforge.net/projects/vrrpd/

Source0: %name-%version-%svndate.tgz
Source1: vrrpd_wrapper
Source2: vrrpd-etcnet.txt

Packager: Denis Kuznetsov <dek@altlinux.ru>

BuildRequires: rpm-build-licenses

Requires: etcnet perl-base

%description
 VRRPd is an implementation of Virtual Router Redundancy Protocol 
 as specified in rfc2338. VRRPd is interoperable with other RFC-based
 VRRP implementations, including Cisco and Juniper, and is included as
 a standard feature on ImageStream routers.


%prep
%setup -q -n %name-%version-%svndate

%build
%make_build

%install
mkdir -p %buildroot/%_sbindir
mkdir -p %buildroot/%_mandir/man8
install -pD -m755 vrrpd %buildroot/%_sbindir/%name
install -pD -m644 vrrpd.8 %buildroot/%_mandir/man8/vrrpd.8
install -pD -m755 %SOURCE1 %buildroot/%_sbindir/vrrpd_wrapper
install -pD -m644 %SOURCE2 vrrpd-etcnet.txt


%files
%_sbindir/%name
%_sbindir/vrrpd_wrapper
%_mandir/man8/%name.8.*

%doc Changes FAQ TODO README doc/draft-ietf-vrrp-spec-v2-05.txt doc/draft-jou-duplicate-ip-address-02.txt doc/rfc2338.txt.vrrp vrrpd-etcnet.txt

%changelog
* Sat Jan 30 2016 Sergey Y. Afonin <asy@altlinux.ru> 1:1.0-alt2
- Fixed FTBFS: changed .gz to .* for man page file

* Fri Jun 06 2014 Sergey Y. Afonin <asy@altlinux.ru> 1:1.0-alt1
- New version (svn trunk 2008-10-17)
- removed BuildArch definition
- added Url

* Thu Aug 09 2007 Denis Kuznetsov <dek@altlinux.ru> 01082007-alt3
- Started package
