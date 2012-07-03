Name:    ucarp
Version: 1.3
Release: alt2
License: BSD
Group:	 System/Base
Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-alt-gratuitous-arp.patch

Summary: UCARP is a portable implementation of the CARP protocol. 

# Automatically added by buildreq on Thu Dec 13 2007
BuildRequires: libpcap-devel

%description
UCARP allows a couple of hosts to share common virtual IP addresses
in order to provide automatic failover. It is a portable userland
implementation of the secure and patent-free Common Address Redundancy
Protocol (CARP, OpenBSD's alternative to the patents-bloated VRRP).

%prep
%setup -q
%patch0 -p2

%build
%configure
%make_build

%install
%makeinstall
rm -rf -- %buildroot/%_datadir/locale

%files
%_sbindir/%name
%doc AUTHORS COPYING README examples/linux/*.sh

%changelog
* Fri Dec 14 2007 Alexey Gladkov <legion@altlinux.ru> 1.3-alt2
- Add docs and examples.

* Thu Dec 13 2007 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- First build for ALT Linux.
