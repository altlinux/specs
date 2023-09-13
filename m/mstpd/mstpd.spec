%define _unpackaged_files_terminate_build 1

Name: mstpd
Version: 0.1.0
Release: alt3

Summary: STP/RSTP/PVST+/MSTP Spanning Tree Protocol Daemon
License: GPLv2+
Group: Development/Other
URL: https://github.com/mstpd/mstpd.git

Source0: %name-%version.tar
Requires: bridge-utils

%description
This package provides a user-space daemon which replaces the STP handling that
is built into the Linux kernel Ethernet bridge and adds support for RSTP and
PVST+.

This daemon also supports participating in MSTP.  However, due to the way the
Linux kernel implements its FIBs, it is not currently possible to map MSTP
topologies onto Linux bridges.  Therefore, mstpd will not actually block ports
on Linux bridges when MSTP is used.

%prep
%setup -q
sed -i -e 's|mstpdpidfile=.*|mstpdpidfile=/run/mstpd.pid|g' Makefile.am

%build
%autoreconf
%configure --with-systemdunitdir=%_unitdir
%make_build

%install
%makeinstall_std
rm -fr %buildroot%_libexecdir/mstpctl-utils/ifquery
rm -fr %buildroot%_libexecdir/mstpctl-utils/mstp_config_bridge

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_man8dir/mstpctl.8*
%_man5dir/mstpctl-utils-interfaces.5*
%_defaultdocdir/mstpd
%_sbindir/mstpd
%_sbindir/mstpctl
%_sbindir/bridge-stp
%_sbindir/mstp_restart
%config(noreplace) %_sysconfdir/bridge-stp.conf
%_sysconfdir/bash_completion.d/mstpctl
%_unitdir/mstpd.service
%_libexecdir/mstpctl-utils

%changelog
* Mon Sep 11 2023 Oleg Obidin <nofex@altlinux.org> 0.1.0-alt3
- Remove unnecessary rpm-build-python3 BR

* Wed May 24 2023 Oleg Obidin <nofex@altlinux.org> 0.1.0-alt2
- Add requires bridge-utils (closes: 46237)

* Thu Apr 13 2023 Oleg Obidin <nofex@altlinux.org> 0.1.0-alt1
- First build for ALT
