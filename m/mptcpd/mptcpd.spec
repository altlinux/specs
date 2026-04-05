# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%define _libexecdir %_prefix/libexec

Name: mptcpd
Version: 0.14
Release: alt1
Summary: Multipath TCP path management daemon
License: BSD-3-Clause and GPL-2.0-or-later
Group: Networking/Other
Url: https://mptcpd.mptcp.dev/
Vcs: https://github.com/multipath-tcp/mptcpd

Source: %name-%version.tar
BuildRequires: autoconf-archive
BuildRequires: libell-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: gcc-c++
}}

%description
The Multipath TCP Daemon - mptcpd - is a daemon for Linux based operating
systems that performs multipath TCP path management related operations
in the user space. It interacts with the Linux kernel through a generic
netlink connection to track per-connection information (e.g. available
remote addresses), available network interfaces, request new MPTCP
subflows, handle requests for subflows, etc.

NOTE: NetworkManager may already manage MPTCP in your system. This daemon
is usually recommended when NetworkManager 1.40 or newer is not available,
or when advanced per-connection path management is needed. Make sure
not to have both NetworkManager and mptcpd conflicting to configure the
MPTCP endpoints.

%package devel
Summary: %summary header files
Group: Development/C
Requires: %name = %EVR
License: BSD-3-Clause

%description devel
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--with-systemdsystemunitdir=%_unitdir \
	--with-kernel=upstream \
	%nil
%make_build

%install
%makeinstall_std
find %buildroot%_libdir -name '*.la' -delete

%check
./src/mptcpd --version | grep -Fx '%name %version'
%make_build check

%post
%post_systemd mptcp

%preun
%preun_systemd mptcp

%files
%doc AUTHORS COPYING ChangeLog LICENSES NEWS README.md SECURITY.md
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_bindir/mptcpize
%_libexecdir/mptcpd
%_libexecdir/mptcp-get-debug
%_libdir/libmptcpd.so.*
%_libdir/%name
%_libdir/mptcpize
%_unitdir/mptcp.service
%_man8dir/mptcpd.8*
%_man8dir/mptcpize.8*

%files devel
%_includedir/%name
%_libdir/libmptcpd.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Apr 05 2026 Vitaly Chikunov <vt@altlinux.org> 0.14-alt1
- Experimental import v0.14 (2025-12-19).
