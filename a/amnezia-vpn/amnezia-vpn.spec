%define git_commit_hash 477afb9d

%define sort_filter_proxy_model_commit f2881493e42bd7b7d5b7abe804dad084dd610b71
%define qtkeychain_commit 7460df6a978669290de5b56c2d98b199b61c3f88
%define qsimplecrypto_commit c99b33f0e08b7206116ddff85c22d3b97ce1e79d
%define amnezia_xray_bindings_version 1.1.0

Name: amnezia-vpn
Version: 4.8.18.0
Release: alt1

Summary: The best client for self-hosted VPN
License: GPL-3.0
Group: System/Servers

Url: https://amnezia.org/
Vcs: https://github.com/%name/amnezia-client
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/%name/amnezia-client/archive/%version/amnezia-client-%version.tar.gz
Source0: amnezia-client-%version.tar
# https://github.com/frankosterfeld/qtkeychain/archive/%sort_filter_proxy_model_commit/qtkeychain-%sort_filter_proxy_model_commit.tar.gz
Source1: SortFilterProxyModel-%sort_filter_proxy_model_commit.tar
# https://github.com/frankosterfeld/qtkeychain/archive/%qtkeychain_commit/qtkeychain-%qtkeychain_commit.tar.gz
Source2: qtkeychain-%qtkeychain_commit.tar
# https://github.com/%name/QSimpleCrypto/archive/%qsimplecrypto_commit/QSimpleCrypto-%qsimplecrypto_commit.tar.gz
Source3: QSimpleCrypto-%qsimplecrypto_commit.tar
# https://github.com/%name/amnezia-xray-bindings/archive/v%amnezia_xray_bindings_version/amnezia-xray-bindings-%amnezia_xray_bindings_version.tar.gz
Source4: amnezia-xray-bindings-%amnezia_xray_bindings_version.tar

Source5: vendor.tar

Patch0: %name-tun2-sudo.patch

BuildRequires: golang
BuildRequires: libsecret-devel
BuildRequires: libssh-devel
BuildRequires: libstdc++-devel-static
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-remoteobjects-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: zlib-devel

%description
Amnezia is an open-source VPN client, with a key feature that enables you to deploy your own VPN server on your server.

%package client
Summary: The best client for self-hosted VPN
Group: System/Servers
Requires: %name-service = %EVR
Requires: amnezia-tun2socks >= 2.5.4
Requires: amneziawg-go >= 0.2.18
Requires: cloak-client
Requires: libnss-resolve
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
%setup -n amnezia-client-%version -b 1 -b 2 -b 3 -b 4 -b 5
%patch0 -p1

%__mv -Tf ../SortFilterProxyModel-%sort_filter_proxy_model_commit client/3rd/SortFilterProxyModel
%__mv -Tf ../qtkeychain-%qtkeychain_commit client/3rd/qtkeychain
%__mv -Tf ../QSimpleCrypto-%qsimplecrypto_commit client/3rd/QSimpleCrypto

%__mv -Tf ../vendor ../amnezia-xray-bindings-%amnezia_xray_bindings_version/vendor

%build
# Export AGW public key and S3 endpoint for work VPN from Amnezia
export PROD_AGW_PUBLIC_KEY="-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAj5mxl/4DL3Sk89ntxs5G\nX3JawGQWIoq6rvNkOzNGuNgedNS2+pi6hZl3Izl1Io9om4KiUlMT6mgLO1hTr9q+\ns7CYhlvroFA7ErucF+9L+7FCt0Igi0kIK/R2/vxd/2HaUrorn/aSvvutkYwbfxqW\nSwtzE+RuBeDWGvEt937OW0oqYONPYv9E4T56Dz/EZ6v2t8ejAnKLbGD/GocMmipK\n7etFSiSMAB2RmaztqTq4NleBepfO80XpYlW9pCSXuHcE8wxHczkzxsbyMAMsG/K3\nvUQY6qPtohqqzSSBwa/8u2ptNHBeor7l7DdYXeR/Nqcc4z92VUkZ5lOVR4evkS5V\n/wQqp5tnOJEj3NjUhEhXFoNEapbZd1bh6iQoUk7jC1TdvKJ/nPKGZAsHRpr0rNKz\nfx/N/Oo6lr2yh/+ps6VxTkbPmB6E85WOO3UvjImZUY0XQdBjWle/4iJLdEC77Nr0\njXhdgeypucy6jkB6iBHMeVMlrNMEV7UxoBR/cCNx55zu/8sml5ByiDvCDT7sRomN\nNgVt5S/FaVjYuzFUifJ12ToChXFgESKFmuso7WluEaWvMIGREdrMrKQKHfYLOzWF\n2B5ZJDqw4o03fU4J/6rw61M1b+rjVpXMjPnzc2A+RgcjTvXv955gfZkwe4lt5wk/\n3j8zMVo3+zLrMTAaEeIUM0UCAwEAAQ==\n-----END PUBLIC KEY-----"
export PROD_S3_ENDPOINT="https://s3.eu-north-1.amazonaws.com/amnezia/, https://storage.googleapis.com/lambda-list/"

