%define nm_version 1.2.0
%define nm_applet_version 1.2.0
%define nm_applet_name NetworkManager-applet-gtk

%def_with libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-fortisslvpn
Version: 1.2.6
Release: alt2
License: %gpl2plus
Group: System/Configuration/Networking
Summary: Fortinet compatible SSLVPN support for NetworkManager
Url: https://git.gnome.org/browse/network-manager-fortisslvpn
# git://git.gnome.org/network-manager-fortisslvpn
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: intltool
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
BuildRequires: libgtk+3-devel
BuildRequires: libsecret-devel
BuildRequires: ppp-devel

Requires: NetworkManager-daemon >= %nm_version
Requires: openfortivpn

%description
Fortinet SSLVPN support for NetworkManager

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-fortisslvpn = %version-%release

Obsoletes: %name-gnome < 0.9.8.4
Provides: %name-gnome = %version-%release

%description gtk
This package contains applications for use with
NetworkManager panel applet.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
%if_without libnm_glib
	--without-libnm-glib \
%endif
	--disable-silent-rules
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files
%doc AUTHORS README
%_libexecdir/NetworkManager/nm-fortisslvpn-service
%_libdir/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%_libdir/pppd/*/*-plugin.so
%config %_sysconfdir/dbus-1/system.d/nm-fortisslvpn-service.conf
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-fortisslvpn-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-fortisslvpn-service.name

%files gtk -f %name.lang
%if_with libnm_glib
%_libdir/NetworkManager/libnm-fortisslvpn-properties.so*
%endif
%_libexecdir/NetworkManager/nm-fortisslvpn-auth-dialog
%_libdir/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so
%_datadir/appdata/*.xml

%exclude %_libdir/pppd/*/*-plugin.la
%exclude %_libdir/NetworkManager/*.la

%changelog
* Thu Jan 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.2.6-alt2
- Fix unresolved symbols (#rhbz 1512606).

* Thu Jan 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.2.6-alt1
- initial build for ALTLinux.


