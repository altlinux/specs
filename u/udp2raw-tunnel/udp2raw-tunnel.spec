Name: udp2raw-tunnel
Version: 20230206.0
Release: alt1

Summary: UDP over TCP/ICMP/UDP tunnel

# The following files are adapted from PolarSSL 1.3.19 (GPL-2.0)
#  lib/md5.cpp
#  lib/aes_acc/aesarm_table.h
#  lib/aes_acc/aesni.c
#  lib/aes_acc/aesacc.c
#  lib/aes_acc/aesni.h
# The following file is adapted from PolarSSL and is licenced under Apache-2.0 OR GPL-2.0
#  lib/pbkdf2-sha1.cpp
# Bundled libev is licenced under GPL-3.0+ or BSD-2-Clause

License: MIT
Group: Networking/Other
Url: https://github.com/wangyu-/udp2raw-tunnel

# Source-url: https://github.com/wangyu-/udp2raw-tunnel/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
Requires: iptables

%description
A tunnel which turns UDP traffic into encrypted UDP/FakeTCP/ICMP traffic
by using raw sockets that can help bypass UDP firewalls (or
unstable UDP environments).

%prep
%setup
%__subst 's|-ggdb||' makefile
%__subst 's|-static||' makefile
%__subst 's|$(shell git rev-parse HEAD)|%version|g' makefile
%__subst 's/\r$//' doc/README.zh-cn.md

%build
export OPT='%optflags'
%make_build

%install
install -D -m 0755 udp2raw %buildroot/%_bindir/udp2raw
install -D -m 0644 example.conf %buildroot/%_sysconfdir/udp2raw/example.conf

%files
%doc LICENSE.md
%doc README.md doc/*
%dir %_sysconfdir/udp2raw
%config(noreplace) %_sysconfdir/udp2raw/example.conf
%_bindir/udp2raw

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 20230206.0-alt1
- new version 20230206.0 (with rpmrb script)

* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 20200818.0-alt1
- initial build for ALT Sisyphus

* Wed Aug 19 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 20200818.0
  * Fixed FATAL:kernel too old (Issue 339) on x86 amd64 and
    possibly arm.
* Fri Jul 31 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 20200727.0
  * Fix issue 337(array out of boundary).
* Thu Jul 16 2020 Martin Hauke <mardnh@gmx.de>
- Update to version 20200715.0
  * further fix of GH#226. --fix-gro is no longer compatible with
    old versions.
  * fix a problem/bug in --cipher-mode aes128cfb, aes128cfb is
    redesigned and not compatible with old versions. The original
    aes128cfb is renamed to aes128cfb_0 and not suggested to use.
  * Fixed a bug which may cause bind port fail in log and the
    program to exit by itself.
* Tue Mar 26 2019 Martin Hauke <mardnh@gmx.de>
- Clarify license
* Fri Mar 15 2019 Jan Engelhardt <jengelh@inai.de>
- Fix spellos in descriptions.
* Mon Feb 25 2019 Martin Hauke <mardnh@gmx.de>
- Initial package, version 20181113.0
