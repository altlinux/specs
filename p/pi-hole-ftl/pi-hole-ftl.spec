# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    pi-hole-ftl
Version: 5.25.2
Release: alt1

Summary: The Pi-hole FTL engine
License: EUPL-1.2
Group:   System/Servers
Url:     https://github.com/pi-hole/ftl

Source: %name-%version.tar
Source1: %name.tmpfile
Source2: %name.sysuser
Source3: %name.conf
Source4: %name.service

BuildRequires(pre): cmake rpm-macros-cmake rpm-macros-systemd
BuildRequires: pkgconfig(sqlite3)
BuildRequires: libgmp-devel
BuildRequires: libidn-devel
BuildRequires: libnettle-devel
BuildRequires: libreadline-devel libreadline-devel-static
BuildRequires: xxd

Conflicts: dnsmasq < %EVR
Provides: dnsmasq = %EVR

%define _name FTL
%define _servicename pihole-FTL
%define optflags_lto %nil

%description
FTLDNS (pihole-FTL) provides an interactive API and also generates statistics for Pi-hole Web interface.

%prep
%setup

%build
export GIT_BRANCH="master"
export GIT_HASH="8943e26041c8730a5a9060eb64f76c6c2dd4e458"
export GIT_VERSION="%version"
export GIT_DATE=""
export GIT_TAG="v5.25.2"

sed -i "s/-Werror/-Wno-error/" src/CMakeLists.txt
sed -i 's/-DHAVE_READLINE /-DHAVE_READLINE=0 /' src/CMakeLists.txt
sed -i 's/-Wp,-D_FORTIFY_SOURCE=2/-Wp,-U_FORTIFY_SOURCE &/' src/CMakeLists.txt
%cmake
%cmake_build

%install
  install -Dm775 %_arch-alt-linux/pihole-FTL  %buildroot%_bindir/pihole-FTL

  install -Dm644 %SOURCE1 %buildroot%_tmpfilesdir/%name.conf
  install -Dm644 %SOURCE2 %buildroot%_sysusersdir/%name.conf

  install -dm775 %buildroot%_sysconfdir/pihole
  install -Dm644 %SOURCE3 %buildroot%_sysconfdir/pihole/pihole-FTL.conf
# install -Dm644 %name.db %buildroot%_sysconfdir/pihole/pihole-FTL.db
  install -Dm664 /dev/null %buildroot%_sysconfdir/pihole/dhcp.leases

  install -Dm644 %SOURCE4 %buildroot%_unitdir/%_servicename.service
  install -dm755 %buildroot%_unitdir/multi-user.target.wants
  ln -s ../%_servicename.service %buildroot%_unitdir/multi-user.target.wants/%_servicename.service

  # ver. 5.0 dnamasq dropin support
  pushd %buildroot%_bindir
  ln -s pihole-FTL dnsmasq
  popd

%pre
/usr/sbin/groupadd -r -f pihole ||:
/usr/sbin/useradd -g pihole -c 'FTL pseudouser' \
        -d %_cachedir/pihole -s /dev/null -r pihole >/dev/null 2>&1 ||:

%files
%doc *.md LICENSE
%_bindir/*
%_tmpfilesdir/%name.conf
%_sysusersdir/%name.conf
%_sysconfdir/pihole
%_unitdir/%_servicename.service
%_unitdir/multi-user.target.wants/%_servicename.service

%changelog
* Fri Nov 08 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.25.2-alt1
- Initial build for ALT.

