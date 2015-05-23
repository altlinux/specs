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

%define hash 7f2d83bca3ae
%define src_name bitbatzen-netvisix

Name: netvisix
Version: 1.2.0
Release: alt1

Summary: Visualizes the network packet flow between hosts
License: GPLv3+
Group: Monitoring

Url: https://bitbucket.org/bitbatzen/netvisix
Source0: https://bitbucket.org/bitbatzen/netvisix/get/default.tar.bz2#/%src_name-%hash.tar.bz2
Source1: %name.policy
Source2: icon.png
# PATCH-FIX-OPENSUSE libtins.patch avvissu@yandex.ru -- Use package from openSUSE instead of static library
Patch: netvisix-1.1.0_libtins.patch

BuildRequires: dos2unix
BuildRequires: gcc-c++
BuildRequires: icon-theme-hicolor
BuildRequires: libpcap-devel
#BuildRequires: update-desktop-files
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires: pkgconfig(libtins)
BuildRequires: polkit

%description
Netvisix listens on your local network interface and visualizes
the network packet flow between hosts. Per host packet statistics
are available either.

Supported Protocols (colored and handled in statistics):
ARP, IPv4, IPv6, ICMP, ICMPv6, IGMP, TCP, UDP, DNS, DHCP, DHCPv6

%prep
%setup -n %src_name-%hash
%patch -p1

dos2unix -k README.md

# Fix files is compiled without RPM_OPT_FLAG
find . -type f -name \*.pro | while read FILE; do
echo "QMAKE_CXXFLAGS += %optflags" >> "$FILE"; done

%build
pushd Build
qmake-qt5 ../Netvisix/Netvisix.pro
make %{?_smp_mflags} PREFIX=%_prefix
popd

%install
install -pDm755 Build/Netvisix %buildroot%_bindir/%name
install -pDm644 %SOURCE1 %buildroot%_datadir/polkit-1/actions/org.opensuse.policykit.%name.policy
install -pDm644 %SOURCE2 %buildroot%_datadir/pixmaps/%name.png
#suse_update_desktop_file -c %name Netvisix "Visualizes the network packet flow" 'pkexec %_bindir/%name' %name Qt Network Monitor

%files
%doc AUTHOR COPYING README*
%_bindir/%name
#_datadir/polkit-1/actions/org.opensuse.policykit.%name.policy
%_datadir/pixmaps/%name.png
#_desktopdir/%name.desktop

# TODO:
# - adapt pkexec/.desktop part too

%changelog
* Sat May 23 2015 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- built for ALT Linux (based on openSUSE package)

* Fri May 22 2015 avvissu@yandex.ru
- Update to 1.2.0:
  * add http protocol handling
  * improved dns/hostname handling
* Fri May 15 2015 avvissu@yandex.ru
- Update to 1.1.0:
  * added hostname lookup (optional)
  * minor display changes
- Add BuildRequires: pkgconfig(Qt5Network)
* Thu May  7 2015 avvissu@yandex.ru
- Initial release
