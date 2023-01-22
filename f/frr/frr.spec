%define _unpackaged_files_terminate_build 1
%filter_from_requires /.etc.default.frr/d
%filter_from_requires /.etc.sysconfig.frr/d

%define _localstatedir /var
%define _runtimedir /run
%define frr_user frr
%define frr_group frr
%define frrvty_group frrvty
%define frr_home %_localstatedir/lib/%name
%define frr_statedir %_runtimedir/%name
%define frr_daemondir %_prefix/lib/%name
%define frr_moduledir %_libdir/%name/modules
%define frr_libdir %_libdir/%name

%def_enable doc
%def_enable doc_html
%def_disable tcmalloc
%def_enable snmp
%def_disable config_rollbacks
%def_disable grpc
%def_disable zeromq
%def_with libpam
%def_disable ospfapi
%def_disable ospfclient
%def_disable shell_access
%def_disable realms
%def_enable fpm
%def_disable pcreposix
%def_disable cumulus
%def_disable datacenter
%def_disable protobuf
%def_disable rpki
%def_disable scripting
%def_disable backtrace
%def_disable dp_dpdk

Name: frr
Version: 8.4.2
Release: alt1
Summary: FRRouting Routing daemon
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Group: Networking/Other
Url: http://www.frrouting.org
Vcs: https://github.com/FRRouting/frr.git
Source0: %name-%version.tar
Source1: %name-tmpfiles.conf
#Patch: %%name-%%version.patch
Patch0001: 0001-update-init-script.patch

BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc-c++
BuildRequires: bison >= 2.7
BuildRequires: flex
BuildRequires: python3-devel
BuildRequires: libjson-c-devel
BuildRequires: pkgconfig(libcares)
BuildRequires: libelf-devel
BuildRequires: libreadline-devel
BuildRequires: pkgconfig(libyang) >= 2.0.0
BuildRequires: libcap-devel
BuildRequires: makeinfo
%{?_enable_doc:BuildRequires: python3-module-sphinx}
%{?_enable_tcmalloc:BuildRequires: libgperftools-devel}
%{?_enable_scripting:BuildRequires: liblua5.3-devel}
%{?_enable_snmp:BuildRequires: libnet-snmp-devel}
%{?_with_libpam:BuildRequires: libpam-devel}
%{?_enable_pcreposix:BuildRequires: libpcre-devel}
%{?_enable_config_rollbacks:BuildRequires: pkgconfig(sqlite3)}
%{?_enable_grpc:BuildRequires: pkgconfig(grpc) >= 6.0.0 pkgconfig(grpc++) >= 1.16.1 pkgconfig(protobuf) >= 3.6.1 /usr/bin/protoc}
%{?_enable_zeromq:BuildRequires: pkgconfig(libzmq) >= 4.0.0}
%{?_enable_rpki:BuildRequires: pkgconfig(rtrlib) >= 0.8.0}
%{?_enable_backtrace:BuildRequires: pkgconfig(libunwind)}
%{?_enable_protobuf:BuildRequires: /usr/bin/protoc /usr/bin/protoc-c pkgconfig(libprotobuf-c) >= 0.14}
%{?_enable_dp_dpdk:BuildRequires: pkgconfig(libdpdk)}

Requires: /usr/bin/less
Conflicts: quagga
Conflicts: zebra
Provides: FRRouting = %EVR frrouting = %EVR

%description
FRRouting is free software that manages TCP/IP based routing protocols. It takes
a multi-server and multi-threaded approach to resolve the current complexity
of the Internet.

FRRouting supports BGP4, OSPFv2, OSPFv3, ISIS, RIP, RIPng, PIM, NHRP, PBR, EIGRP and BFD.

FRRouting is a fork of Quagga.

%prep
%setup
#%%patch -p1
%patch0001 -p1

%build
%autoreconf

%configure \
    --disable-static \
    %{subst_enable doc} \
    %{?_enable_doc_html:--enable-doc-html} \
    --sbindir=%frr_daemondir \
    --sysconfdir=%_sysconfdir/%name \
    --libdir=%frr_libdir \
    --libexecdir=%_libexecdir/%name \
    --with-moduledir=%frr_moduledir \
    --localstatedir=%frr_statedir \
    --enable-user=%frr_user \
    --enable-group=%frr_group \
    --enable-vty-group=%frrvty_group \
    --enable-configfile-mask=0640 \
    --enable-logfile-mask=0640 \
    --with-vtysh-pager=less \
    --enable-multipath=64 \
    %{subst_enable tcmalloc} \
    %{subst_enable snmp} \
    %{?_enable_config_rollbacks:--enable-config-rollbacks} \
    %{subst_enable grpc} \
    %{subst_enable zeromq} \
    %{subst_with libpam} \
    %{subst_enable ospfapi} \
    %{subst_enable ospfclient} \
    %{?_enable_shell_access:--enable-shell-access} \
    %{subst_enable realms} \
    %{subst_enable fpm} \
    %{subst_enable pcreposix} \
    %{subst_enable cumulus} \
    %{subst_enable datacenter} \
    %{subst_enable protobuf} \
    %{subst_enable rpki} \
    %{subst_enable scripting} \
    %{subst_enable backtrace} \
    %{?_enable_dp_dpdk:--enable-dp-dpdk} \
    --with-crypto=openssl

