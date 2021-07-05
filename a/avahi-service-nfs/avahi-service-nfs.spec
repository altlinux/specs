%define avahi_service nfs
Name: avahi-service-%avahi_service
Version: 0.1
Release: alt1

Summary: Local network service discovery for %avahi_service
License: ALT-Public-Domain
Group: System/Servers
Url: https://www.altlinux.org/NFS
BuildArch: noarch

Requires: avahi-daemon

# there is also unfs3 in Sisyphus, but this is nfs3-only, not using 2049 port
#so not Recommends: nfs-server, but
Requires: nfs-server

%description
Avahi is a system which facilitates service discovery on
a local network -- this means that you can plug your laptop or
computer into a network and instantly be able to view other people
who you can chat with, find printers to print to or find files being
shared. This kind of technology is already found in MacOS X
(branded 'Rendezvous', 'Bonjour' and sometimes 'ZeroConf')
and is very convenient.

This package provides avahi daemon with a config file for %avahi_service service.
Install this package on your host if you want other hosts
to automatically discover %avahi_service on your host using avahi.

%prep

%build

%install
mkdir -p %buildroot%_sysconfdir/avahi/services
cat <<EOF > %buildroot%_sysconfdir/avahi/services/nfs.service
<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
<name replace-wildcards="yes">%h</name>
<service>
       <type>_nfs._tcp</type>
       <port>2049</port>
</service>
</service-group>
EOF

%files
%config %_sysconfdir/avahi/services/nfs.service

%changelog
* Mon Jul 05 2021 Igor Vlasenko <viy@altlinux.org> 0.1-alt1
- Sisyphus build

