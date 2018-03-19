%define _unpackaged_files_terminate_build 1
%define pubconfpath %_sysconfdir/gssproxy
%define gpstatepath %_sharedstatedir/gssproxy
%define _localstatedir %_var

%def_with check

Name: gssproxy
Version: 0.8.0
Release: alt1%ubt
Summary: GSSAPI Proxy

Group: System/Servers
License: %mit
Url: https://pagure.io/gssproxy

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-fedora-compat

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
BuildRequires: systemd
BuildRequires: po4a

%if_with check
BuildRequires: krb5-kdc
BuildRequires: krb5-doc
BuildRequires: nss_wrapper
BuildRequires: socket_wrapper
BuildRequires: openldap-clients
BuildRequires: openldap-servers
BuildRequires: valgrind
BuildRequires: python3
%endif

Requires: libkrb5
Requires: libkeyutils
Requires: libverto-module-base
Requires: libini_config >= 1.3.1
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
A proxy for GSSAPI credential handling.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
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

%ifarch x86_64
%make check
%endif

%install
%makeinstall_std
install -d -m755 %buildroot%_sysconfdir/gssproxy
install -m644 examples/gssproxy.conf %buildroot%_sysconfdir/gssproxy/gssproxy.conf
install -m644 examples/99-nfs-client.conf %buildroot%_sysconfdir/gssproxy/99-nfs-client.conf
mkdir -p %buildroot%_sysconfdir/gss/mech.d
install -m644 examples/mech %buildroot%_sysconfdir/gss/mech.d/gssproxy.conf
mkdir -p %buildroot%gpstatepath/rcache
# do not pack la files
rm -f %buildroot%_libdir/%name/proxymech.la

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun_with_restart %name.service

%files
%_unitdir/%name.service
%_sbindir/%name
%attr(755,root,root) %dir %pubconfpath
%attr(755,root,root) %dir %gpstatepath
%attr(700,root,root) %dir %gpstatepath/clients
%attr(700,root,root) %dir %gpstatepath/rcache
%attr(0600,root,root) %config(noreplace) %_sysconfdir/gssproxy/*.conf
%attr(0644,root,root) %config(noreplace) %_sysconfdir/gss/mech.d/*.conf
%dir %_libdir/%name
%_libdir/%name/proxymech.so
%_man5dir/*
%_man8dir/*

%changelog
* Thu Mar 15 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1%ubt
- 0.7.0 -> 0.8.0

* Wed Nov 01 2017 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1%ubt
- New 0.7.0 version

* Thu Jul 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.