%make_build MAKEINFO="makeinfo --no-split" PYTHON=%__python3

# Build info documentation
#%%make_build -C doc info

%install
%makeinstall_std

install -d %buildroot%_sysconfdir/%name

install -d %buildroot%_docdir/%name
# remove stray buildinfo files
find %buildroot%_docdir/%name -type f -name .buildinfo -delete

install -d -m 0755 %buildroot%_logdir/%name

rm -rf %buildroot%_infodir/dir

install -p -D -m 644 %SOURCE1 %buildroot%_tmpfilesdir/%name.conf
sed -e "s|@frr_statedir@|%frr_statedir|g" -i %buildroot%_tmpfilesdir/%name.conf
install -p -D -m 644 tools/etc/frr/daemons %buildroot%_sysconfdir/%name/daemons
install -p -D -m 644 tools/frr.service %buildroot%_unitdir/%name.service

install -p -D -m 644 redhat/frr.logrotate %buildroot%_logrotatedir/%name
install -p -D -m 644 redhat/frr.pam %buildroot%_sysconfdir/pam.d/%name

rm -f %buildroot%frr_daemondir/ssd
mkdir -p %buildroot%_initdir
mv %buildroot%frr_daemondir/%name %buildroot%_initdir/%name

# Delete libtool archives
find %buildroot -type f -name "*.la" -delete -print

#Upstream does not maintain a stable API, these headers from -devel subpackage are no longer needed
rm %buildroot%_libdir/%name/*.so
rm -r %buildroot%_includedir

cat > %buildroot%_sysconfdir/%name/%name.conf << __EOF__
!hostname frr

!password frr
!enable password frr

log file %_logdir/%name/%name.log
__EOF__
cat > %buildroot%_sysconfdir/%name/vtysh.conf << __EOF__
! vtysh is using PAM authentication allowing root to use it.
__EOF__

#%%check
#%%make_build check PYTHON=%%__python3

%pre
groupadd -r -f %frr_group
groupadd -r -f %frrvty_group

useradd -r -g %frr_group -G %frrvty_group -d %frr_home -s /sbin/nologin -c "FRRouting suite" %frr_user >/dev/null 2>&1 ||:
usermod -G %frrvty_group %frr_user >/dev/null 2>&1 ||:

%post
%tmpfiles_create %_tmpfilesdir/%name.conf ||:
%post_service %name

# Create dummy files if they don't exist so basic functions can be used.
if [ ! -e %_sysconfdir/%name/%name.conf ]; then
    echo "hostname `hostname`" > %_sysconfdir/%name/%name.conf
    chown %frr_user:%frr_group %_sysconfdir/%name/%name.conf
    chmod 640 %_sysconfdir/%name/%name.conf
fi

#still used by vtysh, this way no error is produced when using vtysh
if [ ! -e %_sysconfdir/%name/vtysh.conf ]; then
    touch %_sysconfdir/%name/vtysh.conf
    chmod 640 %_sysconfdir/%name/vtysh.conf
    chown %frr_user:%frrvty_group %_sysconfdir/%name/vtysh.conf
fi

%preun
%preun_service %name

%files
%doc README.md doc/mpls
%_docdir/%name/html
%dir %attr(750,%frr_user,%frr_group) %_sysconfdir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %attr(644,%frr_user,%frr_group) %_sysconfdir/frr/daemons
%config(noreplace) %attr(640,%frr_user,%frr_group) %_sysconfdir/%name/[!v]*.conf*
%config(noreplace) %attr(640,%frr_user,%frrvty_group) %_sysconfdir/%name/vtysh.conf
%config(noreplace) %_sysconfdir/pam.d/frr
%dir %attr(755,root,%frr_group) %_logdir/%name
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%frr_libdir
#%%frr_moduledir
%frr_daemondir
%_unitdir/%name.service
%_initdir/%name
%_datadir/yang/*.yang
%_tmpfilesdir/%name.conf

%changelog
* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 8.4.2-alt1
- 8.4.2

* Mon Oct 10 2022 Alexey Shabalin <shaba@altlinux.org> 8.3.1-alt1
- 8.3.1

* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 8.2.2-alt1
- 8.2.2

* Sat Feb 19 2022 Alexey Shabalin <shaba@altlinux.org> 8.1-alt1
- Initial build

