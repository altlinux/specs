
%define _localstatedir %_var

Name: connman
Version: 1.10
Release: alt2

Summary: ConnMan is a daemon for managing internet connections.
License: %gpl2only
Group: Networking/Other
Url: http://connman.net/
#Packager: Serg A. Kotlyarov <shadowsbrother@gmail.com>
Source: %name.tar
Source1: connmand.init

BuildRequires: rpm-build-licenses gcc-c++ glib2-devel iptables-devel libdbus-devel wpa_supplicant
BuildRequires: gtk-doc libgnutls-devel libreadline-devel
BuildRequires: openconnect openvpn vpnc xl2tpd
BuildRequires: ppp-devel
BuildRequires: libpolkit-devel libselinux-devel
BuildRequires: systemd-devel

%description
The Connection Manager (ConnMan) project provides a daemon for
managing internet connections within embedded devices running
the Linux operating system. ConnMan is designed to be slim
and to use as few resources as possible, so it can be easily integrated.
It is a fully modular system that can be extended, through plug-ins,
to support all kinds of wired or wireless technologies.
The plug-in approach allows for easy adaption and modification
for various use cases.

%package -n %name-docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description -n %name-docs
This package contains documentation files for %name

%package -n %name-devel
Summary: Include files for development with ConnMan Library
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
The Connection Manager (ConnMan) project provides a daemon for managing
internet connections within embedded devices running the Linux operating system.

This package contains include files required for development %name-based software.

%prep
%setup -n %name

%build
%autoreconf
./configure \
--prefix=%_usr \
--sysconfdir=%_sysconfdir \
--localstatedir=%_localstatedir \
--enable-client \
--enable-nmcompat \
--enable-polkit \
--enable-selinux \
--enable-openconnect \
--enable-openvpn \
--enable-vpnc \
--enable-l2tp \
--enable-pptp
%make_build

%install
%makeinstall dbusconfdir=%buildroot%_sysconfdir/dbus-1/system.d systemdunitdir=%buildroot%_unitdir
install -pm0755 -D %SOURCE1 %buildroot%_initdir/connmand

%files
%_sbindir/*
%_sysconfdir/dbus-1/system.d/*.conf
%_datadir/dbus-1/system-services/*.service
%_initdir/connmand
%_unitdir/%{name}*
%dir %_libdir/%name
%dir %_libdir/%name/plugins*
%_libdir/%name/plugins*/*.so
%dir %_libdir/%name/scripts
%_libdir/%name/scripts/*.so.*
%_libdir/%name/scripts/*-script
%_datadir/polkit-1/actions/*

%files -n %name-docs
%doc AUTHORS README TODO README ChangeLog doc/*.txt

%files -n %name-devel
%_pkgconfigdir/*.pc
%_includedir/*
%exclude %_libdir/%name/plugins*/*.la
%_libdir/%name/scripts/*.so
%exclude %_libdir/%name/scripts/*.la


%changelog
* Tue Jan 22 2013 Paul Wolneykien <manowar@altlinux.ru> 1.10-alt2
- Fix the storagedir location.

* Fri Jan 18 2013 Paul Wolneykien <manowar@altlinux.ru> 1.10-alt1
- Build with additional features/plugins.
- New version 1.10.
- Add cronbuild scripts.

* Thu Jan 17 2013 Paul Wolneykien <manowar@altlinux.ru> 0.77-alt6
- Initial build for ALT Linux Sisyphus.
