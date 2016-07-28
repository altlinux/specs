Name: gssproxy
Version: 0.5.1
Release: alt1
Summary: GSSAPI Proxy

Group: System/Servers
License: %mit
Url: http://fedorahosted.org/gss-proxy

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libverto-devel
BuildRequires: libini_config-devel
BuildRequires: libkrb5-devel
BuildRequires: libselinux-devel
BuildRequires: libpopt-devel
#BuildRequires: libkeyutils-devel
BuildRequires: doxygen po4a xml-utils docbook-style-xsl

%define _unpackaged_files_terminate_build 1
%define pubconfpath %_sysconfdir/gssproxy
%define gpstatepath %_localstatedir/gssproxy

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
	--with-gpp-default-behavior=REMOTE_FIRST \
	--with-manpages \
	--with-selinux

%make_build

%install
%makeinstall_std
install -d -m755 %buildroot%_sysconfdir/gssproxy
install -m644 examples/gssproxy.conf %buildroot%_sysconfdir/gssproxy/gssproxy.conf
install -m644 examples/24-nfs-server.conf %buildroot%_sysconfdir/gssproxy/24-nfs-server.conf
install -m644 examples/99-nfs-client.conf %buildroot%_sysconfdir/gssproxy/99-nfs-client.conf
mkdir -p %buildroot%_sysconfdir/gss/mech.d
install -m644 examples/mech %buildroot%_sysconfdir/gss/mech.d/gssproxy.conf
mkdir -p %buildroot%gpstatepath/rcache

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING
%_unitdir/gssproxy.service
%_sbindir/gssproxy
%attr(755,root,root) %dir %pubconfpath
%attr(755,root,root) %dir %gpstatepath
%attr(700,root,root) %dir %gpstatepath/clients
%attr(700,root,root) %dir %gpstatepath/rcache
%attr(0600,root,root) %config(noreplace) %_sysconfdir/gssproxy/*.conf
%attr(0644,root,root) %config(noreplace) %_sysconfdir/gss/mech.d/*.conf
%_libdir/gssproxy/
%_man5dir/*
%_man8dir/*

%exclude %_libdir/gssproxy/*.la

%changelog
* Thu Jul 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.
