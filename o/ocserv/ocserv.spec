%global _unpackaged_files_terminate_build 1
%define _localstatedir /var
%define _libexecdir %_prefix/libexec
%def_with maxmind
%def_enable man
%def_disable check
%def_enable oidc_auth

Name: ocserv
Version: 1.3.0
Release: alt1

Summary: OpenConnect SSL VPN server
License: GPLv2+
Group: System/Servers

Url: https://ocserv.openconnect-vpn.net
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libnettle-devel >= 2.7
BuildRequires: libgnutls-devel >= 3.3.0
BuildRequires: libprotobuf-c-devel protobuf-c-compiler
BuildRequires: libev-devel
BuildRequires: libtalloc-devel
BuildRequires: libnl-devel >= 3.1
%if_with maxmind
BuildRequires: libmaxminddb-devel >= 1.0.0
%else
BuildRequires: libGeoIP-devel >= 1.6.0
%endif
BuildRequires: libreadline-devel
BuildRequires: liboath-devel
BuildRequires: libpam-devel
BuildRequires: uid_wrapper socket_wrapper nss_wrapper pam_wrapper
BuildRequires: libradcli-devel >= 1.2.5
BuildRequires: libseccomp-devel
BuildRequires: libsystemd-devel
BuildRequires: libhttp-parser-devel
BuildRequires: liblz4-devel
BuildRequires: libkrb5-devel libtasn1-devel >= 3.4
BuildRequires: libpcl-devel
BuildRequires: iproute2 gnutls-utils
BuildRequires: gperf
BuildRequires: haproxy
BuildRequires: openconnect
BuildRequires: curl
BuildRequires: ipcalc
BuildRequires: gssntlmssp
BuildRequires: /proc
%if_enabled man
BuildRequires: /usr/bin/ronn
%endif
%if_enabled oidc_auth
BuildRequires: libcjose-devel libcurl-devel libjansson-devel
%endif

Requires: gnutls-utils
Requires: iproute2

%description
OpenConnect server (ocserv) is an SSL VPN server. Its purpose is to be a
secure, small, fast and configurable VPN server. It implements the OpenConnect
SSL VPN protocol, and has also (currently experimental) compatibility with
clients using the AnyConnect SSL VPN protocol. The OpenConnect VPN protocol
uses the standard IETF security protocols such as TLS 1.2, and Datagram TLS
to provide the secure VPN service.

%prep
%setup
%patch -p1

rm -f src/http-parser/http_parser.c src/http-parser/http_parser.h
rm -rf src/protobuf/protobuf-c/
touch src/*.proto
rm -rf src/ccan/talloc
rm -f src/pcl/*.c src/pcl/*.h
sed -i 's|/etc/ocserv.conf|/etc/ocserv/ocserv.conf|g' src/config.c
sed -i 's/run-as-group = nogroup/run-as-group = nobody/g' tests/data/*.config

%build
%autoreconf

%configure \
    --enable-systemd \
    --without-libwrap \
    --without-root-tests \
    --runstatedir=/run \
    %{subst_with maxmind} \
    %{?_enable_oidc_auth:--enable-oidc-auth}
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/pam.d
mkdir -p %buildroot%_sysconfdir/ocserv
install -p -m 644 ocserv-pamd.conf %buildroot%_sysconfdir/pam.d/ocserv
install -p -m 644 ocserv.conf %buildroot%_sysconfdir/ocserv
mkdir -p %buildroot%_localstatedir/lib/ocserv
install -p -m 644 doc/profile.xml %buildroot%_localstatedir/lib/ocserv
mkdir -p %buildroot%_unitdir
install -p -m 644 doc/systemd/standalone/%name.service %buildroot%_unitdir
install -p -m 755 doc/scripts/ocserv-script %buildroot%_bindir
mkdir -p %buildroot%_initrddir
install -D -m 0755 ocserv.init %buildroot%_initrddir/%name

%check
export PATH=/sbin:/usr/sbin:$PATH
%make check VERBOSE=1

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -g %name -G %name  -c 'Ocserv VPN Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name
    
%preun
%preun_service %name

%files
%doc NEWS COPYING README.md
%dir %_sharedstatedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%{name}.conf
%config(noreplace) %_sysconfdir/pam.d/%name
%if_enabled man
%_man8dir/*
%endif
%_bindir/ocpasswd
%_bindir/occtl
%_bindir/%name-script
%_sbindir/%name
%_sbindir/%name-worker
%_libexecdir/%name-fw
%_sharedstatedir/ocserv/profile.xml
%_unitdir/%{name}.service
%_initdir/%name

%changelog
* Fri May 31 2024 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Fri Jan 26 2024 Alexey Shabalin <shaba@altlinux.org> 1.2.4-alt1
- New version 1.2.4.

* Sun Nov 26 2023 Nikolay Burykin <bne@altlinux.org> 1.2.1-alt2
- build with --enable-oidc-auth

* Thu Sep 07 2023 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- new version 1.2.1

* Tue Dec 27 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.6-alt2
- Backported upstream patches
- Disable check (new hasher or make?)

* Wed Mar 02 2022 Alexey Shabalin <shaba@altlinux.org> 1.1.6-alt1
- new version 1.1.6

* Wed Dec 22 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Thu Sep 16 2021 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1.1
- introduce man knob (on by default)

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.3-alt1
- new version 1.1.3

* Fri May 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt3
- fixed check on 32-bit arches (glebfm@)

* Sun May 16 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt2
- disable check for 32-bit arches

* Fri Jan 29 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Tue Nov 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Tue Jul 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt1
- new version 1.0.1

* Thu Apr 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Thu Dec 19 2019 Alexey Shabalin <shaba@altlinux.org> 0.12.5-alt1
- 0.12.5
- build with libmaxminddb

* Tue Sep 24 2019 Alexey Shabalin <shaba@altlinux.org> 0.12.4-alt1
- initial build for ALT

