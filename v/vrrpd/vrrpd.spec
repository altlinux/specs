Name:  vrrpd
Version: 01082007
Release: alt3

Summary: VRRPd is an implementation of Virtual Router Redundancy Protocol
License: GPL
Group: Networking/Other
BuildArch: i586
Source0: %name-%version.tgz
Source1: vrrpd_wrapper
Source2: vrrpd-etcnet.txt
Packager: Denis Kuznetsov <dek@altlinux.ru>
Requires: etcnet
Requires: perl-base

%description
 VRRPd is an implementation of Virtual Router Redundancy Protocol 
 as specified in rfc2338. VRRPd is interoperable with other RFC-based
 VRRP implementations, including Cisco and Juniper, and is included as
 a standard feature on ImageStream routers.


%prep
%setup -q

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
%_mandir/man8/%name.8.gz

%doc Changes FAQ TODO doc/draft-ietf-vrrp-spec-v2-05.txt doc/draft-jou-duplicate-ip-address-02.txt doc/rfc2338.txt.vrrp vrrpd-etcnet.txt

%changelog
* Thu Aug 09 2007 Denis Kuznetsov <dek@altlinux.ru> 01082007-alt3
- Started package
