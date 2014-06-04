
Name: realmd
Version: 0.15.1
Release: alt1
Summary: Kerberos realm enrollment service
License: LGPLv2+
Group: Security/Networking
Url: http://www.freedesktop.org/software/realmd/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool >= 0.35.0
BuildRequires: pkgconfig(glib-2.0) >= 2.32.0 pkgconfig(gio-2.0) >= 2.32.0 pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd-journal)
BuildRequires: /usr/bin/krb5-config
BuildRequires: libldap-devel
BuildRequires: xsltproc xmlto

%description
realmd is a DBus system service which manages discovery and enrollment in realms
and domains like Active Directory or IPA. The control center uses realmd as the
back end to 'join' a domain simply and automatically configure things correctly.

%package devel-docs
Summary: Developer documentation files for %name
Group: Development/Documentation

%description devel-docs
The %name-devel package contains developer documentation for developing
applications that use %name.

%define _localstatedir /var

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%find_lang realmd

%check
%make_build check

%files -f realmd.lang
%doc AUTHORS COPYING NEWS README
%_sysconfdir/dbus-1/system.d/org.freedesktop.realmd.conf
%_sbindir/realm
%dir %_libdir/realmd
%_libdir/realmd/*
%_unitdir/realmd.service
%_datadir/dbus-1/system-services/org.freedesktop.realmd.service
%_datadir/polkit-1/actions/org.freedesktop.realmd.policy
%_man8dir/realm.*
%_man5dir/realmd.conf.*
%_localstatedir/cache/realmd/

%files devel-docs
%doc %_datadir/doc/realmd/

%changelog
* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Wed Apr 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.15.0-alt1
- initial build
- disable PackageKit support