# Build amnezia xray bindings
pushd ../amnezia-xray-bindings-%amnezia_xray_bindings_version
%make_build
popd

# Fix utilites exec path
sed \
    -e 's|return Utils::executable("../../client/bin/openvpn", true);|return Utils::usrExecutable("openvpn");|' \
    -e 's|return Utils::executable("../../client/bin/tun2socks", true);|return Utils::usrExecutable("amnezia-tun2socks");|' \
    -i client/utilities.cpp

# Fix WireGuard GO exec path
sed -e 's|m_tunnel.start(appPath.filePath("../../client/bin/wireguard-go"), wgArgs);|m_tunnel.start("%_bindir/amneziawg-go", wgArgs);|' -i client/platforms/linux/daemon/wireguardutilslinux.cpp

# Fix update resolv conf path
sed -e 's|.arg(qApp->applicationDirPath());|.arg("%_libexecdir/%name");|' -i client/configurators/openvpn_configurator.cpp

# Use system libs instead 3rd prebuild
sed \
    -e 's|set(ZLIB_LIB_PATH "${LIBSSH_ROOT_DIR}/linux/x86_64/libz.a")|set(ZLIB_LIB_PATH "%_libdir/libz.so")|' \
    -e 's|set(LIBSSH_LIB_PATH "${LIBSSH_ROOT_DIR}/linux/x86_64/libssh.a")|set(LIBSSH_LIB_PATH "%_libdir/libssh.so")|' \
    -e 's|set(OPENSSL_INCLUDE_DIR "${OPENSSL_ROOT_DIR}/linux/include")|set(OPENSSL_INCLUDE_DIR "%_includedir")|' \
    -e 's|set(OPENSSL_LIB_SSL_PATH "${OPENSSL_ROOT_DIR}/linux/x86_64/libssl.a")|set(OPENSSL_LIB_SSL_PATH "%_libdir/libssl.so")|' \
    -e 's|set(OPENSSL_LIB_CRYPTO_PATH "${OPENSSL_ROOT_DIR}/linux/x86_64/libcrypto.a")|set(OPENSSL_LIB_CRYPTO_PATH "%_libdir/libcrypto.so")|' \
    -e 's|set(OPENSSL_USE_STATIC_LIBS TRUE)|set(OPENSSL_USE_STATIC_LIBS FALSE)|' \
    -i client/cmake/3rdparty.cmake
sed \
    -e 's|set(AMNEZIA_XRAY_ROOT_DIR "${CMAKE_CURRENT_LIST_DIR}/../../client/3rd-prebuilt/3rd-prebuilt/amnezia_xray")|set(AMNEZIA_XRAY_ROOT_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../amnezia-xray-bindings-%amnezia_xray_bindings_version")|' \
    -e 's|set(AMNEZIA_XRAY_LIB_PATH "${AMNEZIA_XRAY_ROOT_DIR}/linux/x86_64/amnezia_xray.a")|set(AMNEZIA_XRAY_LIB_PATH "${AMNEZIA_XRAY_ROOT_DIR}/build/amnezia_xray.a")|' \
    -e 's|set(AMNEZIA_XRAY_INCLUDE_DIR "${AMNEZIA_XRAY_ROOT_DIR}/linux/x86_64")|set(AMNEZIA_XRAY_INCLUDE_DIR "${AMNEZIA_XRAY_ROOT_DIR}/build")|' \
    -e 's|set(OPENSSL_INCLUDE_DIR "${OPENSSL_ROOT_DIR}/linux/include")|set(OPENSSL_INCLUDE_DIR "%_includedir")|' \
    -e 's|set(OPENSSL_LIB_CRYPTO_PATH "${OPENSSL_ROOT_DIR}/linux/x86_64/libcrypto.a")|set(OPENSSL_LIB_CRYPTO_PATH "%_libdir/libcrypto.so")|' \
    -e 's|set(OPENSSL_USE_STATIC_LIBS TRUE)|set(OPENSSL_USE_STATIC_LIBS FALSE)|' \
    -i service/server/CMakeLists.txt

# Set git commit
sed -e 's|add_definitions(-DGIT_COMMIT_HASH="${GIT_COMMIT_HASH}")|add_definitions(-DGIT_COMMIT_HASH="%git_commit_hash")|' -i client/CMakeLists.txt

# Build Amnezia VPN
%add_optflags -Wno-error=return-type
%cmake -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo
%cmake_build

%install
%__mkdir_p %buildroot{%_bindir,%_desktopdir,%_iconsdir/hicolor/512x512/apps,%_libexecdir/%name,%_unitdir}

