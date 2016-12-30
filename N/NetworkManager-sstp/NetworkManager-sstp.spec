%define nm_version 1.1.0
%define nm_applet_version 1.1.0
%define nm_applet_name NetworkManager-applet-gtk
%define ppp_version %((%{__awk} '/^#define VERSION/ { print $NF }' /usr/include/pppd/patchlevel.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')

%def_with libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-sstp
Version: 1.2.2
Release: alt1
License: %gpl2plus
Group: System/Configuration/Networking
Summary:  NetworkManager VPN plugin for SSTP

Url: https://github.com/enaess/network-manager-sstp/

Source: %name-%version.tar
#Patch:  gtk-table-to-gtk-grid.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: ppp-devel libsstp-devel >= 1.0.8
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
BuildRequires: libgtk+3-devel
BuildRequires: libsecret-devel
BuildRequires: intltool gettext

Requires: NetworkManager-daemon >= %nm_version
Requires: sstp-client
Requires: ppp = %ppp_version

%description
This package contains software for integrating the sstp VPN software
with NetworkManager and the GNOME desktop

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-sstp = %version-%release

Obsoletes: %name-gnome < 0.9.8.0
Provides: %name-gnome = %version-%release

%description gtk
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup
#%patch -p1

%build
rm -f m4/{intltool,libtool,lt~obsolete,ltoptions,ltsugar,ltversion}.m4
%autoreconf
%configure \
    --disable-static \
    --libexecdir=%_libexecdir/NetworkManager \
    --localstatedir=%_var \
    --with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
%if_without libnm_glib
    --without-libnm-glib \
%endif
    --enable-more-warnings=error

%make_build

%install
%makeinstall_std
%find_lang %name

%files
%doc AUTHORS ChangeLog COPYING
%config %_sysconfdir/dbus-1/system.d/nm-sstp-service.conf
%_libexecdir/NetworkManager/nm-sstp-service
%_libdir/pppd/%ppp_version/*.so
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-sstp-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-sstp-service.name

%files gtk -f %name.lang
%if_with libnm_glib
%_libdir/NetworkManager/lib*.so*
%endif
%_libexecdir/NetworkManager/nm-sstp-auth-dialog
%_datadir/gnome-vpn-properties/*
%_datadir/appdata/*.xml

%exclude %_libdir/NetworkManager/lib*.la
%exclude %_libdir/pppd/%ppp_version/*.la

%changelog
* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.8.0-alt4
- rebuild with ppp-2.4.7

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt3
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt2
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt1
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.
- Updated to 0.9.8.

* Tue Apr 16 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.4.0-alt2.1
- Replace deprecated GtkTable by GtkGrid

* Thu Oct 25 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt2
- snapshot build
- rebuild with new sstp-client

* Mon May 21 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.4.0-alt1
- initial build

