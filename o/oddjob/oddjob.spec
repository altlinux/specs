Name: oddjob
Version: 0.34.3
Release: alt1
Summary: A D-Bus service which runs odd jobs on behalf of client applications

Group: System/Servers
License: %bsdstyle
Url: http://www.fedorahosted.org/oddjob

Source: %name-%version.tar
Source1: oddjobd.init
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libdbus-devel libxml2-devel libpam0-devel libselinux-devel libsasl2-devel
BuildRequires: libkrb5-devel libcom_err-devel libsystemd-devel libldap-devel
BuildRequires: xmlto

%define _unpackaged_files_terminate_build 1

%description
oddjob is a D-Bus service which performs particular tasks for clients
which connect to it and issue requests using the system-wide message
bus.

%package mkhomedir
Summary: An oddjob helper which creates and populates home directories
Group: System/Servers
Requires: %name = %version-%release

%description mkhomedir
This package contains the oddjob helper which can be used by the
pam_oddjob_mkhomedir module to create a home directory for a user
at login-time.

%package sample
Summary: A sample oddjob service
Group: System/Servers
Requires: %name = %version-%release

%description sample
This package contains a trivial sample oddjob service.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
		--disable-static \
		--enable-pie \
		--enable-now \
		--with-selinux-acls \
		--with-selinux-labels \
		--without-python \
		--enable-xml-docs \
		--enable-systemd \
		--disable-sysvinit \
		--enable-sample
%make_build

%install
%makeinstall_std

# Make sure we don't needlessly make these docs executable.
chmod -x src/reload src/mkhomedirfor src/mkmyhomedir

# Install initscript
install -Dm0755 %SOURCE1 %buildroot%_initdir/oddjobd

# Sample
install -m644 sample/oddjobd-sample.conf	%buildroot/%_sysconfdir/%{name}d.conf.d/
install -m644 sample/oddjob-sample.conf		%buildroot/%_sysconfdir/dbus-1/system.d/
install -m755 sample/oddjob-sample.sh		%buildroot/%_libexecdir/%name/

%files
%doc *.dtd COPYING NEWS QUICKSTART doc/oddjob.html src/reload
%_unitdir/oddjobd.service
%_initrddir/oddjobd
%_bindir/*
%_sbindir/*
%config(noreplace) %_sysconfdir/dbus-*/system.d/oddjob.conf
%config(noreplace) %_sysconfdir/oddjobd.conf
%dir %_sysconfdir/oddjobd.conf.d
%config(noreplace) %_sysconfdir/oddjobd.conf.d/oddjobd-introspection.conf
%dir %_sysconfdir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/sanity.sh
%_mandir/*/oddjob.*
%_mandir/*/oddjob_request.*
%_mandir/*/oddjobd.*
%_mandir/*/oddjobd-introspection.*

%files mkhomedir
%doc src/mkhomedirfor src/mkmyhomedir
%_libexecdir/%name/mkhomedir
%_libdir/security/pam_oddjob_mkhomedir.so
%_mandir/*/pam_oddjob_mkhomedir.*
%_mandir/*/oddjob-mkhomedir.*
%_mandir/*/oddjobd-mkhomedir.*
%config(noreplace) %_sysconfdir/dbus-*/system.d/oddjob-mkhomedir.conf
%config(noreplace) %_sysconfdir/oddjobd.conf.d/oddjobd-mkhomedir.conf

%exclude %_libdir/security/pam_oddjob_mkhomedir.la

%files sample
%_libexecdir/%name/oddjob-sample.sh
%config %_sysconfdir/dbus-*/system.d/oddjob-sample.conf
%config %_sysconfdir/oddjobd.conf.d/oddjobd-sample.conf

%post
%post_service oddjobd

%preun
%preun_service oddjobd

%changelog
* Mon Jun 27 2016 Mikhail Efremov <sem@altlinux.org> 0.34.3-alt1
- Initial build.