%__install -Dp -m0755 %_cmake__builddir/client/AmneziaVPN %buildroot%_bindir/
%__install -Dp -m0644 deploy/data/linux/AmneziaVPN.png %buildroot%_iconsdir/hicolor/512x512/apps/

sed \
    -e 's|/usr/share/pixmaps/||' \
    -e 's|.png||' \
    deploy/installer/config/AmneziaVPN.desktop.in > %buildroot%_desktopdir/AmneziaVPN.desktop

sed -i '/Version=/d' %buildroot%_desktopdir/AmneziaVPN.desktop

sed \
    -e 's|/opt/AmneziaVPN/service/||' \
    -e 's|.sh||' \
    deploy/data/linux/AmneziaVPN.service > %buildroot%_unitdir/AmneziaVPN.service

sed -i '/Environment=/d' %buildroot%_unitdir/AmneziaVPN.service

%__install -Dp -m0755 %_cmake__builddir/service/server/AmneziaVPN-service %buildroot%_bindir/
%__install -Dp -m0755 deploy/data/linux/client/bin/update-resolv-conf.sh %buildroot%_libexecdir/%name/

%post service
%post_systemd_postponed AmneziaVPN.service

%preun service
%systemd_preun AmneziaVPN.service

%files client
%doc README.md README_RU.md
%_bindir/AmneziaVPN
%_desktopdir/AmneziaVPN.desktop
%_iconsdir/hicolor/512x512/apps/AmneziaVPN.png
%_libexecdir/%name

%files service
%_bindir/AmneziaVPN-service
%_unitdir/AmneziaVPN.service

%changelog
* Thu Jun 11 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.18.0-alt1
- Version 4.8.18.0

* Thu Apr 30 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.15.4-alt1
- Version 4.8.15.4

* Mon Mar 16 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.14.5-alt1
- Version 4.8.14.5

* Tue Feb 10 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.12.9-alt4
- Switch to use fork tun2socks from Amnezia for XRay protocol

* Mon Feb 09 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.12.9-alt3
- Fix work VPN from Amnezia

* Sat Feb 07 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.12.9-alt2
- Add AGW public key and S3 endpoint for work VPN from Amnezia (ALT #55896, #57788)

* Sat Jan 31 2026 Nazarov Denis <nenderus@altlinux.org> 4.8.12.9-alt1
- Version 4.8.12.9

* Thu Dec 11 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.11.4-alt1
- Version 4.8.11.4

* Tue Nov 11 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.10.0-alt2
- Fix DNS resolve (ALT #52679, #56803)

* Tue Sep 09 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.10.0-alt1
- Version 4.8.10.0

* Sun Aug 03 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.9.2-alt1
- Version 4.8.9.2
- Fix locale (ALT #55403)

* Thu Jul 10 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.8.3-alt1
- Version 4.8.8.3

* Wed Jul 09 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.7.2-alt2
- Fix interface tun2 with XRay (ALT #53992)

* Tue Jul 01 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.7.2-alt1
- Version 4.8.7.2 (ALT #54992)

* Sun Apr 06 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.5.0-alt1
- Version 4.8.5.0

* Mon Feb 24 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.3.1-alt1
- Version 4.8.3.1

* Wed Feb 19 2025 Nazarov Denis <nenderus@altlinux.org> 4.8.2.3-alt1.1
- Fix FTBFS

* Sat Nov 16 2024 Nazarov Denis <nenderus@altlinux.org> 4.8.2.3-alt1
- Version 4.8.2.3

* Mon Sep 30 2024 Nazarov Denis <nenderus@altlinux.org> 4.8.1.9-alt1
- Version 4.8.1.9

* Sat Sep 21 2024 Nazarov Denis <nenderus@altlinux.org> 4.8.1.0-alt1
- Version 4.8.1.0

* Fri Sep 20 2024 Nazarov Denis <nenderus@altlinux.org> 4.8.0.5-alt1
- Version 4.8.0.5

* Fri Sep 13 2024 Nazarov Denis <nenderus@altlinux.org> 4.8.0.1-alt1
- Version 4.8.0.1

* Thu Aug 22 2024 Nazarov Denis <nenderus@altlinux.org> 4.7.0.0-alt3
- Fix desktop file

* Wed Aug 21 2024 Nazarov Denis <nenderus@altlinux.org> 4.7.0.0-alt2
- Add patch for correct exec tun2socks path and require tun2socks and xray-core
- Move icon from pixmaps dir to icons dir
- Fix desktop file
- Restart service after update

* Tue Aug 20 2024 Nazarov Denis <nenderus@altlinux.org> 4.7.0.0-alt1
- Version 4.7.0.0

* Mon Aug 19 2024 Nazarov Denis <nenderus@altlinux.org> 4.6.0.3-alt6
- Add requires for Cloak client

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
