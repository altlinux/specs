%define _unpackaged_files_terminate_build 1

Name: netdiscover
Version: 0.21
Release: alt1
Summary: A network address discovering/monitoring tool
License: GPL-3.0
Group: Monitoring
Url: https://github.com/netdiscover-scanner/netdiscover

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: dos2unix
BuildRequires: libpcap-devel
BuildRequires: hwdata-devel
BuildRequires: libnet2-devel 

%description
Netdiscover is a network address discovering tool,
developed mainly for those wireless networks without dhcp server,
it also works on hub/switched networks. Its based on arp packets,
it will send arp requests and sniff for replies.

%prep
%setup
%autopatch -p1

%build
autoreconf -fiv
%configure
cp -p %_datadir/hwdata/oui.txt ./oui.txt-$(date +%%Y%%m%%d)
sh update-oui-database.sh --no-download
%make_build

%install
%makeinstall_std

%files
%doc *.md README.rpm ChangeLog README AUTHORS NEWS TODO
%_sbindir/%name
%_man8dir/%name.8.*

%changelog
* Fri Sep 05 2025 Pavel Shilov <zerospirit@altlinux.org> 0.21-alt1
- Initial build for Sisyphus