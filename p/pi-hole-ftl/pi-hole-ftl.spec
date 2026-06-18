# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    pi-hole-ftl
Version: 6.6.2
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
BuildRequires: pkgconfig(libidn2)
BuildRequires: libgmp-devel
BuildRequires: libidn-devel
BuildRequires: libmbedtls-3.6-devel
BuildRequires: libnettle-devel
BuildRequires: libreadline-devel libreadline-devel-static
BuildRequires: libunistring-devel
BuildRequires: xxd

Conflicts: dnsmasq

%define _name FTL
%define _servicename pihole-FTL
%define optflags_lto %nil

%description
FTLDNS (pihole-FTL) provides an interactive API and also generates statistics for Pi-hole Web interface.

%prep
%setup

%build
export GIT_BRANCH="master"
export GIT_HASH="82c58cc45435ddd77875daf368cf64398bc15966"
export GIT_VERSION="%version"
export GIT_DATE=""
export GIT_TAG="v%version"

sed -i "s/-Werror/-Wno-error/" src/CMakeLists.txt
# No libtermcap in ALT:
sed -i -e 's/ AND LIBTERMCAP//' -e 's/ ${LIBTERMCAP}//' src/CMakeLists.txt
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
* Thu Jun 18 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.6.2-alt1
- v6.6.2

* Tue Apr 07 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.6-alt1
- v6.6

* Thu Feb 19 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.5-alt1
- v6.5

* Fri Nov 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.4.1-alt1
- v6.4.1

* Wed Nov 26 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.3.3-alt1
- v6.3.3

* Tue Oct 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.3.2-alt1
- v6.3.2

* Sat Oct 18 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.2.3-alt2
- fix FTBFS with libmbedtls

* Tue Aug 05 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.2.3-alt1
- v6.2.3

* Tue Jun 10 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.2.2-alt1
- v6.2.2

* Mon Jun 02 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.2.1-alt1
- v6.2.1

* Thu Apr 03 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.1-alt1
- v6.1

* Mon Mar 17 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0.4-alt3
- drop dnsmasq dropin support (ALT #53462)

* Fri Mar 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0.4-alt2
- fix wrong Provides (ALT #53462)

* Mon Mar 10 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0.4-alt1
- v6.0.4

* Wed Feb 19 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0-alt1
- v6.0

* Fri Nov 08 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.25.2-alt1
- Initial build for ALT.

