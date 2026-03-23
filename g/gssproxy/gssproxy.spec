%define _unpackaged_files_terminate_build 1
%define pubconfpath %_sysconfdir/gssproxy
%define gpstatepath %_sharedstatedir/gssproxy
%define _localstatedir %_var
%define gssproxy_user _gssproxy
%define gssproxy_group _gssproxy

%def_with check

Name: gssproxy
Version: 0.9.2
Release: alt1
Summary: GSSAPI Proxy

Group: System/Servers
License: %mit
Url: https://github.com/gssapi/gssproxy

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-valgrind

BuildRequires: libxslt
BuildRequires: xsltproc
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: gettext-devel
BuildRequires: pkg-config
BuildRequires: libkrb5-devel
BuildRequires: libselinux-devel
BuildRequires: libkeyutils-devel
BuildRequires: libini_config-devel >= 1.3.1
BuildRequires: libverto-devel
BuildRequires: libpopt-devel
BuildRequires: libsystemd-devel
BuildRequires: po4a
BuildRequires: libcap-devel

%if_with check
BuildRequires: /proc
BuildRequires: krb5-kdc
BuildRequires: krb5-doc
BuildRequires: nss_wrapper
BuildRequires: socket_wrapper
BuildRequires: openldap-clients
BuildRequires: openldap-servers

# https://pagure.io/gssproxy/issue/227
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif

BuildRequires: python3
%endif

%description
A proxy for GSSAPI credential handling.

%package nfs-server
Summary: GSSAPI Proxy configuration for NFS server
Group: System/Base
Requires: %name

%description nfs-server
GSSAPI Proxy configuration for NFS server

%package nfs-client
Summary: GSSAPI Proxy configuration for NFS client
Group: System/Base
Requires: %name

%description nfs-client
GSSAPI Proxy configuration for NFS client

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
        --with-cap \
	--with-pubconf-path=%pubconfpath \
	--with-gpstate-path=%gpstatepath \
	--with-initscript=systemd \
	--with-systemdunitdir=%_unitdir \
	--disable-static \
	--disable-rpath \
	--with-gpp-default-behavior=REMOTE_FIRST

%make_build all

%check
%make_build test_proxymech

# https://pagure.io/gssproxy/issue/227
%make check \
%ifnarch %valgrind_arches
	CHECKARGS="--valgrind-cmd=" \
%endif
	%nil


%install
%makeinstall_std

install -d -m0755 %buildroot%_sysconfdir/gssproxy
install -m0644 examples/gssproxy.conf %buildroot%_sysconfdir/gssproxy/gssproxy.conf
install -m0644 examples/24-nfs-server.conf %buildroot%_sysconfdir/gssproxy/
install -m0644 examples/99-network-fs-clients.conf %buildroot%_sysconfdir/gssproxy/
install -d -m755 %buildroot%_sysconfdir/gss/mech.d
install -m644 examples/proxymech.conf %buildroot%_sysconfdir/gss/mech.d/
mkdir -p %buildroot%gpstatepath/rcache
# do not pack la files
rm -f %buildroot%_libdir/%name/proxymech.la

# setup non-privileged user
grep -qs 'run_as_user' %buildroot%_sysconfdir/gssproxy/gssproxy.conf && exit 1
echo 'run_as_user = %gssproxy_user' >> %buildroot%_sysconfdir/gssproxy/gssproxy.conf

