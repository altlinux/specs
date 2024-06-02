#
# spec file for package netvisix
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define hash 969fbcbcd74f
%define src_name bitbatzen-netvisix

Name:           netvisix
Version:        1.4.0
Release:        alt1
Summary:        Visualizes the network packet flow between hosts
License:        GPL-3.0+
Group:          Monitoring
Url:            https://bitbucket.org/bitbatzen/netvisix
Source0:        https://bitbucket.org/bitbatzen/netvisix/get/default.tar.bz2#/%src_name-%hash.tar.bz2
Source1:        %name.policy
Source2:        icon.png
Patch0:         %name-1.4.0_libtins.patch
BuildRequires:  gcc-c++
BuildRequires:  icon-theme-hicolor
BuildRequires:  libpcap-devel
BuildRequires:  qt5-base-devel
BuildRequires:  libtins-devel
BuildRequires:  polkit

%description
Netvisix listens on your local network interface and visualizes the network
packet flow between hosts. Also packet statistics per host are available.

Supported Protocols (colored and handeld in statistics): ARP, IPv4, IPv6, ICMP,
ICMPv6, IGMP, TCP, UDP, DNS, DHCP, DHCPv6

%prep
%setup -n %src_name-%hash

# Make sure, that libtins is not used
rm -rv libtins libtins-win

%patch0 -p2

# Fix files is compiled without RPM_OPT_FLAG
find . -type f -name \*.pro | while read file; do
echo "QMAKE_CXXFLAGS += %optflags %(pkg-config --cflags-only-I libtins)" >> "$file"; done

%build
pushd Netvisix
qmake-qt5 Netvisix.pro
%make_build
popd

%install
install -Dm 0755 Netvisix/Netvisix %buildroot%_bindir/%name
install -Dm 0644 %SOURCE2 %buildroot%_datadir/pixmaps/%name.png

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/pixmaps/%name.png

%changelog
* Sat Jun 01 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Build new version.

* Thu Dec 13 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Build new version.

* Sat May 23 2015 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- built for ALT Linux (based on openSUSE package)
