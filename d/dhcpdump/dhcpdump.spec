# Spec file for dhcpdump utility

Name: dhcpdump

Version: 1.8
Release: alt2

Summary: DHCP packet dumper

#%%artistic_license
License: %bsdstyle
Group: Networking/Other
URL: http://www.mavetju.org/unix/dhcpdump-man.php
#URL: http://www.mavetju.org/download/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-1.8-debian.patch

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: libpcap-devel perl-Pod-Parser

%description
dhcpdump package provides a tool for visualization of DHCP
packets to analyze DHCP server responses.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
mkdir -p -- %buildroot{%_sbindir,%_man8dir}
install -m 0755 -- %name %buildroot%_sbindir/
install -m 0755 -- %name.8 %buildroot%_man8dir/

%files
%doc CONTACT LICENSE CHANGES
%_sbindir/%name
%_man8dir/*

%changelog
* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt2
- fix build with perl 5.12

* Wed Oct 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- Initial build

