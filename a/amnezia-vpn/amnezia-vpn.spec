%define sort_filter_proxy_model_commit f2881493e42bd7b7d5b7abe804dad084dd610b71
%define qtkeychain_commit 74776e2a3e2d98d19943e0968901c5b5e04cc1bd

Name: amnezia-vpn
Version: 4.6.0.3
Release: alt5

Summary: The best client for self-hosted VPN
License: GPL-3.0
Group: System/Servers

Url: https://amnezia.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/amnezia-vpn/amnezia-client/archive/%version/amnezia-client-%version.tar.gz
Source0: amnezia-client-%version.tar
# https://github.com/frankosterfeld/qtkeychain/archive/%sort_filter_proxy_model_commit/qtkeychain-%sort_filter_proxy_model_commit.tar.gz
Source1: SortFilterProxyModel-%sort_filter_proxy_model_commit.tar
# https://github.com/frankosterfeld/qtkeychain/archive/%qtkeychain_commit/qtkeychain-%qtkeychain_commit.tar.gz
Source2: qtkeychain-%qtkeychain_commit.tar

Patch0: %name-use-system-libs-instead-3rd-prebuilt.patch
Patch1: %name-openvpn-exec-path.patch
Patch2: %name-update-resolv-conf-path.patch
Patch3: %name-wireguard-exec-path.patch

BuildRequires: cmake
BuildRequires: libsecret-devel
BuildRequires: libssh-devel
BuildRequires: libstdc++-devel-static
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-remoteobjects-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel

%description
Amnezia is an open-source VPN client, with a key feature that enables you to deploy your own VPN server on your server.

%package client
Summary: The best client for self-hosted VPN
Group: System/Servers
Requires: %name-service = %EVR
Requires: amneziawg-go
Requires: openvpn
Requires: qt6-5compat
Requires: qt6-declarative
Requires: qt6-svg
Requires: shadowsocks-libev

%description client
Amnezia is an open-source VPN client, with a key feature that enables you to deploy your own VPN server on your server.

%package service
Summary: The best client for self-hosted VPN (systemd service)
Group: System/Servers

%description service
Amnezia is an open-source VPN client, with a key feature that enables you to deploy your own VPN server on your server.

This package contains systemd service files.

%prep
%setup -n amnezia-client-%version -b 1 -b 2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%__mv -Tf ../SortFilterProxyModel-%sort_filter_proxy_model_commit client/3rd/SortFilterProxyModel
%__mv -Tf ../qtkeychain-%qtkeychain_commit client/3rd/qtkeychain

%build
%add_optflags -Wno-error=return-type
%cmake
%cmake_build

%install
%__mkdir_p %buildroot{%_bindir,%_desktopdir,%_libexecdir/%name,%_pixmapsdir,%_unitdir}

%__install -Dp -m0755 %_cmake__builddir/client/AmneziaVPN %buildroot%_bindir/
%__install -Dp -m0644 deploy/data/linux/AmneziaVPN.png %buildroot%_pixmapsdir/

sed \
    -e 's|@CMAKE_PROJECT_VERSION@|%version|' \
    -e 's|/usr/share/pixmaps/||' \
    -e 's|.png||' \
    deploy/installer/config/AmneziaVPN.desktop.in > %buildroot%_desktopdir/AmneziaVPN.desktop

sed \
    -e 's|/opt/AmneziaVPN/service/||' \
    -e 's|.sh||' \
    deploy/data/linux/AmneziaVPN.service > %buildroot%_unitdir/AmneziaVPN.service

sed -i '/Environment=/d' %buildroot%_unitdir/AmneziaVPN.service

%__install -Dp -m0755 %_cmake__builddir/service/server/AmneziaVPN-service %buildroot%_bindir/
%__install -Dp -m0755 deploy/data/linux/client/bin/update-resolv-conf.sh %buildroot%_libexecdir/%name/

%preun service
%preun_systemd AmneziaVPN

%files client
%doc README.md
%_bindir/AmneziaVPN
%_desktopdir/AmneziaVPN.desktop
%_libexecdir/%name
%_pixmapsdir/AmneziaVPN.png

%files service
%_bindir/AmneziaVPN-service
%_unitdir/AmneziaVPN.service

%changelog
* Sun Aug 18 2024 Nazarov Denis <nenderus@altlinux.org> 4.6.0.3-alt5
- Add patch for correct exec AmneziaWG path and require

* Sat Aug 17 2024 Nazarov Denis <nenderus@altlinux.org> 4.6.0.3-alt4
- Add patch for correct update resolv conf

* Thu Aug 15 2024 Nazarov Denis <nenderus@altlinux.org> 4.6.0.3-alt3
- Add patch for correct exec OpenVPN path and require
- Add requires for Shadowsocks client
- Stop service before uninstall

* Wed Aug 14 2024 Nazarov Denis <nenderus@altlinux.org> 4.6.0.3-alt2
- Added needed requires

* Tue Aug 13 2024 Nazarov Denis <nenderus@altlinux.org> 4.6.0.3-alt1
- Initial build for ALT Linux
