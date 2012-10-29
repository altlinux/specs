Name:    ucarp
Version: 1.5.2
Release: alt1
License: BSD
Group:	 System/Base
Packager: Alexei Takaseev <taf@altlinux.ru>
URL: http://www.ucarp.org

Source: %name-%version.tar

Summary: UCARP is a portable implementation of the CARP protocol. 

# Automatically added by buildreq on Thu Dec 13 2007
BuildRequires: libpcap-devel

%description
UCARP allows a couple of hosts to share common virtual IP addresses
in order to provide automatic failover. It is a portable userland
implementation of the secure and patent-free Common Address Redundancy
Protocol (CARP, OpenBSD's alternative to the patents-bloated VRRP).

%prep
%setup

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
* Mon Oct 29 2012 Alexei Takaseev <taf@altlinux.org> 1.5.2-alt1
- 1.5.2

* Fri Dec 14 2007 Alexey Gladkov <legion@altlinux.ru> 1.3-alt2
- Add docs and examples.

* Thu Dec 13 2007 Alexey Gladkov <legion@altlinux.ru> 1.3-alt1
- First build for ALT Linux.
