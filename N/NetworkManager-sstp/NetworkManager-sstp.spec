%define nm_version 0.9.4.0
%define nm_applet_version 0.9.4.0
%define nm_applet_name NetworkManager-applet-gtk
%define ppp_version 2.4.5
%define gtkver 3

Name: NetworkManager-sstp
Version: 0.9.8.0
Release: alt1
License: %gpl2plus
Group: System/Configuration/Networking
Summary:  NetworkManager VPN plugin for SSTP

Url: http://www.gnome.org/projects/NetworkManager/

Source: %name-%version.tar
Patch:  gtk-table-to-gtk-grid.patch
Requires: NetworkManager >= %nm_version
Requires: sstp-client
Requires: ppp = %ppp_version

BuildRequires(pre): rpm-build-licenses
BuildRequires: ppp-devel libsstp-devel >= 1.0.8
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: NetworkManager-glib-devel >= %nm_version
BuildRequires: libgtk+%gtkver-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libdbus-glib-devel >= 0.74
BuildRequires: intltool gettext

%description
This package contains software for integrating the sstp VPN software
with NetworkManager and the GNOME desktop

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: shared-mime-info >= 0.16
Requires: gnome-keyring
Requires: %nm_applet_name >= %nm_applet_version
Requires: NetworkManager-sstp = %version-%release

Obsoletes: %name-gnome < 0.9.8.0
Provides: %name-gnome = %version-%release

%description gtk
This package contains GNOME applications for use with
NetworkManager panel applet.

%prep
%setup
%patch -p1

%build
rm -f m4/{intltool,libtool,lt~obsolete,ltoptions,ltsugar,ltversion}.m4
%autoreconf
%configure \
    --disable-static \
    --enable-more-warnings=no \
    --libexecdir=%_libexecdir/NetworkManager \
    --localstatedir=%_var \
    --with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
    --with-gtkver=%gtkver

%make_build

%install
%makeinstall_std
%find_lang %name

%files
%doc AUTHORS ChangeLog COPYING
%config(noreplace) %_sysconfdir/dbus-1/system.d/nm-sstp-service.conf
%config(noreplace) %_sysconfdir/NetworkManager/VPN/nm-sstp-service.name
%_libexecdir/NetworkManager/nm-sstp-service
%_libdir/pppd/%ppp_version/*.so

%exclude %_libdir/pppd/%ppp_version/*.la

%files gtk -f %name.lang
%_libdir/NetworkManager/lib*.so*
%_libexecdir/NetworkManager/nm-sstp-auth-dialog
%_datadir/gnome-vpn-properties/sstp

%exclude %_libdir/NetworkManager/lib*.la

%changelog
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

