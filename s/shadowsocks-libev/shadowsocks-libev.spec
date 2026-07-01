# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: shadowsocks-libev
Version: 3.3.6
Release: alt1
Summary: A fast tunnel proxy that helps you bypass firewalls
License: GPL-3.0-or-later
Group: Security/Networking
Url: https://shadowsocks.org/
Vcs: https://github.com/shadowsocks/shadowsocks-libev

Source: %name-%version.tar
Source1: libbloom-0.tar
Source2: libcork-0.tar
Source3: libipset-0.tar
Patch: shadowsocks-libev-3.3.5-gcc13-comp.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: asciidoc
BuildRequires: libcares-devel
BuildRequires: libev-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libpcre-devel
BuildRequires: libsodium-devel
BuildRequires: libssl-devel
BuildRequires: xmlto
BuildRequires: gcc-c++
BuildRequires: libpcre2-devel
%{?!_without_check:%{?!_disable_check:BuildRequires: banner curl}}

%description
%summary.

This is a legacy version, use shadowsocks-rust for a new version.

%package devel
Summary: %summary
Group: Development/C
Requires: lib%name = %EVR

%description devel
%summary.

%package -n lib%name
Summary: %summary
Group: System/Libraries

%description -n lib%name
%summary.

%prep
%setup
%autopatch -p1
tar xf %SOURCE1 -C .
tar xf %SOURCE2 -C .
tar xf %SOURCE3 -C .

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake -DWITH_STATIC=OFF
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_datadir/doc/%name
mkdir -p %buildroot%_unitdir %buildroot%_sysconfdir/%name %buildroot%_sysconfdir/sysctl.d
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-local.service
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-server.service
install -m0640 .gear/*.json %buildroot%_sysconfdir/%name
install -m0644 .gear/sysctl.conf* %buildroot%_sysconfdir/sysctl.d/88-%name.conf.example

%check
.gear/ss-test.sh

%post
%post_service %name-local
%post_service %name-server

%preun
%preun_service %name-local
%preun_service %name-server

%files
%doc Changes COPYING AUTHORS README.md LICENSE
%attr(750,root,wheel) %dir %_sysconfdir/%name
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/%name/*
%config %_sysconfdir/sysctl.d/*
%_unitdir/*.service
%_bindir/ss-*
%_man1dir/ss-*.1*
%_man8dir/%name.8*

%files devel
%_includedir/shadowsocks.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files -n lib%name
%_libdir/lib%name.so.*

%changelog
* Wed Jul 01 2026 Anton Vyatkin <toni@altlinux.org> 3.3.6-alt1
- New version 3.3.6.

* Wed Jun 17 2026 Anton Vyatkin <toni@altlinux.org> 3.3.5-alt5
- Fix FTBFS.

* Sun Mar 20 2022 Vitaly Chikunov <vt@altlinux.org> 3.3.5-alt4
- Hardened systemd units and configs (latter are made non-world readable).

* Sat Mar 19 2022 Vitaly Chikunov <vt@altlinux.org> 3.3.5-alt3
- Disable stream ciphers.
- Add simple testing in %%check.

* Fri Mar 18 2022 Vitaly Chikunov <vt@altlinux.org> 3.3.5-alt2
- Rename client to local in config and systemd units.

* Mon Mar 14 2022 Vitaly Chikunov <vt@altlinux.org> 3.3.5-alt1
- First import v3.3.5-34-g46382c2 (2022-02-15).
