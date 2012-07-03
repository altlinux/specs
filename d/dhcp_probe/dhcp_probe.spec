Name: dhcp_probe
Version: 1.3.0
Release: alt1
Summary: Tool for discover DHCP and BootP servers
License: %bsdstyle
Group: Networking/Other
URL: http://www.net.princeton.edu/software/dhcp_probe/

Source0: %name-%version.tar

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Apr 12 2009
BuildRequires: libnet2-devel libpcap-devel

%description
dchp_probe attempts to discover DHCP and BootP servers on a directly-attached Ethernet network.
A network administrator can use this tool to locate unauthorized DHCP and BootP servers. 

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall
%__install -m 644 -D extras/dhcp_probe.cf.sample %buildroot%_sysconfdir/dhcp_probe.cf

%files
%doc INSTALL.dhcp_probe README COPYING
%_sbindir/%name
%config(noreplace) %_sysconfdir/dhcp_probe.cf
%_man8dir/*
%_man5dir/*

%changelog
* Sun Apr 12 2009 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- first build for Sisyphus
