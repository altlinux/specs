%define _unpackaged_files_terminate_build 1
%define _libexecdir %_usr/libexec

Name: fcoe-utils
Version: 1.0.34
Release: alt1
Summary: Fibre Channel over Ethernet utilities

Group: Networking/Other
License: GPLv2
Url: https://github.com/openSUSE/fcoe-utils
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-systemd
BuildRequires: pkgconfig(lldpad) >= 0.9.46
BuildRequires: pkgconfig(pciaccess)
Requires: lldpad
Requires: iproute2
Requires: multipath-tools

%description
Fibre Channel over Ethernet utilities
fcoeadm - command line tool for configuring FCoE interfaces
fcoemon - service to configure DCB Ethernet QOS filters, works with dcbd

%prep
%setup
%patch -p1

# dropped support for software fcoe (fcoe.ko)
sed -i 's/^\(SUPPORTED_DRIVERS\)=".*"$/\1="bnx2fc qedf"/' etc/config
# make the defaults sane for supported offload drivers
sed -i 's/^\(DCB_REQUIRED\)=".*"$/\1="no"/' etc/cfg-ethx

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot/etc/init.d
mkdir -p %buildroot%_libexecdir/fcoe
for file in \
    contrib/*.sh \
    debug/*sh
    do install -m 755 $file %buildroot%_libexecdir/fcoe/
done

%post
%systemd_post fcoe.service fcoemon.socket
 
%preun
%systemd_preun fcoe.service fcoemon.socket
 
%postun
%systemd_postun_with_restart fcoe.service fcoemon.socket

%files
%doc README COPYING QUICKSTART
%_sbindir/*
%_man8dir/*
%_unitdir/*
%_sysconfdir/fcoe
%config(noreplace) %_sysconfdir/fcoe/cfg-ethx
%config(noreplace) %_sysconfdir/fcoe/config
%_datadir/bash-completion/completions/*
%_libexecdir/fcoe/

%changelog
* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.34-alt1
- Initial build.

