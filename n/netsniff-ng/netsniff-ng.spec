# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: netsniff-ng
Version: 0.6.9
Release: alt1
Summary: A Swiss army knife for your daily Linux network plumbing
License: GPL-2.0-only
Group: Networking/Other
Url: http://netsniff-ng.org
Vcs: https://github.com/netsniff-ng/netsniff-ng

Source: %name-%version.tar

BuildRequires: bison
BuildRequires: flex
BuildRequires: libcli-devel
BuildRequires: libnet-devel
BuildRequires: libnetfilter_conntrack-devel
BuildRequires: libnl-devel
BuildRequires: libpcap-devel
BuildRequires: libsodium-devel
BuildRequires: libuserspace-rcu
BuildRequires: libuserspace-rcu-devel
BuildRequires: ncurses-devel
BuildRequires: perl-podlators
BuildRequires: zlib-devel

%description
netsniff-ng is a free, performant       .      .
Linux network analyzer and             /(      )\
networking toolkit. If you will,     .' {______} '.
the Swiss army knife for network      \ ^,    ,^ /
packets.                               |'O\  /O'|   _.<0101011>--
                                       > `'  '` <  /
The gain of performance is             ) ,.==., (  |
reached by built-in zero-copy       .-(|/--~~--\|)-'
mechanisms, so that on packet      (      ___
reception and transmission the      \__.=|___E
kernel does not need to copy
from kernel space to user space, and vice versa.

The netsniff-ng toolkit's primary usage goal is to facilitate a network
developer's / hacker's daily Linux plumbing. It can be used for network
development, debugging, analysis, auditing or network reconnaissance. It
consists of the following fixed set of utilities:

 * netsniff-ng: a zero-copy packet analyzer, pcap capturing/replaying tool
 * trafgen: a multithreaded low-level zero-copy network packet generator
 * mausezahn: high-level packet generator for appliances with Cisco-CLI
 * ifpps: a top-like kernel networking and system statistics tool
 * curvetun: a lightweight curve25519-based multiuser IP tunnel
 * astraceroute: an autonomous system trace route and DPI testing utility
 * flowtop: a top-like netfilter connection tracking tool
 * bpfc: a [seccomp-]BPF (Berkeley packet filter) compiler, JIT disassembler

%prep
%setup
sed -i '/_version/s/(none)/%version-%release/' configure

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
./configure --disable-geoip
%make_build CFLAGS='%optflags' Q=

%install
%makeinstall_std PREFIX=%_prefix

%check
%buildroot%_sbindir/netsniff-ng --version | grep '^%name %version '

%files
%define _customdocdir %_docdir/%name
%doc AUTHORS COPYING README
%_sbindir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_man8dir/*.8*

%changelog
* Sat Dec 13 2025 Vitaly Chikunov <vt@altlinux.org> 0.6.9-alt1
- First import v0.6.9-9-g1af7ae3 (2025-06-11).