mkdir -p %buildroot%_unitdir/%name.service.d/
cat > %buildroot%_unitdir/%name.service.d/run_as_user.conf <<-'__SVC_EOF__'
[Service]
# required to set correct permissions for StateDirectory
Group=%gssproxy_group
PrivateTmp=yes
ProtectHome=true
ReadWritePaths=
# additional caps required if run_as_user is used (see drop_privs func)
# default CapabilityBoundingSet=CAP_DAC_OVERRIDE (also required by root)
CapabilityBoundingSet=CAP_SETUID CAP_SETGID CAP_SETPCAP CAP_SYS_PTRACE
# r for %gssproxy_group group (default UMask=0177)
UMask=0137
# required to resolve dns names
# default PrivateNetwork=yes
PrivateNetwork=false
# default IPAddressDeny=any
IPAddressDeny=
# default RestrictAddressFamilies=AF_UNIX AF_LOCAL
RestrictAddressFamilies=
# replicate permissions
# /var/lib/gssproxy 0755,root,%gssproxy_group
# /var/lib/gssproxy/clients 0770,root,%gssproxy_group
# /var/lib/gssproxy/rcache 0770,root,%gssproxy_group
StateDirectory=
StateDirectory=gssproxy
# rx for %gssproxy_group group (default StateDirectoryMode=0700)
# rx for others to access the default socket
StateDirectoryMode=0755
__SVC_EOF__

%pre
%_sbindir/groupadd -r -f %gssproxy_group >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %gssproxy_group -G _keytab -d %_sharedstatedir/gssproxy \
-s /dev/null -c "User for gssproxy" %gssproxy_user >/dev/null 2>&1 ||:

%post
%post_service gssproxy

%post nfs-server
%post_service gssproxy

%post nfs-client
%post_service gssproxy

%preun
%preun_service gssproxy

%preun nfs-server
%preun_service gssproxy

%preun nfs-client
%preun_service gssproxy

%triggerpostun -- gssproxy < 0.8.0-alt2
/bin/chown %gssproxy_user:%gssproxy_group %gpstatepath/rcache/* >/dev/null 2>&1 ||:
/bin/chown %gssproxy_user:%gssproxy_group %gpstatepath/clients/* >/dev/null 2>&1 ||:

%files
%_unitdir/%name.service
%_unitdir/%name.service.d/
%_sbindir/%name
%_userunitdir/gssuserproxy.service
%_userunitdir/gssuserproxy.socket
%attr(0755,root,%gssproxy_group) %dir %pubconfpath
%attr(0640,root,%gssproxy_group) %config(noreplace) %_sysconfdir/gssproxy/gssproxy.conf
%attr(0644,root,root) %config(noreplace) %_sysconfdir/gss/mech.d/proxymech.conf
%attr(0755,root,%gssproxy_group) %dir %gpstatepath
%attr(0770,root,%gssproxy_group) %dir %gpstatepath/clients
%attr(0770,root,%gssproxy_group) %dir %gpstatepath/rcache
%dir %_libdir/%name
%_libdir/%name/proxymech.so
%_man5dir/*
%_man8dir/*

%files nfs-server
%attr(0640,root,%gssproxy_group) %config(noreplace) %_sysconfdir/gssproxy/24-nfs-server.conf

%files nfs-client
%attr(0640,root,%gssproxy_group) %config(noreplace) %_sysconfdir/gssproxy/99-network-fs-clients.conf

%changelog
* Thu Dec 21 2023 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1
- 0.9.1 -> 0.9.2.

* Sat Dec 09 2023 Ivan A. Melnikov <iv@altlinux.org> 0.9.1-alt1.1
- NMU: fix FTBFS on loongarch64
  + use rpm-macros-valgrind;
  + backport tests/userproxytest.c fix from upstream.

* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- 0.8.4 -> 0.9.1.

* Thu Jan 21 2021 Stanislav Levin <slev@altlinux.org> 0.8.4-alt1
- 0.8.3 -> 0.8.4.

* Mon Apr 20 2020 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1
- 0.8.2 -> 0.8.3.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1
- 0.8.1 -> 0.8.2.

* Wed Apr 17 2019 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1.

* Wed Mar 06 2019 Ivan A. Melnikov <iv@altlinux.org> 0.8.0-alt3
- Run tests without valgrind on %%ix86 and mipsel.

* Sun Dec 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt2
- Added gssproxy config for nfs-server.
- Enabled running gssproxy as a non-privileged user.
- Enabled testing on aarch64.

* Thu Mar 15 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.0 -> 0.8.0

* Wed Nov 01 2017 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- New 0.7.0 version

* Thu Jul 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.
