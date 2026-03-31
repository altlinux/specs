%define _unpackaged_files_terminate_build 1
%define abiversion 2

Name: netopeer2
Version: 2.7.0
Release: alt1
Summary: NETCONF server implementation in C.
License: BSD-3-Clause
Group: Networking/Other
Url: https://github.com/CESNET/netopeer2

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-make
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: cmake gcc make
BuildRequires: pkg-config 
BuildRequires: libyang-devel
BuildRequires: libnetconf2-devel
BuildRequires: sysrepo-devel
BuildRequires: openssh-clients
BuildRequires: libcurl-devel
BuildRequires: libsystemd-devel
BuildRequires: libidn2-devel
BuildRequires: zlib-devel
BuildRequires: libbrotli-devel
BuildRequires: libzstd-devel
BuildRequires: libkrb5-devel
BuildRequires: libgnutls-devel
BuildRequires: libnettle-devel
BuildRequires: libtasn1-devel
BuildRequires: libp11-kit-devel
BuildRequires: libpsl-devel
BuildRequires: libgsasl-devel
BuildRequires: libssh2-devel
BuildRequires: libssl-devel
BuildRequires: libnghttp2-devel
BuildRequires: libngtcp2-devel
BuildRequires: libnghttp3-devel
BuildRequires: libcmocka-devel
%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif
BuildRequires: sysrepo-tools

Requires: libyang
Requires: libnetconf2
Requires: sysrepo

%description
Netopeer2 is a set of tools implementing NETCONF protocol as stated in RFC 6241,
6242, 6243, 6244 and 6246.
This package contains the Netopeer2 Server and the netopeer2-cli client.

%package -n %name-server
Summary: Serer files for %name
Group: Networking/Other
Requires: %name-cli

%description -n %name-server
%name-server is a server for implementing network configuration management based
on the NETCONF Protocol.


%package -n %name-cli
Summary: Command line tool for %name
Group: Security/Networking

%description -n %name-cli
Command line tool for %name

%prep
%setup -q
%autopatch -p1
subst "s|/usr/lib/systemd/system|%_unitdir|" CMakeLists.txt
subst 's|"\${CMAKE_INSTALL_SYSCONFDIR}/pam.d"|"%_sysconfdir/pam.d"|g' CMakeLists.txt
subst 's/common-auth/system-auth/g; s/common-account/system-auth/g; s/common-password/system-auth/g; s/common-session/system-auth/g' pam/netopeer2.conf

%build
export CFLAGS="%optflags"
%cmake \
   -DCMAKE_INSTALL_PREFIX=%_prefix \
   -DSYSREPO_SETUP=OFF 
%cmake_build

%install
%cmake_install

%files -n %name-server
%doc *.md
%config(noreplace) %_sysconfdir/pam.d/%name.conf
%_unitdir/%name-server.*
%_sbindir/%name-server
%_man8dir/%name-server.8.*
%_datadir/yang/modules/%name/
%_datadir/%name/scripts/*

%files -n %name-cli
%_bindir/%name-cli
%_man1dir/%name-cli.1.*

%changelog
* Sat Dec 20 2025 Pavel Shilov <zerospirit@altlinux.org> 2.7.0-alt1
- New version 2.7.0

* Wed Aug 20 2025 Pavel Shilov <zerospirit@altlinux.org> 2.4.5-alt1
- New version 2.4.5.

* Thu Aug 07 2025 Ivan A. Melnikov <iv@altlinux.org> 2.4.1-alt2
- NMU: don't require valgrind on architectures that it
  does not support (fixes FTBFS on loongarch64).

* Mon Aug 04 2025 Pavel Shilov <zerospirit@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus.

