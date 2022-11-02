%define nm_version 1.2.28
%define nm_applet_version 1.2.28
%define nm_applet_name NetworkManager-applet-gtk

%def_with gtk4
%def_without libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-fortisslvpn
Version: 1.4.0
Release: alt1
License: %gpl2plus
Group: System/Configuration/Networking
Summary: Fortinet compatible SSLVPN support for NetworkManager
Url: https://gitlab.gnome.org/GNOME/NetworkManager-fortisslvpn.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: intltool
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
%if_with gtk4
BuildRequires: libgtk4-devel
BuildRequires: libnma-gtk4-devel
%else
BuildRequires: libgtk+3-devel
%endif
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

%package gtk4
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-fortisslvpn = %version-%release

%description gtk4
This package contains applications for use with
NetworkManager panel applet build with gtk4.

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
%if_with gtk4
	--with-gtk4 \
%endif
	--disable-silent-rules
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files -f %name.lang
%doc AUTHORS README
%_libexecdir/NetworkManager/nm-fortisslvpn-service
%_libexecdir/NetworkManager/nm-fortisslvpn-pinentry
%_libdir/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%_libdir/pppd/*/*-plugin.so
%config %_sysconfdir/dbus-1/system.d/nm-fortisslvpn-service.conf
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-fortisslvpn-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-fortisslvpn-service.name
%attr(700,root,root) %dir %_localstatedir/%name
%_datadir/appdata/*.xml
%exclude %_libdir/pppd/*/*-plugin.la
%exclude %_libdir/NetworkManager/*.la

%files gtk
%if_with libnm_glib
%_libdir/NetworkManager/libnm-fortisslvpn-properties.so*
%endif
%_libexecdir/NetworkManager/nm-fortisslvpn-auth-dialog
%_libdir/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so

%files gtk4
%_libdir/NetworkManager/libnm-gtk4-vpn-plugin-fortisslvpn-editor.so

%changelog
* Wed Nov 02 2022 L.A. Kostis <lakostis@altlinux.ru> 1.4.0-alt1
- Build with gtk4 support.

* Thu Jan 07 2021 L.A. Kostis <lakostis@altlinux.ru> 1.2.10-alt1
- 1.2.10.

* Fri Nov 09 2018 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt1.1
- NMU: Disable libnm-glib-* support.
- NMU: Fix build without libnm-glib-*.

* Thu Mar 22 2018 L.A. Kostis <lakostis@altlinux.ru> 1.2.8-alt1
- 1.2.8.
- remove configuration hack.

* Thu Jan 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.2.6-alt3
- don't expose configuration to public.

* Thu Jan 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.2.6-alt2
- Fix unresolved symbols (#rhbz 1512606).

* Thu Jan 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.2.6-alt1
- initial build for ALTLinux.
