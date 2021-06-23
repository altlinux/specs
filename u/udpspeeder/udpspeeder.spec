# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: udpspeeder
Version: 20210116.0
Release: alt1
Summary: Improve Network Quality using Forward Error Correction (FEC)
# - UDPspeeder license is MIT
# - libev license is BSD-2-Clause,GPL-2.0+
License: MIT and (BSD-2-Clause or GPL-2.0-or-later)
Group: Networking/Other
Url: https://github.com/wangyu-/UDPspeeder
Vcs: https://github.com/wangyu-/UDPspeeder.git

Source: %name-%version.tar
BuildRequires: gcc-c++

%description
A Tunnel which Improves your Network Quality on a High-latency Lossy
Link by using Forward Error Correction (FEC).

When used alone, UDPspeeder improves only UDP connection. Nevertheless,
if you used UDPspeeder + any UDP-based VPN together, you can improve
any traffic (including TCP/UDP/ICMP), currently OpenVPN/L2TP/ShadowVPN
are confirmed to be supported.

%prep
%setup
sed -i 's!\./this_program!speederv2!' main.cpp

%build
# Their own build system is so broken it's unusable.
echo "const char *gitversion = \"%version\";" > git_version.h
SOURCES="main.cpp log.cpp common.cpp lib/fec.cpp lib/rs.cpp packet.cpp
	delay_manager.cpp fd_manager.cpp connection.cpp fec_manager.cpp
	misc.cpp tunnel_client.cpp tunnel_server.cpp"
FLAGS="-Wall -Wextra -Wno-unused-variable -Wno-unused-parameter -Wno-missing-field-initializers"
# libev 4.24 (2016-11-16) is bundled.
LIBEV_ISBUNDLED="my_ev.cpp -isystem libev"
g++ %optflags -o speederv2 -I. $SOURCES $LIBEV_ISBUNDLED $FLAGS %(getconf LFS_CFLAGS)
# The software seems pristinely untouched by sanitizers nor static analyzers.

%install
install -Dp speederv2 %buildroot/%_bindir/speederv2

%files
%doc LICENSE.md README.md doc/udpspeeder_openvpn.md
%_bindir/speederv2

%changelog
* Tue Jun 22 2021 Vitaly Chikunov <vt@altlinux.org> 20210116.0-alt1
- First import of 20210116.0.
